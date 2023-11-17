# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# for key in student_scores:
#   score = student_scores[key]
#   if 100 > score >= 91:
#     student_grades[key] = "Outstanding"
#   elif 91 > score >= 80: 
#     student_grades[key] = "Exceeds Expectations"
#   elif 81 > score >= 70:
#     student_grades[key] = "Acceptable"
#   else:
#     student_grades[key] = "Failed"


# # 🚨 Don't change the code below 👇
# print(student_grades)

# travel_log = {
#   "France": {
#     "cities visited": ["Monreal", "Paris", "Provance"],
#     "total_visits": 12
#   }
# }

# for i in travel_log["France"]:
#   print(i)


country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

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
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country, visits, list_of_cities):
  new_country = {}
  new_country["country"] = country
  new_country["visits"] = visits
  new_country["cities"] = list_of_cities

  travel_log.append(new_country)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")