# MetaLearnAI test_utils.py

import unittest
import numpy as np
from metalearnai.utils import load_data, preprocess_data, split_data

class TestUtils(unittest.TestCase):
    def test_split_data(self):
        data = np.array([i for i in range(10)])
        train, test = split_data(data, train_size=0.8)
        self.assertEqual(len(train), 8)
        self.assertEqual(len(test), 2)

if __name__ == "__main__":
    unittest.main()
