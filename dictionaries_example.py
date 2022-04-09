# Dictionary example with correct formatting
programming_dictionary = { 
    "Bug": "An error in a program.", # Each key/value pair has it's own line, ended with a comma 
    "Function": "Code that can be used repeatedly.", 
} # Closing brace in line with the definition

# Retrieveing items from a dictionary.
print(programming_dictionary["Bug"]) # Key can be used as an index, check spelling if error occurs

# Add new items to dicitonary
programming_dictionary["Loop"] = "The action of doing something over and over."
print(programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}

# Clear existing dictionary
# programming_dictionary = {}
# print(programming_dictionary) # Useful for clearing user stats, e.g high scores

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary: #When looping through a dictionary, each pair is looped through, returning the key
    print(key)
    print(programming_dictionary[key])

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nest dictionary in dictionary

travel_log_with_visits = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 11},
}

#Nest dictionary inside a list

travel_log_with_visits = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 11
    },
]
