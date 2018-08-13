import unittest
from meza import Body
from meza import Vector2


class BodyTestCase(unittest.TestCase):

    def test_construction(self):
        b = Body(1, Vector2(1, 2), Vector2(1, 1))
        self.assertEqual(b.mass, 1)
        self.assertEqual(b.position, Vector2(1, 2))
        self.assertEqual(b.velocity, Vector2(1, 1))
        self.assertEqual(b.acceleration, Vector2())

    def test_default_construction(self):
        b = Body()
        self.assertEqual(b.mass, 1)
        self.assertEqual(b.position, Vector2())
        self.assertEqual(b.velocity, Vector2())
        self.assertEqual(b.acceleration, Vector2())

    def test_apply_force(self):
        b = Body(2)
        b.add_force(Vector2(3, 4))
        self.assertEqual(b.acceleration.mag, 5 / 2)

    def test_integrate(self):
        b = Body(2, Vector2(0, 0), Vector2(0, -1))
        b.add_force(Vector2(0, 2))
        b.integrate(0.1)
        self.assertAlmostEqual(b.position, Vector2(0, -0.09))
