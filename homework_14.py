def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle given its length and width.

    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: The area of the rectangle.
    """
    return length * width


if __name__ == "__main__":
    import unittest


    class TestUtilityFunctions(unittest.TestCase):
        def test_calculate_rectangle_area(self):
            self.assertEqual(calculate_rectangle_area(5, 10), 50)
            self.assertEqual(calculate_rectangle_area(0, 10), 0)
            self.assertAlmostEqual(calculate_rectangle_area(3.5, 2.1), 7.35, places=2)


    unittest.main()
