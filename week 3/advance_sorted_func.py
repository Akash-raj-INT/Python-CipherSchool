cars=[
    {"model":"BMWki","price":7000000},
    {"model":"fortunre","price":1000000},
    {"model":"bolero","price":5500000},
    {"model":"mercidies","price":2100000000},
    {"model":"ferrari","price":454545445400000},
    {"model":"rolls royce","price":410000000000000},
    # last ke 2 khalredena mai tera ghar chala jayenga
]
print(sorted(cars,key= lambda x : x["price"]))
print(sorted(cars,key= lambda x : x["price"] , reverse = True))
