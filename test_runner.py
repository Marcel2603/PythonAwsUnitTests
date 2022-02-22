import sys
import unittest

import suite.TestS3 as s3

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(s3))
runner = unittest.TextTestRunner(verbosity=1)
result = runner.run(suite)
sys.exit(not result.wasSuccessful())
