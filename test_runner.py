import unittest
import suite.TestS3 as s3
import suite.TestApiGatewayV2 as apiGwV2

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(apiGwV2))
suite.addTests(loader.loadTestsFromModule(s3))
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
