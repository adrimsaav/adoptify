"""
Handles user questions and interactions in the pet matchmaker app.
"""

def get_user_info():
    """Get user information through a series of questions."""
    print("\n=== Welcome to Adoptify: Your Perfect Pet Matchmaker! === \n")
    
    questions = {
        'age': "What is your age? ",
        'living_situation': "\nWhat is your living situation?\n1. Apartment\n2. House\n3. Rural property\nEnter number (1-3): ",
        'energy_level': "\nHow would you describe your energy level?\n1. Very active\n2. Moderately active\n3. Relatively calm\nEnter number (1-3): ",
        'social_preference': "\nWhat's your social preference?\n1. Very social/extroverted\n2. Balanced\n3. Quiet/introverted\nEnter number (1-3): ",
        'noise_tolerance': "\nWhat's your tolerance for pet noise?\n1. High - Don't mind frequent noise\n2. Medium - Occasional noise is fine\n3. Low - Prefer quiet pets\nEnter number (1-3): ",
        'size_preference': "\nWhat size pet do you prefer?\n1. Large\n2. Medium\n3. Small\nEnter number (1-3): ",
        'time_available': "\nHow many hours per day can you spend with your pet?\n1. More than 4 hours\n2. 2-4 hours\n3. Less than 2 hours\nEnter number (1-3): "
    }
    
    answers = {}
    
    for key, question in questions.items():
        """
        Iterates through a dictionary of questions to collect and validate user responses.
        Done with ChatGPT.

        - Function loops through each question in the `questions` dictionary, prompting 
        the user for input. It ensures valid responses by handling specific validation rules:
        - For the 'age' question: Users must be 18 or older.
        - For other questions: Users must input a number between 1 and 3.

        If an invalid response is entered, the user is prompted to try again until valid input is provided.

        Returns:
            dict: dictionary containing the user's validated responses.

        Raises:
            ValueError: if the input cannot be converted to an integer."""
        
        while True:
            try:
                if key == 'age':
                    answer = int(input(question))
                    if answer < 18:
                        print("Sorry, you must be 18 or older to adopt a pet.")
                        continue
                    answers[key] = answer
                else:
                    answer = int(input(question))
                    if answer not in [1, 2, 3]:
                        print("Please enter a number between 1 and 3.")
                        continue
                    answers[key] = answer
                break
            except ValueError:
                print("Please enter a valid number.")
    
    return answers

def display_match_results(matches):
    """Display the top matching pets to the user."""
    if not matches:
        print("\nSorry, no matching pets were found. Please try adjusting your preferences.")
        return
    
    print("\n=== Your Top Pet Matches ===\n")
    for i, (pet, score) in enumerate(matches, 1):
        print(f"Match #{i} (Compatibility Score: {score*100:.1f}%)")
        print(f"Type: {pet.type}")
        print(f"Breed: {pet.breed}")
        print(f"Age: {int(pet.age_months/12)} years, {pet.age_months%12} months")
        print(f"Size: {pet.size}")
        print(f"Gender: {'Male' if pet.gender == 'M' else 'Female'}")
        print(f"Color: {pet.color}")
        print(f"Time in Shelter: {pet.time_in_shelter} days")
        print(f"Adoption Fee: ${pet.adoption_fee}")
        print("-" * 50)
