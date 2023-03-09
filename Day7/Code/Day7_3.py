#list of collection where various number of columns in rows
def function1():
    numbers=[
        [10,20],
        [30,40,50],
        [60,70,80,90]
    ]

    for row in numbers:
        print(row)
    print("-"*80)

    for row in numbers:
        for value in row:
            print(f"val = {value}")

function1()
