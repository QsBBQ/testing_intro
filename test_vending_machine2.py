import unittest
from vending_machine2 import give_change, give_item_and_change

class TestVendingMachine(unittest.TestCase):
    def test_return_change(self):
        self.assertEqual(give_change(.17), [.10, .05, .02])
        self.assertEqual(give_change(.18), [.10, .05, .02, .01])
        self.assertEqual(give_change(.04), [.02, .02])

    def test_give_item_and_change(self):
        item, change, _ = give_item_and_change('coke', "1.0")
        self.assertEqual(item, 'coke')
        self.assertEqual(change, [.20, .05, .02])
        item, change, _ = give_item_and_change('biscuits', "1.5")
        self.assertEqual(item, 'biscuits')
        self.assertEqual(change, [.20, .10, .05])
        item, change, _ = give_item_and_change('apple', ".65")
        self.assertEqual(item, 'apple')
        self.assertEqual(change, [.20, .02])
        item, change, _ = give_item_and_change('apple', ".65 1.0")
        self.assertEqual(item, 'apple')
        self.assertEqual(change, [1.0, .20, .02])

    def test_unavailable_item(self):
        """if user asks for an item that's unavailable, they should not be given the item, and their money should be returned"""
        item, change, _ = give_item_and_change('crisps', .50)
        self.assertIsNone(item)
        self.assertEqual(change, None)

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVendingMachine)
    unittest.TextTestRunner(verbosity=2).run(suite)
