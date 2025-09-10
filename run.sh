# More additional internal tests:

# 1. Kafka that there are actually messages in the topic

docker exec -it podcast-monitoring-project-kafka-1 \
kafka-console-consumer --bootstrap-server localhost:9092 \
--topic podcast-files --from-beginning --timeout-ms 5000

# 2. Consumer that is consuming and processing

docker logs podcast-monitoring-project-consumer-1 --tail=50

# 3. Mongo that the files are being saved

docker exec -it podcast-monitoring-project-mongo-1 \
mongosh podcasts_db --eval "db.podcasts_files.files.find().limit(2).pretty()"

# 4. Elasticsearch that the metadata is coming in

curl "http://localhost:9200/podcasts_metadata_v2/_search?pretty&size=2"

# 5. Transcriber that is running

docker logs podcast-monitoring-project-transcriber-1 --tail=50

# 6. Analyzer running

docker logs podcast-monitoring-project-analyzer-1 --tail=50