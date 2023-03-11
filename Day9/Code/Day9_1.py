#collection of collection
def function1():
    mobile=[
        {"model":"oneplus","company":"OnePlus","price":50000},
        {"model": "apple", "company": "APPLE", "price": 60000},
        {"model": "samsung", "company": "SAMSUNG", "price": 40000},
        {"model": "oppo", "company": "OPPO", "price": 10000}
    ]
    #print(mobile)
    my_final_list=[]
    for m in mobile:
        my_final_list.append({"model":m['model'],
                              "price":m['price']

        })
    print(my_final_list)

function1()