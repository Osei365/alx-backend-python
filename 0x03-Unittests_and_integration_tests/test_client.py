#!/usr/bin/env python3
""" test client module."""


import unittest
from unittest.mock import patch, Mock, PropertyMock
import client
from client import GithubOrgClient
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
        instance = GithubOrgClient(org)
        instance.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{org}')

    def test_public_repos_url(self):
        """test public repo url."""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {'repos_url': 'REPO'}
            mock.return_value = payload
            instance = GithubOrgClient('testing')
            repo_url = instance._public_repos_url
            self.assertEqual(repo_url, payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """tests public repos."""

        payload = [{'name': 'the url'}, {'name': 'anotherone'}]
        mock_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock:
            mock.return_value = 'world'
            instance = GithubOrgClient('testing')
            result = instance.public_repos
            check = [item['name'] for item in payload]
            self.assertEqual(result, check)
            mock.assert_called_once()
            mock_json.assert_called_once()
