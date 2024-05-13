# 0x03. Unittests and Integration Tests

## test_utils.py:
- Understanding the utils.access_nested_map function an its purpose.
- Implement TestAccessNestedMap.test_access_nested_map_exception. Use the assertRaises context manager to test that a KeyError is raised for inputs
- Define the TestGetJson(unittest.TestCase) class and implement the TestGetJson.test_get_json method to test that utils.get_json returns the expected result
- Implement the TestMemoize(unittest.TestCase) class with a test_memoize method

## test_client.py:
- Declare the TestGithubOrgClient(unittest.TestCase) class and implement the test_org method
- Implement the test_public_repos_url method to unit-test GithubOrgClient._public_repos_url
- Implement TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos
- Implement TestGithubOrgClient.test_has_license to unit-test GithubOrgClient.has_license
- Create the TestIntegrationGithubOrgClient(unittest.TestCase) class and implement the setUpClass and tearDownClass which are part of the unittest.TestCase API