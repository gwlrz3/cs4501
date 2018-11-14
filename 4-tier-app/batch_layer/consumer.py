from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
import time

success = False
while not success:
	try:
		consumer = KafkaConsumer('newListing', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
		success = True
		break
	except:
		time.sleep(5)
		success = False

es = Elasticsearch(['es'])


for message in consumer:
	data = json.loads((message.value).decode('utf-8'))
	print(data)
	es.index(index='listing_index', doc_type='listing', id=data['id'], body=data)
	es.indices.refresh(index='listing_index')
	

