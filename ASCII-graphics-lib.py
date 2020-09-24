class Node():
    """A node."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'<Node data: {self.data} next: {self.next}>'


class LinkedList():
    """A linked list."""

    def __init__(self):

        self.head = None
        self.tail = None

    def append(self, shape):
        """Add shape to end of linked list."""

        new_node = Node(shape)

        # if an empty ll set head and tail as new node
        if self.head is None:
            self.head = new_node

        # if ll has at least one node, set new node as tail
        if self.tail is not None:
            self.tail.next = new_node
            self.tail = new_node

        self.tail = new_node

    def __repr__(self):
        return f'<DLL head: {self.head} tail: {self.tail}>'


class Canvas():
    """A canvas."""

    def __init__(self):
        """Create a 10 x 10 character canvas."""

        self.width = 10
        self.height = 10
        self.shapes = LinkedList()

    def render_canvas(self):
        """Print canvas and any shapes."""

        # create a 2d array, for number of rows we will print (which is the height)
        row = [' '] * self.width
        canvas = [row for i in range(self.height)]

        def each_shape_canvas(shape):
            """Recursive helper function to render shapes."""

            if shape is None:
                return

            # iterate through each row of canvas and change item with index of shape's dimensions to shape's fill char
            for row in range(len(canvas)):
                current_row = list(canvas[row])
                if row in shape.data.shape_len:
                    for column in range(len(current_row)):
                        if column in shape.data.shape_wid:
                            current_row[column] = shape.data.fill_char
                # update rows in canvas with shape's fill char
                canvas[row] = current_row

            # recursive call on next shape in ll
            each_shape_canvas(shape.next)

        # call helper function on first shape
        each_shape_canvas(self.shapes.head)

        # render completed canvas with all shapes overlapped
        for row in canvas:
            print(row)

    def add_shape(self, shape):
        """Add shape to a canvas, most recently added rectangles should appear on top."""

        self.shapes.append(shape)

    def clear_canvas(self):
        """Clear all shapes from a canvas."""

        self.shapes = LinkedList()

    def __repr__(self):
        return f'<Canvas>'


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

    def __repr__(self):
        return f'<Rectangle start: {self.start_x, self.start_y} end: {self.end_x, self.end_y}>'

    @property
    def shape_wid(self):
        """Return set of indices for shape's width."""

        self._shape_wid = set(list(range(self.start_x, self.end_x + 1)))

        return self._shape_wid

    @property
    def shape_len(self):
        """Return set of indices for shape's length."""

        self._shape_len = set(list(range(self.start_y, self.end_y + 1)))

        return self._shape_len

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


# ******** Functions to call to test when running file. *******

def plain_canvas(canvas):
    """Render plain canvas."""

    print('\nNew plain canvas')
    canvas.render_canvas()

def add_shapes_to_canvas(canvas, *shapes):
    """Adding rectangles to canvas."""

    print('\nAdding shapes to canvas')
    for shape in shapes:
        canvas.add_shape(shape)
    canvas.render_canvas()

def move_shape(canvas, shape):
    """Move a rectangle."""

    print('\nMove * rectangle to the right by 3')
    shape.translate('x',3)
    canvas.render_canvas()

def change_fill(canvas, rec1, rec2, rec3):
    """Change fill character for rectangle(s)."""

    print('\nChange fill characters')
    rec1.change_fill_char('$')
    rec2.change_fill_char('1')
    rec3.change_fill_char('#')
    canvas.render_canvas()

def clear_canvas(canvas):
    """Remove shapes from canvas."""

    print('\nRemove all shapes from canvas.')
    canvas.clear_canvas()


# *************************

if __name__ == '__main__':

    canvas = Canvas()
    rec1 = Rectangle(1,1,3,3,'@')
    rec2 = Rectangle(1,6,7,8, '0')
    rec3 = Rectangle(2,2,4,7, '*') 
    plain_canvas(canvas)
    add_shapes_to_canvas(canvas, rec1, rec2, rec3)
    move_shape(canvas, rec3)
    change_fill(canvas, rec1, rec2, rec3)
    clear_canvas(canvas)


