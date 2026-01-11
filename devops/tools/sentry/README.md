### Create Kafka Topics to use in Snuba:
```bash
docker compose --env-file .env run --pull=never --rm web upgrade --noinput --create-kafka-topics
```
