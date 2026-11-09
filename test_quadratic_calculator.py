import unittest

from quadratic_calculator import solve_quadratic


class SolveQuadraticTests(unittest.TestCase):
    def test_two_real_roots(self):
        self.assertEqual(solve_quadratic(1, -5, 6), (3 + 0j, 2 + 0j))

    def test_repeated_root(self):
        self.assertEqual(solve_quadratic(1, 2, 1), (-1 + 0j, -1 + 0j))

    def test_complex_roots(self):
        first, second = solve_quadratic(1, 0, 1)
        self.assertEqual(first, 1j)
        self.assertEqual(second, -1j)

    def test_zero_a_is_rejected(self):
        with self.assertRaises(ValueError):
            solve_quadratic(0, 2, 1)


if __name__ == "__main__":
    unittest.main()
