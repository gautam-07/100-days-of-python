# **************************************************
# ✥ Title  :- Dictionaries and Nesting
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 1 January 2021
# **************************************************
# ✥ Dictionary in list
# **************************************************

# Nesting list inside dictionaries:-
# travel_log = {
#    "India": {"cities_visited": ["Chandigarh","Kota","Bengaluru"], "total_visits": 20}
# }


# Nesting dictionaries inside list:-
# travel_log = [
#    {
#       "country": "India",
#       "cities_visited": ["Chandigarh","Kota","Bengaluru"],
#       "total_visits": 20
#    },
# ]

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
def add_new_country(country_visited,times_visited,cites_visited):
   new_country = {}
   new_country["country"] = country_visited
   new_country["visits"]  = times_visited
   new_country["cities"]  = cites_visited
   travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

