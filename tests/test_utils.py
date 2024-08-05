import pytest

from solution.utils import parse_config_file, parse_text_file


@pytest.fixture
def create_temp_config_file(tmp_path):
    config_content = "a=z\nb=y\nc=x\n"
    config_file = tmp_path / "config.txt"
    config_file.write_text(config_content)
    return config_file


@pytest.fixture
def create_temp_simple_config_file(tmp_path):
    config_content = "a=z\n"
    config_file = tmp_path / "config.txt"
    config_file.write_text(config_content)
    return config_file


@pytest.fixture
def create_temp_text_file(tmp_path):
    text_content = "jgrebk6hnae\ncnhjrfyjvth3nxr\nb#sjcf_ansvo!\ndjf#aemfaaofna%"
    text_file = tmp_path / "text.txt"
    text_file.write_text(text_content)
    return text_file


@pytest.fixture
def create_temp_simple_text_file(tmp_path):
    text_content = "a\naaa\naa\n"
    text_file = tmp_path / "text.txt"
    text_file.write_text(text_content)
    return text_file


@pytest.mark.parametrize(
    "config_fixture, expected_replacements",
    [
        ("create_temp_config_file", {"a": "z", "b": "y", "c": "x"}),
        ("create_temp_simple_config_file", {"a": "z"}),
    ],
)
def test_parse_config_file(request, config_fixture, expected_replacements):
    config_file = request.getfixturevalue(config_fixture)
    replacements = parse_config_file(config_file)
    assert replacements == expected_replacements


@pytest.mark.parametrize(
    "text_fixture, replacements, expected_sorted_lines",
    [
        (
            "create_temp_text_file",
            {"a": "z", "b": "y", "c": "x"},
            ["djf#zemfzzofnz%", "y#sjxf_znsvo!", "jgreyk6hnze", "xnhjrfyjvth3nxr"],
        ),
        (
            "create_temp_simple_text_file",
            {"a": "z"},
            [
                "zzz",
                "zz",
                "z",
            ],
        ),
    ],
)
def test_parse_text_file(request, text_fixture, replacements, expected_sorted_lines):
    text_file = request.getfixturevalue(text_fixture)
    sorted_lines = parse_text_file(text_file, replacements)
    assert sorted_lines == expected_sorted_lines
