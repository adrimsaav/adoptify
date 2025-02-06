"""
Driver: Adriana Saavedra, Kimberly Alfaro Mejia, Fred Effueze
Assignment: Exercise 6 INST326
Date: 12_12_24
Challenges Encountered:
We had challenges with error handling, and making sure csv file was being called and processed correctly.
Also, implementing pet matching logic and abstract class was difficult. Going back and forth between files made
this process long, especially with test_pet_matcher.py. 

"""
"""Main module for the Adoptify pet matchmaker program."""

import os
from questions import get_user_info, display_match_results
from pet_matcher import PetMatcher

def main():
    """Main function to run the pet matchmaker program."""
    csv_path = os.path.join(os.path.dirname(__file__), 'pet_adoption_data.csv')
    
    try:
        matcher = PetMatcher(csv_path)        
        user_info = get_user_info()
        matches = matcher.find_matches(user_info)
        display_match_results(matches)
        
    except FileNotFoundError:
        print("Error: Could not find the pet database file (pet_adoption_data.csv)")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
