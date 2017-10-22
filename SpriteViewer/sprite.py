import turtle

class Sprite:
    """Class to hold the data for a sprite"""

    def __init__(self, **kwargs):

        self._color_map = dict()
        self._color_map['B']='black'
        self._color_map[' ']='white'
        self._color_map['Y']='yellow'
        self._color_map['R']='red'
        self._color_map['O']='orange'
        return super().__init__(**kwargs)
    
    def load_from_file(self, file):

        """Read the content of a file into the sprite"""
        self._file = file


        self._lines = []

        with open(file, "rtU") as f:

            for textline in f:
                line = []
                # Now you have one line of text in the variable "line" and can
                # iterate over its characters like so:
                for ch in textline:
                    if ch != '\n':
                        line.append(self._color_map[ch])

                self._lines.append(line)


    def draw(self):
        """Draw the sprite"""
        print("Drawing sprite from " + self._file)

        self._draw_start()

        lineno = 0
        for line in self._lines:
            for pixel in line:
                self._draw_pixel(pixel)

            lineno = lineno + 1
            self._draw_start_of_line(lineno)

    def _draw_start_of_line(self, lineno):
        turtle.penup()
        turtle.home()
        turtle.right(90)
        turtle.forward(15*lineno)
        turtle.left(90)
        turtle.pendown()


    def _draw_start(self):
        turtle.speed(10)

    def _draw_pixel(self, pixel):
        if pixel == 'white':
            turtle.penup()
            turtle.forward(15)
            turtle.pendown()
        else:
            print("Drawing pixel " + pixel)
            turtle.pen(fillcolor=pixel, pencolor=pixel, pensize=0)
            turtle.begin_fill()
            turtle.forward(15)
            turtle.left(90)
            turtle.forward(15)
            turtle.left(90)
            turtle.forward(15)
            turtle.left(90)
            turtle.forward(15)
            turtle.left(90)
            turtle.end_fill()
            turtle.penup()
            turtle.forward(15)
            turtle.pendown()
