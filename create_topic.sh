#/bin/bash
/opt/bitnami/kafka/bin/kafka-topics.sh --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic test-topic
echo "topics have been created .."

/opt/bitnami/kafka/bin/kafka-consumer-groups.sh  --list --bootstrap-server kafka:9092
echo "Listing created topics ..."
