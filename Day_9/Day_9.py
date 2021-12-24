# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again.",
#     "Number": 2,
# }

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"],},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

print(travel_log["France"]["cities_visited"])