import unittest
from meza import Body, Vector2, System


class SystemTestCase(unittest.TestCase):

    def setUp(self):
        self.system = System()

    def test_add_body(self):
        b = Body()
        self.system.add_body(b)
        self.assertIn(b, self.system.bodies)

    def test_remove_body(self):
        b = Body()
        self.system.add_body(b)
        self.system.remove_body(b)
        self.assertNotIn(b, self.system.bodies)

    def test_simple_step(self):
        b = Body(1, Vector2(), Vector2(0, 0))
        b.add_force(Vector2(1, 1))
        self.system.add_body(Body(1, Vector2(), Vector2(1, 1)))
        self.system.add_body(b)
        self.system.step(1)
        self.assertEqual(self.system.bodies[0].velocity,
                         self.system.bodies[1].velocity)

    def test_time_elapsed(self):
        self.assertEqual(self.system.datetime.microsecond, 0)
        self.system.step(0.1)
        self.system.step(0.001)
        self.system.step(0.010)
        self.assertEqual(self.system.datetime.microsecond, 111000)

    def test_default_dt_step(self):
        self.system.default_dt = 0.001
        self.system.step()
        self.assertEqual(self.system.datetime.microsecond, 1000)
