#!/usr/bin/env python3
""" module test-utils.py"""

import utils
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """test access nested map."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)
