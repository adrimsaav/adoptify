"""
Contains tests for the pet matcher application using pytest.
"""
import pytest
from pet_matcher import Pet, Dog, Cat, PetMatcher
import os

@pytest.fixture
def pet_data():
    """Create sample pet data for testing."""
    return {
        'PetID': '500',
        'PetType': 'Dog',
        'Breed': 'Labrador',
        'Gender': 'M',
        'AgeMonths': '24',
        'Color': 'Black',
        'Size': 'Large',
        'TimeInShelterDays': '30',
        'AdoptionFee': '200',
        'AdoptionLikelihood': '0.8'
    }

@pytest.fixture
def matcher_setup():
    """Fixture that provides a PetMatcher instance with the actual CSV data."""
    csv_path = os.path.join(os.path.dirname(__file__), 'pet_adoption_data.csv')
    return PetMatcher(csv_path)

def test_pet_initialization(pet_data):
    """Test if a pet is initialized with correct attributes."""
    dog = Dog(pet_data)
    assert dog.id == '500'
    assert dog.type == 'Dog'
    assert dog.breed == 'Labrador'
    assert dog.size == 'Large'

def test_energy_and_social_levels(pet_data):
    """
    - Initialize dog
    - Modify data for cat
    - Test energy levels
    - Test social levels
    """
    dog = Dog(pet_data)
    
    pet_data['PetID'] = '501'
    pet_data['PetType'] = 'Cat'
    cat = Cat(pet_data)
    
    assert 0 <= dog.get_energy_level() <= 1
    assert 0 <= cat.get_energy_level() <= 1
    
    assert 0 <= dog.get_social_level() <= 1
    assert 0 <= cat.get_social_level() <= 1

def test_match_calculation(matcher_setup):
    """
    - Test if match calculations work correctly.
    - Test finding matches.
    """
    user_preferences = {
        'energy_level': 2,
        'social_preference': 2,
        'noise_tolerance': 2,
        'size_preference': 2,
        'time_available': 2
    }
    
    matches = matcher_setup.find_matches(user_preferences)
    assert len(matches) <= 3 
    
    if matches:
        assert 0 <= matches[0][1] <= 1 
