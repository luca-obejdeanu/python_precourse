import pandas as pd

data = pd.read_csv("Day4/restaurants.csv")


def by_city(name):
    found = data[data["city"] == name]

    if found.shape[0] == 0:
        print("no city called", name)
        return

    print("restaurants in", name)
    for place in found["name"]:
        print("   ", place)


def good_ones(limit):
    found = data[data["rating"] > limit]
    print("rating above", limit)
    for place in found["name"]:
        print("   ", place)


def with_delivery():
    found = data[data["delivery"] == True]
    print("delivery available:", found.shape[0], "of", data.shape[0])
    for place in found["name"]:
        print("   ", place)


by_city("Madrid")
print()
good_ones(4.4)
print()
with_delivery()
