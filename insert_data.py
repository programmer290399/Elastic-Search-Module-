from elasticsearch import Elasticsearch

from read_data import read_JSON 

es = Elasticsearch("http://localhost:9200")

if not es.indices.exists(index="dish_index"):
    es.indices.create(index = "dish_index", ignore = 400)

docs = read_JSON('menu.json')

for doc in docs :
        es.index(index="dish_index", doc_type="rest_dish_mapping", id = doc['dish_id'], body = doc , ignore = 400 )
        print('Successfully Inserted =>',doc)

