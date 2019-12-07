import unittest
import numpy as np
from iv_jett import iv_init

class TestBetas(unittest.TestCase):
    def test_square_instruments(self):
        z = np.random.rand(255, 5)
        x = np.random.rand(255, 5)
        y = np.random.rand(255, 5)

        betas = np.linalg.inv(np.transpose(z) @ x) @ np.transpose(z) @ y
        x2 = iv_init.estimate_beta_iv(x, z, y, nocons = True)

        self.assertIsNone(np.testing.assert_allclose(betas, x2))

if __name__ == "__main__":
    unittest.main()
