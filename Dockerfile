FROM python:3.8-slim

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends \
    cron \
  && apt-get autoclean \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /var/cache/apt/archives
RUN mkdir /app
COPY entrypoint.sh /srv/entrypoint.sh
COPY echo-test.sh /app
COPY setup.py /app
COPY speedtest2datadog /app/speedtest2datadog
COPY cron /etc/cron.d/speedtest2datadog
RUN chmod 0755 /srv/entrypoint.sh
RUN chmod 0755 /app/echo-test.sh
RUN chmod 0644 /etc/cron.d/speedtest2datadog
RUN pip install virtualenv
RUN python -m virtualenv /app/venv
RUN /app/venv/bin/pip install -e /app
RUN crontab /etc/cron.d/speedtest2datadog
CMD /srv/entrypoint.sh
