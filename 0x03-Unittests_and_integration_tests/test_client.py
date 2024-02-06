#!/usr/bin/env python3
""" test client module."""


import unittest
from unittest.mock import patch, Mock
import client
from parameterized import parameterized
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """test github org client."""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mock: Mock) -> None:
        """testing the org method."""
        instance = client.GithubOrgClient(org)
        instance.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{org}')
