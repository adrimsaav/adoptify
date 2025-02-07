![ScreenRecording2025-02-06at7 42 32PM-ezgif com-speed](https://github.com/user-attachments/assets/560f93bd-1e89-4eea-bdf1-2c8601514811)
# Adoptify: Pet Adoption Matchmaking Program
Welcome to **Adoptify**, a pet adoption matchmaking program designed to connect users with their ideal pets based on personality and lifestyle. Our aim is to make it personalized and give a match percentage as to how compatible a pet is for the User.

## Features
In our command-line program, the User is asked a series of questions about what type of pet they’re looking for, their living environment, activity levels, and preferences. Based on this input, Adoptify will analyze the local dataset sourced from Kaggle that contains detailed information about adoptable pets, including their physical traits, age, and other characteristics. The program utilizes local pet adoption data sourced from Kaggle, and offers personalized recommendations with compatibility scores.

## Getting Started
While staying on main.py, the User can run the program through the terminal. The first question would be how old the User is, and if the User enters an age younger than 18, the program will let the User know that they must be older than 18 in order to adopt a pet. 

<img width="423" alt="Screenshot 2025-02-06 at 7 50 22 PM" src="https://github.com/user-attachments/assets/dfc51af5-04f4-4a30-890f-501fdc139af2" />

From there, there will be a series of questions where the User must answer using numbers 1-3, depending on the answers provided (e.g. What is your living situation? (1) Apartment, (2) House, (3) Rural property). After six of these questions, the top three results will be displayed, like so:

<img width="545" alt="Screenshot 2025-02-06 at 7 49 11 PM" src="https://github.com/user-attachments/assets/81cb0708-b79f-4344-863d-d18c6dac8056" />

## Technologies Used
- **Python**
- **Kaggle**

## Presentation Video Link
https://drive.google.com/file/d/1_UD73kt5TVg4Wv1O-Wsu1zK_h_0TS9uF/view?usp=sharing

## pet_matcher.py
We used the ABC module for abstract classes and csv for reading/writing files, and the Pet class is an abstract base class for all pets, and its __init__ method initializes attributes (e.g., ID, type, breed, gender) from a dictionary.  Subclasses (Dog, Cat, Rabbit, Bird) implement the abstract methods for specific behaviors. Property methods provide getters/setters, while abstract methods (get_energy_level, get_social_level, get_noise_level) are defined for subclasses to implement. The to_dict method converts attributes into a dictionary, and __str__ and __repr__ provide readable and debugging output. The PetFactory class uses the create_pet static method to create pet objects based on type, raising a ValueError for unrecognized types. This was done through ChatGPT. The PetMatcher class matches pets to users. It initializes with a _pets list (populated from a CSV file) and a scoring dictionary for matching attributes. Using csv.DictReader, it reads the file, creates pet objects via PetFactory.create_pet, and stores them in _pets, handling errors with ValueError. Getter methods allow access to _pets and weights.

## questions.py
The questions.py file gathers user preferences and shows pet match results in the command-line program. The get_user_info function starts with a welcome message introducing Adoptify. It asks the user a series of questions stored in a dictionary, using \n for better readability. An empty answers dictionary collects the user’s responses. A loop goes through each question, ensuring valid inputs using while True. For the age question, users under 18 are shown an error and asked again, since they must be of age to adopt. Other questions require users to pick options (1, 2, or 3), with error handling for invalid inputs. Once all responses are valid, the function returns the answers dictionary. The display_match_results function shows the user's pet matches. If there are no matches, an error message is displayed. Otherwise, a message introduces the top matches. A loop goes through the matches (tuples of pet objects and compatibility scores), showing details like the match number, compatibility percentage, pet info, age (in years and months), shelter time, and adoption fee. Dividers are used to separate each match for clarity.


## test_pet_matcher.py
In test_pet_matcher.py, we use pytest as the testing framework and import os, along with the Pet, Dog, Cat, and PetMatcher classes from pet_matcher.py, which contains Adoptify's main logic. The @pytest.fixture decorator is used to define reusable data for tests. The pet_data() fixture provides sample pet data as a dictionary, ensuring tests can access consistent input. Another fixture sets up the PetMatcher instance, initializing it with the path to the .csv file.
The test_pet_initialization(pet_data) function checks if a Dog object is initialized correctly using pet_data. It creates a Dog object and verifies attributes like ID, energy level, and social level, ensuring they meet expected values. Similarly, the fixture data is modified to create and test a Cat object. The test_match_calculation(matcher_setup) function ensures the PetMatcher class calculates matches accurately. A user_preferences dictionary is created to represent user answers. The find_matches() method is called, and assertions check if the matches are as expected. If all tests pass, it confirms that Adoptify’s matching logic works properly.

## main.py
As you can see, we imported os and used it to construct the file path to the .csv file for our pet data. We import from questions import get_user_info, display_match_results from the questions.py module and for our last import, we have from pet_matcher import PetMatcher.
We now move on to the try-except statements, which is meant to catch any errors that may occur. For matcher = PetMatcher(csv_path), we create an instance of the PetMatcher class, passing the file path to the .csv file. The PetMatcher object reads and processes the pet data, which brings us to user_info = get_user_info(). This calls the get_user_info() function from questions.py. This function collects input from the user, which would be the user’s answers to our questionnaire. This collected data is stored in the user_info dictionary. We call the method, find_matches, of the PetMatcher class. This calculates the compatibility scores for each pet and returns the list of best-matching pets. Matches are stored in the matches variable. For error handling, this catches the specific error raised if .csv is not found. An error message is shown to tell the user that the database could not be found. 

## Key Takeaways 
- The simpler, the better!
- Pytest is your friend :)
