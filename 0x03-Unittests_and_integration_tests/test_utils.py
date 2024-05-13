#!/usr/bin/env python3
""" Parameterized unittest. """
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing Nested Map function """
    # unittest does not support test decorators,
    # only tests created with @parameterized.expand will be executed
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """ Test method returns correct output """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ Test method raises correct exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(unittest.TestCase):
    """ Class for testing get_json function """
    # order of args: test_url, test_payload
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test method returns correct output """
        # create Mock object with json method that returns test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        # function calls requests.get, need patch to get mock return value
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            # check that mocked method called once per input
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ Class for testing memoization """

    def test_memoize(self):
        """ Tests memoize function """

        class TestClass:
            """ Test class """

            def a_method(self):
                """ Method to always return 42 """
                return 42

            @memoize
            def a_property(self):
                """ Returns memoized property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.asset_called_once()
