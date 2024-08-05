import pytest
import os

from solution.utils import parse_config_file, parse_text_file

@pytest.fixture
def create_temp_config_file(tmp_path):
    config_content = "a=z\nb=y\nc=x\n"
    config_file = tmp_path / "config.txt"
    config_file.write_text(config_content)
    return config_file

def test_parse_config_file(create_temp_config_file):
    replacements = parse_config_file(create_temp_config_file)
    assert replacements == {'a': 'z', 'b': 'y', 'c': 'x'}

@pytest.fixture
def create_temp_text_file(tmp_path):
    text_content = "jgrebk6hnae\ncnhjrfyjvth3nxr\nb#sjcf_ansvo!\ndjf#aemfaaofna%"
    text_file = tmp_path / "text.txt"
    text_file.write_text(text_content)
    return text_file

def test_parse_text_file(create_temp_text_file):
    replacements = {'a': 'z', 'b': 'y', 'c': 'x'}
    sorted_lines = parse_text_file(create_temp_text_file, replacements)
    assert sorted_lines == [
        'djf#zemfzzofnz%', 
        'y#sjxf_znsvo!', 
        'jgreyk6hnze', 
        'xnhjrfyjvth3nxr'
    ]

@pytest.fixture
def create_temp_simple_config_file(tmp_path):
    config_content = "a=z\n"
    config_file = tmp_path / "config.txt"
    config_file.write_text(config_content)
    return config_file

def test_simple_parse_config_file(create_temp_simple_config_file):
    replacements = parse_config_file(create_temp_simple_config_file)
    assert replacements == {'a': 'z'}

@pytest.fixture
def create_temp_simple_text_file(tmp_path):
    text_content = "a\naaa\naa\n"
    text_file = tmp_path / "text.txt"
    text_file.write_text(text_content)
    return text_file

def test_simple_parse_text_file(create_temp_simple_text_file):
    replacements = {'a': 'z'}
    sorted_lines = parse_text_file(create_temp_simple_text_file, replacements)
    assert sorted_lines == [
        'zzz', 
        'zz', 
        'z', 
    ]    