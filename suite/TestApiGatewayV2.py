import unittest

import boto3


class TestApiGwV2(unittest.TestCase):
    def setUp(self) -> None:
        self.client = boto3.resource('apigatewayv2', endpoint_url='http://localhost:4566')

    def test_api_has_integration(self):
        self.client.get_integrations(ApiId='testId')
