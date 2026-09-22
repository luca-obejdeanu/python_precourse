import pandas as pd

data = pd.read_csv("Day4/restaurants.csv")


def count_values(column):
    counts = {}
    for value in column:
        if value in counts:
            counts[value] = counts[value] + 1
        else:
            counts[value] = 1
    return counts


def show_info():
    print("restaurants:", data.shape[0])
    print("columns:", data.shape[1])
    print("cities:", len(set(data["city"])))
    print("average rating:", round(data["rating"].mean(), 2))


def per_city():
    counts = count_values(data["city"])
    for city in counts:
        print(city, "-", counts[city])


def rating_per_city():
    print(data.groupby("city")["rating"].mean())


show_info()
print()
per_city()
print()
rating_per_city()
