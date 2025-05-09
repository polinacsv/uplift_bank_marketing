# tests/test_data.py


import unittest
import os
from uplift_bank_marketing.data.load_data import load_data

class TestDataLoading(unittest.TestCase):

    def test_data_loading(self):
        # Test that the data loading function works properly.
        X, y = load_data()
        self.assertIsNotNone(X)
        self.assertIsNotNone(y)
        self.assertGreater(X.shape[0], 0)
        self.assertGreater(y.shape[0], 0)
        print("Data loading test passed.")

    def test_data_saved(self):
        # Test that the data is saved properly.
        data_dir = "src/uplift_bank_marketing/data"
        X_path = os.path.join(data_dir, "X_bank_marketing.csv")
        y_path = os.path.join(data_dir, "y_bank_marketing.csv")

        self.assertTrue(os.path.exists(X_path))
        self.assertTrue(os.path.exists(y_path))
        print("Data saved test passed.")

if __name__ == "__main__":
    unittest.main()
