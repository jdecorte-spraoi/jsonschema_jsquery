"""
    Add common fixtures
"""
import json

import pytest


@pytest.fixture
def test_schema():
    """ Test schema dictionary """
    with open("tests/test_schema.json") as infile:
        schema_dict = json.load(infile)
    return schema_dict
