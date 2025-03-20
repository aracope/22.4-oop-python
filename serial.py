"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Make a new generator with starting number."""

        self.start = start
        self.next = start

    def generate(self):
        """Returns next serial number, increments counter."""
        serial = self.next
        self.next += 1
        return serial

    def reset(self):
        """Reset number to original start value."""

        self.next = self.start

    def __repr__(self):
        """Shows string representation of object."""

        return f"<SerialGenerator start={self.start} next={self.next}>"
