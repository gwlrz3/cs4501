from kafka import KafkaConsumer
from elasticsearch import Elasticsearch


consumer = KafkaConsumer('newListing', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
es = Elasticsearch(['es'])


for message in consumer:
	data = json.loads((message.value).decode('utf-8'))
	es.index(index='listing_index', doc_type='listing', id=data['id'], body=data)
	es.indices.refresh(index="listing_index")

