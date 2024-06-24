"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    length = (width - 2*GRAPH_MARGIN_SIZE)//len(YEARS)
    return GRAPH_MARGIN_SIZE + length*year_index


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(0, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(0, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # canvas.create_line(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, width=LINE_WIDTH)

    # ----- Write your code below this line ----- #

    y_bottom = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

    for i in range(len(lookup_names)):
        value = name_data[lookup_names[i]]
        lst = []
        for j in range(len(YEARS)):
            year_str = str(YEARS[j])
            if year_str in value and int(value[year_str]) <= 1000:
                rth_y_coordinate = GRAPH_MARGIN_SIZE + int(value[year_str]) * (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE) // MAX_RANK
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX, rth_y_coordinate,
                                   text=lookup_names[i] + value[year_str],
                                   fill=COLORS[i % len(COLORS)],
                                   anchor=tkinter.SW)
                lst += [(get_x_coordinate(CANVAS_WIDTH, j), rth_y_coordinate)]
            else:  # there is no info in YEARS[j] or rank > 1000
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX, y_bottom,
                                   text=lookup_names[i] + '*',
                                   fill=COLORS[i % len(COLORS)],
                                   anchor=tkinter.SW)
                lst += [(get_x_coordinate(CANVAS_WIDTH, j), y_bottom)]
        lst = sorted(lst)
        for k in range(len(lst)-1):
            canvas.create_line(lst[k][0], lst[k][1], lst[k+1][0], lst[k+1][1], width=LINE_WIDTH, fill=COLORS[i % 4])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
