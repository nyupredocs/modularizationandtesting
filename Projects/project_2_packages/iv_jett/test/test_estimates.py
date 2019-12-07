import unittest
import numpy as np
from iv_jett import iv_init

class TestBetas(unittest.TestCase):
    def test_square_instruments(self):
        z = np.random.rand(1, 5)
        x = np.random.rand(1, 5)
        y = np.random.rand(1, 5)
        betas = np.linalg.inv(np.transpose(z) @ x) @ np.transpose(z) @ y
        self.assertTrue(np.testing.assert_array_equal(betas, iv_init.estimate_beta_iv(x, z, y, nocons = True)))

if __name__ == "__main__":
    unittest.main()
