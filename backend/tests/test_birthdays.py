import os
import sys
from fastapi.testclient import TestClient


# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now you can do the relative import
from app.main import app

from app.mymodules.birthdays import return_birthday, print_birthdays_str

client = TestClient(app)

def test_smoke_valid_input():
    expected_output = 'Albert Einstein, Benjamin Franklin, Ada Lovelace, Donald Trump, Rowan Atkinson'
    assert print_birthdays_str() == expected_output

def test_error_entry():
    error_entry = "John Doe"
    expected_output = 'Sadly, we don\'t have John Doe\'s birthday.'
    assert return_birthday(error_entry) == expected_output