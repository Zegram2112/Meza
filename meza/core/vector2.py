import math


class Vector2:
    """Class to represent 2d vectors"""

    def __init__(self, x=0, y=0):
        """Class constructor, accepts x and y coordinates"""
        self.x = x
        self.y = y

    # Unary operators

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "<Vector2 " + str(self) + ">"

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __abs__(self):
        return self.mag

    def __iter__(self):
        return iter((self.x, self.y))

    # Binary operators

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __rmul__(self, other):
        return Vector2(other * self.x, other * self.y)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)

    # Properties

    @property
    def mag(self):
        """Vector magnitude

        :getter: Return this vector's magnitude
        :type: int|float
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def angle(self):
        """Angle of this vector in radians

        Angle described by this property is included in the
        :math:`(-\pi, \pi]` range. It is positive if `y` coordinate is positive, and
        vice versa.

        :getter: Return this vector's angle
        :type: int|float

        .. note::
            This property returns 0 if evaluated in a null vector
        """
        if self.x > 0:
            return math.atan(self.y / self.x)
        elif self.x < 0:
            if self.y >= 0:
                return math.atan(self.y / self.x) + math.pi
            else:
                return - math.pi + math.atan(self.y / self.x)
        else:
            if self.y > 0:
                return math.pi
            elif self.y < 0:
                return -math.pi
            else:
                return 0

    # Methods

    def normalized(self):
        """Return a normalized vector from this one.

        :returns: :class:`Vector2` -- normalized vector of magnitude 1
        """
        mag = self.mag
        return Vector2(self.x / mag, self.y / mag)

    def dot(self, other):
        """Return the dot product between this and other vector

        :param other: Another vector
        :type other: Vector2
        :returns: float -- dot product between the two vectors
        """
        return self.x * other.x + self.y * other.y

    def angle_between(self, other):
        """Return the minor angle between this and other vector

        :param other: Another vector
        :type other: Vector2
        :returns: float -- angle between the two vectors
        """
        return math.acos(self.dot(other) / (self.mag * other.mag))
