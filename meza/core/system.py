import datetime as d


class System:
    """Class to represent physical systems"""

    def __init__(self):
        """System constructor"""
        self.datetime = d.datetime.min
        self.bodies = []
        self.default_dt = 0.1
        self.external_forces = []

    def add_body(self, body):
        """Add a body into the system

        :param body: Body to be handled
        :type body: Body
        """
        self.bodies.append(body)

    def remove_body(self, body):
        """Remove a body from the system

        :param body: Body to be removed
        :type body: Body
        """
        self.bodies.remove(body)

    def step(self, dt = None):
        """Make a time step

        :param dt: Amount of time in seconds
        :type dt: float|int
        """
        if dt is None:
            dt = self.default_dt
        for body in self.bodies:
            for force in self.external_forces:
                body.add_force(force)
            body.integrate(dt)
        self.datetime += d.timedelta(seconds=dt)

    def add_external_force(self, force):
        """Add a external force into the system"""
        self.external_forces.append(force)
