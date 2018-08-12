import unittest
from meza.core.vector2 import Vector2
import math


class Vector2TestCase(unittest.TestCase):

    def test_default_construction(self):
        v = Vector2()
        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 0)

    def test_construction(self):
        v = Vector2(3, 5)
        self.assertEqual(v.x, 3)
        self.assertEqual(v.y, 5)

    def test_str(self):
        self.assertEqual(
            str(Vector2(3, 5)), "(3, 5)"
        )

    def test_repr(self):
        self.assertEqual(
            repr(Vector2(3, 5)), "<Vector2 (3, 5)>"
        )

    def test_neg(self):
        self.assertEqual(-Vector2(2, 3), Vector2(-2, -3))

    def test_equal(self):
        self.assertEqual(
            Vector2(2, 3), Vector2(2, 3)
        )

    def test_add(self):
        self.assertEqual(
            Vector2(2, 3) + Vector2(2, 4),
            Vector2(4, 7)
        )

    def test_self_add(self):
        v = Vector2(2, 3)
        v += Vector2(1, 1)
        self.assertEqual(v, Vector2(3, 4))

    def test_substraction(self):
        self.assertEqual(
            Vector2(2, 3) - Vector2(2, 4),
            Vector2(0, -1)
        )

    def test_mul(self):
        self.assertEqual(
            Vector2(2, 3) * 2, Vector2(4, 6)
        )

    def test_rmul(self):
        self.assertEqual(
            2 * Vector2(2, 3), Vector2(4, 6)
        )

    def test_self_mul(self):
        v = Vector2(2, 3)
        v *= 2
        self.assertEqual(v, Vector2(4, 6))

    def test_truediv(self):
        self.assertEqual(
            Vector2(4, 6) / 2, Vector2(2, 3)
        )

    def test_self_div(self):
        v = Vector2(4, 6)
        v /= 2
        self.assertEqual(v, Vector2(2, 3))

    def test_mag(self):
        self.assertAlmostEqual(Vector2(3, 4).mag, 5)

    def test_angle_first_quarter(self):
        self.assertAlmostEqual(Vector2(1, math.sqrt(3)).angle, math.pi / 3)

    def test_angle_second_quarter(self):
        self.assertAlmostEqual(
            Vector2(-1, math.sqrt(3)).angle,
            math.pi - (math.pi / 3)
            )

    def test_angle_third_quarter(self):
        self.assertAlmostEqual(
            Vector2(-1, -math.sqrt(3)).angle,
            math.pi / 3 - math.pi
            )

    def test_angle_fourth_quarter(self):
        self.assertAlmostEqual(Vector2(1, -math.sqrt(3)).angle, -math.pi / 3)

    def test_angle_null_x(self):
        self.assertEqual(Vector2(0, 1).angle, math.pi)
        self.assertEqual(Vector2(0, -1).angle, -math.pi)

    def test_angle_null_vector(self):
        self.assertEqual(Vector2().angle, 0)

    def test_abs(self):
        self.assertEqual(abs(Vector2(2, 3)), Vector2(2, 3).mag)

    def test_iter(self):
        values = []
        for x in Vector2(2, 3):
            values.append(x)
        self.assertListEqual(values, [2, 3])

    def test_normalized(self):
        v = Vector2(2, 3)
        vn = Vector2(2, 3).normalized()
        self.assertEqual(vn.mag, 1)
        self.assertEqual(vn.angle, v.angle)

    def test_dot(self):
        self.assertEqual(
            Vector2(2, 3).dot(Vector2(1, 2)),
            8
        )

    def test_angle_between(self):
        self.assertAlmostEqual(
            Vector2(1, math.sqrt(3)).angle_between(Vector2(0, 1000)),
            math.pi / 6
        )
