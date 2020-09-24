class Node():
    """A node."""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DLinkedlist():
    """A linked list."""

    def __init__(self):

        self.head = None
        self.tail = None

    def append(self, shape):
        """Add shape to end of linked list."""

        new_node = Node(shape)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

        self.tail = new_node


class Canvas():
    """A canvas."""

    def __init__(self):
        """Create a 10 x 10 character canvas."""

        self.width = 10
        self.height = 10
        self.shapes = DLinkedlist()

    def render_canvas(self):
        """Print canvas and any shapes."""

        row = [0] * self.width
        top_shape = self.shapes.tail.data

        top_shape.shape

        for i in range(0, self.height):
            current_row = list(row)
            if i in shape_len:
                for j in range(0, self.width):
                    if j in shape_wid:
                        current_row[j] = top_shape.fill_char
            print(current_row)

    def render_plain_canvas(self):
        """Print plain canvas with no shapes."""
        row = [0] * self.width
        for i in range(0, self.height):
            print(row)

    def add_shape(self, shape):
        """Add shape to a canvas, most recently added rectangles should appear on top."""

        self.shapes.append(shape)

    def clear_canvas(self):
        """Clear all shapes from a canvas."""

        self.shapes = None


class Rectangle():
    """A rectangle."""

    def __init__(self, start_x=None, start_y=None, end_x=None, end_y=None, fill_char=None):
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
        # self.area = (self.end_x - self.start_x) * (self.start_y - self.end_y)

    @property
    def shape_len(self):

        self._shape_len = set(list(range(self.start_x, self.end_x + 1)))

        return self._shape_len

    @property
    def shape_wid(self):

        self._shape_wid = set(list(range(self.start_y, self.end_y + 1)))

        return self._shape_wid

    def change_fill_char(self, new_char):
        """Change rectangle's fill character."""

        self.fill_char = new_char

    def translate(self, axis, num):
        """Move rectangle left, right, up, or down."""

        if axis == 'x':
            self.start_x += num
            self.end_x += num
        if axis == 'y':
            self.start_y += num
            self.end_y += num



