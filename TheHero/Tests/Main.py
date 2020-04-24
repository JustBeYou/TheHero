import unittest
from . import Stats
from . import Creature

loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(Stats))
suite.addTests(loader.loadTestsFromModule(Creature))

runner = unittest.TextTestRunner(verbosity = 3)
result = runner.run(suite)
