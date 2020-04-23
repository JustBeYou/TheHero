import unittest
from . import Stats

loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(Stats))

runner = unittest.TextTestRunner(verbosity = 3)
result = runner.run(suite)
