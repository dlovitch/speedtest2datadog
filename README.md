# speedtest2datadog

The name is silly.

1. Get yourself a `.env` file that looks like

    ```
    DATADOG_API_KEY=xx
    DATADOG_APP_KEY=xx
    ```

1. `./build.sh`

1. `./run.sh`

## TODO

1. Probably make it work inside Kubernetes.
1. Remove the `tail -f` in `entrypoint.sh`?