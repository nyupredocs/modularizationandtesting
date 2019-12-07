import unittest
import numpy as np
import iv_reg as iv

class TestBetas(unittest.TestCase):
    def test_square_instruments(self):
        z = np.random.rand(5, 5)
        x = np.random.rand(1, 20)
        y = np.random.rand(1, 20)
        betas = np.linalg.inv(np.transpose(z) @ x) @ np.transpose(z) @ y
        self.assertEqual(betas, iv.estimate_beta_iv(x, z, y, nocons = True))

if __name__ == "__main__":
    unittest.main()
