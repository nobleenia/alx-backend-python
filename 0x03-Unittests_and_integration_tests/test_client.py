#!/usr/bin/env python3
import unittest
from unittest.mock import PropertyMock, patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import requests

from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value
        and that get_json is called once with the expected URL.
        """
        json_payload = {'name': org_name}
        mock_get_json.return_value = json_payload
        github_client = GithubOrgClient(org_name)
        expected_url = f"https://api.github.com/orgs/{org_name}"

        self.assertEqual(github_client.org, json_payload)
        mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self):
        """
        Test that GithubOrgClient._public_repos_url
        returns the expected URL.
        """
        mock_org_payload = {
            'repos_url': 'https://api.github.com/orgs/google/repos'
        }
        org_name = 'google'
        with patch.object(
                GithubOrgClient,
                'org',
                new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = mock_org_payload
            client = GithubOrgClient(org_name)
            self.assertEqual(
                client._public_repos_url,
                mock_org_payload['repos_url'])

    @patch('client.GithubOrgClient.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the expected list of repositories."""
        # Setup the mock return values
        mock_repos_url = 'https://api.github.com/orgs/test-org/repos'
        mock_repo_data = [{'name': 'repo1'}, {'name': 'repo2'}]
        mock_get_json.return_value = mock_repo_data

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = mock_repos_url
            client = GithubOrgClient('test-org')
            repos = client.public_repos

            # Check that the return value is as expected
            self.assertEqual(repos, ['repo1', 'repo2'])
            # Check that the get_json was called once with the correct URL
            mock_get_json.assert_called_once_with(mock_repos_url)
            # Check that _public_repos_url was accessed exactly once
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that has_license method returns True if the license key matches, False otherwise.
        """
        client = GithubOrgClient('test-org')  # Example org, not used in the test directly
        
        # Directly call the has_license method with the repo dictionary
        result = client.has_license(repo, license_key)
        
        # Assert that the result matches the expected output
        self.assertEqual(result, expected)

@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [
    (org_payload, repos_payload, expected_repos, apache2_repos)
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the `GithubOrgClient.public_repos` method."""

    @classmethod
    def setUpClass(cls):
        """Setup the class by starting the patcher."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if 'orgs/google' in url:
                return Mock(json=Mock(return_value=cls.org_payload))
            elif 'orgs/google/repos' in url:
                return Mock(json=Mock(return_value=cls.repos_payload))
            raise ValueError("Unhandled URL")

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method for correct data retrieval."""
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos, self.expected_repos)

@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [
    (org_payload, repos_payload, expected_repos, apache2_repos)
])
class TestGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if 'orgs/test-org/repos' in url:
                return Mock(json=Mock(return_value=cls.repos_payload))
            return Mock(json=Mock(return_value=cls.org_payload))
        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient('test-org')
        self.assertEqual(client.public_repos, self.expected_repos)

    def test_public_repos_with_license(self):
        client = GithubOrgClient('test-org')
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
