default:
	make docker-build docker-run

docker-build:
	docker build -t speedtest2datadog .

docker-run:
	docker run --name speedtest2datadog -it --env-file ./.env speedtest2datadog

test:
	echo-test.sh

docker-stop:
	docker stop speedtest2datadog

docker-remove:
	docker rm speedtest2datadog && docker rmi speedtest2datadog

docker-destroy:
	make docker-stop docker-remove

docker-debug:
	docker run --rm -it speedtest2datadog /bin/bash
