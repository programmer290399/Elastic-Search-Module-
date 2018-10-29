from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")
from operator import itemgetter
import sys 

query  = sys.argv[1]

response = es.search(index="dish_index", body={ "from": 0, "size": 1000 , "query": { "bool": { "must": { "match": { "dish_name": query } } ,"should": { "match": { "restaurant_name": query } } } } })

results = response['hits']['hits']

results = sorted(results, key=itemgetter('_score'), reverse=True)

# for result in results :
#     print(result)
    
print(results)
sys.stdout.flush()