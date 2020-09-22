class Linkedlist():
    """A linked list."""

    def __init__(self):

        self.head = None
        self.tail = None


class Canvas():
    """A canvas."""

    def __init__(self):
        """Create a 10 x 10 character canvas."""
        self.width = 10
        self.height = 10
        self.shapes = Linkedlist()

    def render_canvas(self):
        """Print canvas and any shapes."""
        print(self)

    def add_shape(self, shape):
        """Add shape to a canvas."""

        self.shapes.append(shape)

    def clear_canvas(self):
        """Clear all shapes from a canvas."""

        self.shapes = None

class Rectangle():
    """A rectangle."""

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        """Create instance of rectangle's dimensions and character.

        start_x is the X coordinate of the upper-left-hand corner of the rectangle,
        start_y is the Y coordinate of the upper-left-hand corner of the rectangle,
        end_x is the X coordinate of the lower-right-hand corner of the rectangle,
        end_y is the Y coordinate of the lower-right-hand corner of the rectangle,
        fill_char is the character that should be used to draw the rectangle.
        """

        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char

    def change_fill_char(self, new_char):
        """Change rectangle's fill character."""

        self.fill_char = new_char


