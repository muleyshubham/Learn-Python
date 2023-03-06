#nested Functions
#function defined inside (inner function) another function body (outer function)

def outer_fn():
    print("Inside Outer Function")
    def inner_fn():
        print("Inside Inner Function")
    inner_fn()

outer_fn()
#inner_fn() #unresolved reference to inner_fn()
