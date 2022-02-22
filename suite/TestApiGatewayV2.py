import unittest
import os
from parameterized import parameterized

import boto3

class TestApiGwV2(unittest.TestCase):
    def setUp(self) -> None:
        self.client = boto3.client('apigatewayv2', endpoint_url=os.getenv('ENDPOINT_URL'))

    @parameterized.expand([
        ["support-ui-login"],
    ])
    def test_api_has_integration(self, name):
        api = self._find_api_by_name(name)
        self.assertIsNotNone(api)
        integrations_obj = self.client.get_integrations(ApiId=api['ApiId'])
        integrations = integrations_obj['Items']
        self.assertEqual(1, len(integrations), 'We expect only one integration')
        integration = integrations[0]
        self.assertIsNotNone(integration['ResponseParameters'])

    def _find_api_by_name(self, name) -> object:
        apis = self.client.get_apis()
        api = None
        for temp_api in apis['Items']:
            if temp_api['Name'] == name:
                api = temp_api
        return api
