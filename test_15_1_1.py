import unittest
import json
import os


def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f)
    except TypeError as err:
        raise err
    except IOError as err:
        raise err


def read_from_file(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError as err:
        raise err
    except IOError as err:
        raise err


test_data = {
    "pk": 4,
    "title": "Test Title",
    "author": "Test Author",
    "published_date": "2024-06-23",
    "publisher": 6,
    "price": 9.99,
    "discounted_price": 3.56,
    "is_bestseller": True,
    "is_banned": False,
    "genres": [1, 3, 5]
}


class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_file.json'
        self.test_data = test_data
        self.empty_data = {}
        self.bad_data = [write_to_file, read_from_file]

    def test_write_and_read_file(self):
        write_to_file(self.test_file, self.test_data)
        result = read_from_file(self.test_file)
        self.assertEqual(result, self.test_data)
        for key, value in self.test_data.items():
            self.assertEqual(type(result[key]), type(value))

    def test_write_and_read_empty_file(self):
        write_to_file(self.test_file, self.empty_data)
        result = read_from_file(self.test_file)
        self.assertEqual(result, self.empty_data)

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file('filenotfounderror.json')

    def test_write_bad_data_into_file(self):
        for bad_data in self.bad_data:
            with self.assertRaises(TypeError):
                write_to_file(self.test_file, bad_data)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == '__main__':
    unittest.main()
