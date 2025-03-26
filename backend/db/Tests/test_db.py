import sys
import os

# Ensure test can import from 'db' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from connection import execute_query

def test_user_retrieval():
    result = execute_query(
        "SELECT email FROM users WHERE email=%s",
        ('abdessamad@example.com',)
    )
    assert result[0][0] == 'abdessamad@example.com'
