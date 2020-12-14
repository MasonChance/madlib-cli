import pytest
from madlib_cli.madlib import read_template, parse_template, get_stripped_template, get_parts, merge


def test_read_template_returns_stripped_string():
    actual = read_template("assets/small_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

def test_get_stripped_template():
    actual = get_stripped_template(read_template("assets/small_template.txt"))
    expected = 'It was a {} and {} {}.'
    assert actual == expected

def test_get_parts():
    actual = get_parts(read_template("assets/small_template.txt"))
    expected = ('Adjective', 'Adjective', 'Noun')
    assert actual == expected




def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


# def test_read_template_raises_exception_with_bad_path():

#     with pytest.raises(FileNotFoundError):
#         path = "missing.txt"
#         read_template(path)

