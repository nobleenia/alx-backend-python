#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test the access_nested_map function from the utils module.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the correct result.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError not raised by access_nested_map"),
        ({"a": 1}, ("a", "b"), "KeyError not raised by access_nested_map")
    ])
    def test_access_nested_map_exception(self, nested_map, path, msg):
        """
        Test that access_nested_map raises KeyError for invalid paths.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), msg)

class TestGetJson(unittest.TestCase):
    """Tests for the get_json function from the utils module."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that utils.get_json returns the expected result and
        that requests.get is called properly.
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value = Mock(json=Mock(return_value=test_payload))
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            mock_get.assert_called_once_with(test_url)

class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator from the utils module."""

    def test_memoize(self):
        """
        Test that the memoized property only calls the decorated method once.
        """

        class TestClass:
            def __init__(self):
                self.method_calls = 0

            def a_method(self):
                self.method_calls += 1
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked_method:
            instance = TestClass()
            self.assertEqual(instance.a_property, 42)  # Call property first time
            self.assertEqual(instance.a_property, 42)  # Call property second time

            mocked_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
