import unittest

import boto3


class TestS3(unittest.TestCase):
    def setUp(self) -> None:
        self.s3 = boto3.resource('s3', endpoint_url='http://localhost:4566')

    def test_bucket_exists(self) -> None:
        """
        Tests if buckets exists
        """
        bucket_name = 'test-bucket'
        bucket = self.s3.Bucket(bucket_name)

        self.assertTrue(bucket.creation_date, f'Bucket {bucket_name} does not exists')
