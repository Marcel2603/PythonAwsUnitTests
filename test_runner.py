import unittest
import suite.TestS3 as s3

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(s3))
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
print(result)
