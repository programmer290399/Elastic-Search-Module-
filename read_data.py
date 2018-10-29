import json 


def read_JSON(name):
    
    json_data=open(name).read()

    data = json.loads(json_data)

    menu = data['success']

    feed_back_data = list()

    for item in menu :
        dish_info = dict()
        dish_info["dish_name"] = item["dish_name"]
        dish_info["dish_id"] = item["dish_id"]
        dish_info["restaurant_id"] = item["restaurant_id"]
        dish_info["restaurant_name"] = item["restaurant_name"]
        feed_back_data.append(dish_info)    
    
    return(feed_back_data)



if __name__ == '__main__' :
   lst = read_JSON('menu.json')
   for e in lst :
       print(e)