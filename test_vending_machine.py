import unittest
from vending_machine import give_change

class TestVendingMachine(unittest.TestCase):
    def test_return_change(self):
        self.assertEqual(give_change(.17), [.10, .05, .02])
        self.assertEqual(give_change(.18), [.10, .05, .02, .01])
    def test_multiple_same_coins(self):
        self.assertEqual(give_change(.04), [.02, .02])

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVendingMachine)
    unittest.TextTestRunner(verbosity=2).run(suite)
