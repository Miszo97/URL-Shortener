from apps.urls.utils.generate_code import generate_code


def test_empty_string():
    assert len(generate_code("", size=4)) == 4


def test_sizes():
    assert len(generate_code("https://www.example.com", size=0)) == 0
    assert len(generate_code("https://www.example.com", size=7)) == 7
