"""
Handles pet matching algorithm and data processing using OOP.
"""

from abc import ABC, abstractmethod
import csv

class Pet(ABC):
    """Abstract base class for pets."""
    
    def __init__(self, pet_data):
        """Initialize pet with data from CSV."""
        self._id = pet_data['PetID']
        self._type = pet_data['PetType']
        self._breed = pet_data['Breed']
        self._gender = pet_data['Gender']
        self._age_months = int(pet_data['AgeMonths'])
        self._color = pet_data['Color']
        self._size = pet_data['Size']
        self._time_in_shelter = int(pet_data['TimeInShelterDays'])
        self._adoption_fee = int(pet_data['AdoptionFee'])

    
    @property
    def id(self):
        """Returns pet ID."""
        return self._id
    
    @property
    def type(self):
        """Returns pet type."""
        return self._type
    
    @property
    def breed(self):
        """Returns pet breed."""
        return self._breed
    
    @property
    def gender(self):
        """Returns pet gender."""
        return self._gender
    
    @property
    def age_months(self):
        """Returns pet age in months."""
        return self._age_months
    
    @property
    def color(self):
        """Returns pet color."""
        return self._color
    
    @property
    def size(self):
        """Returns pet size."""
        return self._size
    
    @property
    def time_in_shelter(self):
        """Returns time pet has been in shelter."""
        return self._time_in_shelter
    
    @property
    def adoption_fee(self):
        """Returns pet adoption fee."""
        return self._adoption_fee
    
    
    @abstractmethod
    def get_energy_level(self):
        """Return the energy level of the pet."""
        pass
    
    @abstractmethod
    def get_social_level(self):
        """Return the social level of the pet as a float between 0 and 1."""
        pass
    
    @abstractmethod
    def get_noise_level(self):
        """Return the noise level of the pet as a float between 0 and 1."""
        pass
    
    def to_dict(self):
        """Store pet information in a dictionary."""
        self.pet_dict = {
            'PetID': self._id,
            'PetType': self._type,
            'Breed': self._breed,
            'Gender': self._gender,
            'Age': self._age_months,
            'Color': self._color,
            'Size': self._size,
            'TimeInShelter': self._time_in_shelter,
            'AdoptionFee': self._adoption_fee,
            'EnergyLevel': self.get_energy_level(),
            'SocialLevel': self.get_social_level(),
            'NoiseLevel': self.get_noise_level()
        }
        return self.pet_dict

    def __str__(self):
        """Return string representation of pet."""
        return f"{self._type} - {self._breed} ({self._gender}, {self._age_months} months)"
    
    def __repr__(self):
        """Return detailed string representation of pet."""
        return f"Pet(ID: {self._id}, Type: {self._type}, Breed: {self._breed}, Age: {self._age_months} months)"

class Dog(Pet):
    """Class representing a dog."""
    
    def get_energy_level(self):
        """
        -Calculate dog's energy level based on age.
        - Younger dogs have higher energy levels, which is represented by base_energy.
        - age_factor shows how much the energy level changes with age.
        - The result is a value between 0 and 1.
        """
        base_energy = 0.8 
        age_factor = max(0, 1 - (self.age_months / (12 * 15)))
        return min(1.0, base_energy * (1 + 0.25 * age_factor))
    
    def get_social_level(self):
        """Dogs are typically very social."""
        return 0.9
    
    def get_noise_level(self):
        """Dogs can be quite noisy."""
        return 0.8

class Cat(Pet):
    """Class representing a cat."""
    
    def get_energy_level(self):
        """
        - Calculate cat's energy level based on age.
        - Younger cats have higher energy levels, which is represented by base_energy.
        - age_factor shows how much the energy level changes with age.
        - The result is a value between 0 and 1.
        """
        base_energy = 0.6
        age_factor = max(0, 1 - (self.age_months / (12 * 15)))
        return min(1.0, base_energy * (1 + 0.25 * age_factor))
    
    def get_social_level(self):
        """Cats are moderately social."""
        return 0.5
    
    def get_noise_level(self):
        """Cats are generally quieter than dogs."""
        return 0.4

class Rabbit(Pet):
    """Class representing a rabbit."""
    
    def get_energy_level(self):
        """
        - Calculate rabbit's energy level based on age.
        - age_factor shows how much the energy level changes with age.
        - The result is a value between 0 and 1.
        """
        age_factor = max(0, 1 - (self.age_months / (12 * 10)))
        return 0.4 * (1 + age_factor)
    
    def get_social_level(self):
        """Rabbits are less social than cats and dogs."""
        return 0.3
    
    def get_noise_level(self):
        """Rabbits are very quiet."""
        return 0.1

class Bird(Pet):
    """Class representing a bird."""
    
    def get_energy_level(self):
        """Calculate bird's energy level based on age."""
        age_factor = max(0, 1 - (self.age_months / (12 * 8)))
        return 0.5 * (1 + age_factor)
    
    def get_social_level(self):
        """Birds are moderately social."""
        return 0.6
    
    def get_noise_level(self):
        """Birds can be very noisy."""
        return 0.9

class PetFactory:
    """Factory class to create appropriate pet objects.
    ChatGPT helped with the creation of this class."""
    
    @staticmethod
    def create_pet(pet_data):
        """Create and return appropriate pet object based on type."""
        pet_type = pet_data['PetType']
        pet_classes = {
            'Dog': Dog,
            'Cat': Cat,
            'Rabbit': Rabbit,
            'Bird': Bird
        }
        if pet_type not in pet_classes:
            raise ValueError(f"Unknown pet type: {pet_type}")
        return pet_classes[pet_type](pet_data)

class PetMatcher:
    """Class for matching pets with users."""
    
    def __init__(self, csv_file):
        """Initialize PetMatcher with pets from CSV file."""
        self._pets = []
        self._weights = {
            'size_match': 0.25,
            'energy_match': 0.25,
            'social_match': 0.20,
            'noise_match': 0.15,
            'age_match': 0.15
        }
        
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                try:
                    pet = PetFactory.create_pet(row)
                    self._pets.append(pet)
                except ValueError as e:
                    print(f"Warning: {e}")
    
    @property
    def pets(self):
        """Returns list of pets."""
        return self._pets

    @property
    def weights(self):
        """Returns matching weights dictionary."""
        return self._weights
    
    def calculate_size_score(self, preference, pet_size):
        """Calculate size compatibility score."""
        size_map = {'Small': 3, 'Medium': 2, 'Large': 1}
        if pet_size not in size_map:
            return 0
        return 1 - abs(preference - size_map[pet_size]) / 2
    
    def calculate_match_score(self, user_info, pet):
        """
        - Calculate overall match score for a pet.
        - Convert user preferences to 0-1 scale (1: high/very active, 3: low/calm)
        - Calculate individual scores for size, energy, social, noise, and age
        - Calculate age preference based on time available (1: >4hrs -> young, 2: 2-4hrs -> adult, 3: <2hrs -> senior)
        - Calculate weighted score
        """
        user_energy = (4 - user_info['energy_level']) / 3
        user_social = (4 - user_info['social_preference']) / 3
        user_noise = (4 - user_info['noise_tolerance']) / 3
        
        size_score = self.calculate_size_score(user_info['size_preference'], pet.size)
        energy_score = 1 - abs(user_energy - pet.get_energy_level())
        social_score = 1 - abs(user_social - pet.get_social_level()) 
        noise_score = 1 - abs(user_noise - pet.get_noise_level())
        
        age_years = pet.age_months / 12
        pet_age_category = 1 if age_years < 2 else (2 if age_years < 8 else 3)
        age_score = 1 - abs(user_info['time_available'] - pet_age_category) / 2  

        total_score = (
            self._weights['size_match'] * size_score +
            self._weights['energy_match'] * energy_score +
            self._weights['social_match'] * social_score +
            self._weights['noise_match'] * noise_score +
            self._weights['age_match'] * age_score
        )
        
        return total_score
    
    def find_matches(self, user_info, top_n=3):
        """
        - Find top matching pets based on user preferences.
        - Calculate match score for each pet.
        - Sort by score in descending order.
        - Return top matches
        """
        matches = []
        for pet in self._pets:
            score = self.calculate_match_score(user_info, pet)
            matches.append((pet, score))
        
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches[:top_n]
