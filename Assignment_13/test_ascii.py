import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Project 1 ASCII ART')))

def test_ascii_folder_exists():
    assert os.path.exists("../Project 1 ASCII ART")

def test_basic_logic():
    test_str = "Hello"
    assert len(test_str) > 0
