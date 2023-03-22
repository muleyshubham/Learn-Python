#list comprehesion on dictionary

products = [
    {"id":1,"title":"book","price":500},
    {"id":2,"title":"mobile","price":60000},
    {"id":3,"title":"laptop","price":90000},
    {"id":4,"title":"speaker","price":1500},
    {"id":5,"title":"ipad","price":40000},
]

def function1():
    def calc_tax(product):
        return product['price']*0.18

    taxes = [calc_tax(p) for p in products]
    print(taxes)
function1()

