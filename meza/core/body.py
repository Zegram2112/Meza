from meza.core.vector2 import Vector2


class Body:
    """Solid body, main object of a physics simulation"""

    def __init__(self, mass=1, position=Vector2(), velocity=Vector2()):
        """Body constructor

        :param mass: Mass of the object in kg
        :type mass: int|float
        :param position: Position of body in a euclidean space
        :type position: Vector2
        :param velocity: Initial velocity of the body
        :type velocity: Vector2
        """
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = Vector2()

    def integrate(self, dt):
        """Updates velocity and position in a interval of time

        Calculation is done assuming that the current acceleration is constant
        (calculated implicitly from the forces applied). At the end of the
        integration, acceleration is set to 0, so constant forces should be
        added again after each iteration.

        :param dt: Amount of time
        :type dt: int|float

        .. warning:: Integration could be error prone if not executed with
            a tiny amount of time
        """
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

        self.acceleration = Vector2()

    def add_force(self, force):
        """Add a force to this body

        Adding a force to this body will change temporarily its acceleration.
        Forces should be added to this object before any integration, when that
        happens, acceleration is set to 0.

        :param force: Force applied to this body
        :type force: Vector2
        """
        self.acceleration += force / self.mass
