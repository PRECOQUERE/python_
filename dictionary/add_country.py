#2022/10/13

from pickle import APPEND


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },  
]

def add_new_country(country, visited_count, cities_visited):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visited_count
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)