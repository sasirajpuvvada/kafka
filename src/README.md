# kafka

# Create Topic
- kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic {first_topic_kafka}

# List Topics
- kafka-topics.sh --list --zookeeper zookeeper:2181

# Delete Topic
- kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic {first_topic_kafka}

# Producer shell command
- kafka-console-producer.sh --broker-list kafka:9092 --topic {first_topic_kafka}


# Consumer Shell command
- kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic {first_topic_kafka} --from-beginning