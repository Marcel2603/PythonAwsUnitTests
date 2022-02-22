import unittest
import os

import boto3
from parameterized import parameterized

from .config import Config


class TestS3(unittest.TestCase):
    buckets = Config().buckets

    def setUp(self) -> None:
        self.s3 = boto3.resource('s3', endpoint_url=os.getenv('ENDPOINT_URL'))

    @parameterized.expand(buckets)
    def test_bucket_exists(self, name) -> None:
        """
        Tests if buckets exists
        """

        bucket = self.s3.Bucket(name)

        self.assertTrue(bucket.creation_date, f'Bucket {name} does not exists')
