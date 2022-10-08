from django.test import TestCase
from django.urls import reverse
import pytest
from users.models import Instructor

# Create your tests here.
def test_homepage_access():
    url = reverse('home')
    assert url == "/"

@pytest.fixture
def new_instructor(db):
    instructor = Instructor.objects.create(
        first_name='Pytest',
        last_name='last_name',
        credentials='degree',
    )
    return instructor

def test_search_instructors(new_instructor):
    assert Instructor.objects.filter(first_name='Pytest').exists()

def test_update_instructor(new_instructor):
    new_instructor.first_name = 'Pytest-Django'
    new_instructor.save()
    assert Instructor.objects.filter(first_name='Pytest-Django').exists() 
