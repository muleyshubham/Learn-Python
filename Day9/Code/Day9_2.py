#collection of collection
def function1():
    mobile=[
        {"model":"oneplus","company":"OnePlus","price":50000},
        {"model": "apple", "company": "APPLE", "price": 60000},
        {"model": "samsung", "company": "SAMSUNG", "price": 40000},
        {"model": "oppo", "company": "OPPO", "price": 10000}
    ]

    process_mobile= lambda mobile : {"model":mobile['model'],"price":mobile['price']}
    final_list=list(map(process_mobile,mobile))
    print(final_list)
#function1()

def function2():
    d1={"1":"RED","2":"GREEN","3":"YELLOW"}
    print(d1)
    #print(d1["1"])
    #print(d1.get("1"))
    d1.update({"4":"BLUE"})
    print(d1)

#function2()