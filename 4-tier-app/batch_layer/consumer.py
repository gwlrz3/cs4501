from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

consumer = KafkaConsumer('newListing', group_id='listing-indexer', bootstrap_servers=['kafka:9092'], api_version = '0.9')
es = Elasticsearch(['es'])
# try:
# 	resp = es.indices.create(index='listing_index')

# except:
# 	print("error")


for message in consumer:
	data = json.loads((message.value).decode('utf-8'))
	print(data)
	es.index(index='listing_index', doc_type='listing', id=data['id'], body=data)
	es.indices.refresh(index='listing_index')
	

