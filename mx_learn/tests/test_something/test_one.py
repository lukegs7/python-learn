"""
    this is a test
"""

import json
import pytest
import os


@pytest.mark.run_json
def test_one():
    with open('tests/data/data.json', 'r') as f:
        data = json.load(f)
    assert data == {'name': 'geshuai', 'age': 12}

@pytest.mark.env
def test_env():
    assert os.environ.get('CURRENT_USER', '') == 'Luke G'
