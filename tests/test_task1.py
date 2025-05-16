import unittest
from task1.solution import sum_two, strict


class TestStrictDecorator(unittest.TestCase):
    def test_sum_two_correct(self):
        self.assertEqual(sum_two(2, 3), 5)

    def test_sum_two_type_error(self):
        with self.assertRaises(TypeError):
            sum_two(2, 2.5)

    def test_custom_function(self):
        @strict
        def concat(a: str, b: str) -> str:
            return a + b

        self.assertEqual(concat("foo", "bar"), "foobar")
        with self.assertRaises(TypeError):
            concat("foo", 1)


if __name__ == '__main__':
    unittest.main()
