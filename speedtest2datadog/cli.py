#! /usr/bin/env python3

# Builtins
import logging
import time

# Additional dependencies
import click
import datadog
import speedtest

# Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)
formatter = logging.Formatter('[%(asctime)s]:%(levelname)s:[%(name)s]:%(message)s')
console_logger = logging.StreamHandler()
console_logger.setFormatter(formatter)
logger.addHandler(console_logger)

def set_verbosity(ctx, param, verbose: int):
    """ Set verbosity of logging """
    if verbose > 1:
        logger.setLevel(logging.DEBUG)
    elif verbose > 0:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARN)

## Click options
cli_verbose = click.option(
    "-v",
    "--verbose",
    count=True,
    expose_value=False,
    callback=set_verbosity,
    help="Enable verbose logging",
)

cli_servers = click.option(
    "-s", "--servers",
    required=False,
    help="If you want to test against a specific server"
)

cli_threads = click.option(
    "-t", "--threads",
    required=False,
    help="If you want to use a single threaded test"
)

def test_speed(servers=None, threads=None):
    s = speedtest.Speedtest()
    # need to convert servers to list
    if servers:
        s.get_servers([servers])
    else:
        s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    results = s.results.dict()
    logger.debug(results["download"])
    logger.debug(results["upload"])
    logger.debug(results["ping"])
    logger.debug(results["server"]["id"])
    logger.debug(results["bytes_sent"])
    logger.debug(results["bytes_received"])
    return results


def send_results_to_datadog(results):
    datadog.initialize()
    now = time.time()
    metrics = []
    metrics.append({"metric": "spectrum_internet.download.bits"         , "points": (now, results["download"])          , "host": "Vinton", "tags": [f"""server_id:{results["server"]["id"]}"""]})
    metrics.append({"metric": "spectrum_internet.upload.bits"           , "points": (now, results["upload"])            , "host": "Vinton", "tags": [f"""server_id:{results["server"]["id"]}"""]})
    metrics.append({"metric": "spectrum_internet.ping.milliseconds"     , "points": (now, results["ping"])              , "host": "Vinton", "tags": [f"""server_id:{results["server"]["id"]}"""]})
    metrics.append({"metric": "spectrum_internet.data_sent.bytes"       , "points": (now, results["bytes_sent"])        , "host": "Vinton", "tags": [f"""server_id:{results["server"]["id"]}"""]})
    metrics.append({"metric": "spectrum_internet.data_received.bytes"   , "points": (now, results["bytes_received"])    , "host": "Vinton", "tags": [f"""server_id:{results["server"]["id"]}"""]})
    logger.debug(metrics)
    datadog.api.Metric.send(metrics)

@click.command()
@cli_verbose
@cli_servers
@cli_threads
def cli(servers: str=None, threads: str=None):
    """Main CLI entrypoint"""
    logger.debug(f"Servers: servers")
    logger.debug(f"Threads: threads")
    results = test_speed(servers, threads)
    send_results_to_datadog(results)


if __name__ == "__main__":
    cli(auto_envvar_prefix="ST2DD", servers=None, threads=None)