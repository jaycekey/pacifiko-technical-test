# To execute this test please install pytest using the following command in your terminal: "pip install pytest"
# then, execute "pytest" command to run the tests

import exercise_3

def test_valid_isbn():

    valid_isbn_list = [
        '0471958697',
        '0134685997',
        '080442957X',
        '0201633612',
        '0743273567',
        '059035342X',
        '1565926218',
        '0066620996'
    ]

    for isbn in valid_isbn_list:
        assert exercise_3.is_valid_ISBN10(isbn), f"ISBN {isbn} is not valid"

def test_invalid_isbn():

    invalid_isbn_list = [
        '0072855493',
        '0842359287',
    ]

    for isbn in invalid_isbn_list:
        assert not exercise_3.is_valid_ISBN10(isbn), f"ISBN {isbn} is valid, but it shouldn't be"

if __name__ == "__main__":
    test_valid_isbn()
    test_invalid_isbn()
