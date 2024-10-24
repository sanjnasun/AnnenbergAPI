from typing import List, Dict
import json

def findKeywords(user_pref: List[str], keywords: List[str]):
    # Define the preferences mapping
    preferences = {
        "technology/science": ["AI", "technology", "computer", "research", "innovation", "tech"],
        "entertainment": ["actor", "movie", "music", "celebrity", "film", "show", "art", "singer"],
        "USC": ["University of Southern California", "Trojans", "campus", "USC", "student", "Carol", "Folt", "DPS"],
        "politics": ["election", "government", "policy", "congress", "senate", "representatives", "voters", "president", "govenor", "democratic", "republican"],
        "sports": ["baseball", "basketball", "volleyball", "football", "soccer", "swimming", "olympics", "athlete", "score", "match"],
    }

    # List to hold all keywords for the user's preferences
    super_list = []

    # Loop through user preferences and add their associated keywords
    for curr_pref in user_pref: 
        list_of_keywords = preferences.get(curr_pref, [])
        super_list.extend(list_of_keywords)

    # Return the final list of keywords
    return super_list


# Sample JSON string representing articles (replace with actual JSON when available)
json_string = '{"article1": "Tech Innovation at USC", "article2": "USC Wins Championship", "article3": "Breakthrough in Quantum Physics"}'

# Step 1: Parse the JSON string into a Python dictionary
parsed_data = json.loads(json_string)

# Step 2: Create a new dictionary with the article names as keys and their words as values
transformed_data = {}
for key, article_name in parsed_data.items():
    # Split the article name into words and store them as the value
    word_list = article_name.split()
    transformed_data[article_name] = word_list

# Output the transformed dictionary
print("Transformed Article Data:", transformed_data)

# Use the transformed_data for keyword matching
# List of keywords related to preferences
keywords = findKeywords(["sports", "USC"], [])

# Traverse the transformed data and check for keyword presence
for article_name, word_list in transformed_data.items():
    word_set = set(word_list)
    keyword_set = set(keywords)
    
    # Find intersection between article words and preference keywords
    common_keywords = word_set.intersection(keyword_set)
    
    if common_keywords:
        print(f"The article '{article_name}' contains the keywords: {common_keywords}")
