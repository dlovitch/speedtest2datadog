# speedtest2datadog


### General

The name is silly.

### Pre-Flight
* Get yourself a `.env` file that looks like

```
DATADOG_API_KEY=xx
DATADOG_APP_KEY=xx
DATADOG_HOSTNAME=<hostname as it will appear in datadog>
```

The API and app keys can be managed at https://app.datadoghq.com/account/settings#api

The hostname is as it will appear in https://app.datadoghq.com/infrastructure

### Container Setup
* Run: `make`
  * Builds and runs container


### Container Removal
* Run: `make docker-destroy`


### Container Troubleshooting
* Run: `make docker-debug`

## TODO

1. Probably make it work inside Kubernetes.
2. Remove the `tail -f` in `entrypoint.sh`?


### Lessons Learned

The Internet is having problems during COVID-19.

### Resources
