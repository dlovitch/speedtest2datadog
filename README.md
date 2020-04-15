# speedtest2datadog


### General

The name is silly.


### Pre-Flight
1. Get yourself a `.env` file that looks like

```
DATADOG_API_KEY=xx
DATADOG_APP_KEY=xx
```

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


### Resources
