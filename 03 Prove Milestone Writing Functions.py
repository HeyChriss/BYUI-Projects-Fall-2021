import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500
    

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}" )

    # Create a Frame object.
    frame = tk.Frame(root )
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1 )
    

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1 )

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    tree_center = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    draw_grass(canvas)
    draw_sun(canvas, 60, 20)
    draw_river(canvas)
    draw_cloud1(canvas, 380, 75) 
    draw_cloud2(canvas, 400, 20)
    draw_cloud3(canvas, 330, 20)
    draw_fence(canvas)
    draw_cloud4(canvas, 580, 75) 
    draw_cloud5(canvas, 600, 20)
    draw_cloud6(canvas, 530, 20)

    
    
    


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.



def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")


def draw_grass(canvas):
    canvas.create_rectangle(0, 250, 799, 799, fill = "greenYellow")

def draw_sun(canvas, x, y): 
    canvas.create_oval(x, y, x + 200, y + 200, fill="yellow")

def draw_cloud1(canvas, x, y): 
    canvas.create_oval(x, y, x + 100, y + 100, fill="honeydew4", width=0)
def draw_cloud2(canvas, x, y): 
    canvas.create_oval(x, y, x + 100, y + 100, fill="honeydew4", width=0)
def draw_cloud3(canvas, x, y): 
    canvas.create_oval(x, y, x + 100, y + 100, fill="honeydew4", width=0)
def draw_river(canvas):
    canvas.create_rectangle(0, 350, 799, 400, fill="skyBlue")
def draw_fence(canvas):
    canvas.create_rectangle(0, 325, 50, 175, fill = "lavender")
    canvas.create_rectangle(50, 325, 100, 175, fill = "lavender")
    canvas.create_rectangle(100, 325, 150, 175, fill = "lavender")
    canvas.create_rectangle(150, 325, 200, 175, fill = "lavender")
    canvas.create_rectangle(200, 325, 250, 175, fill = "lavender")
    canvas.create_rectangle(250, 325, 300, 175, fill = "lavender")
    canvas.create_rectangle(300, 325, 350, 175, fill = "lavender")
    canvas.create_rectangle(350, 325, 400, 175, fill = "lavender")
    canvas.create_rectangle(400, 325, 450, 175, fill = "lavender")
    canvas.create_rectangle(550, 325, 600, 175, fill = "lavender")
    canvas.create_rectangle(600, 325, 650, 175, fill = "lavender")
    canvas.create_rectangle(650, 325, 700, 175, fill = "lavender")
    canvas.create_rectangle(700, 325, 750, 175, fill = "lavender")
    canvas.create_rectangle(750, 325, 800, 175, fill = "lavender")
def draw_cloud4(canvas, x, y): 
    canvas.create_oval(x, y, x + 100, y + 100, fill="honeydew4", width=0)
def draw_cloud5(canvas, x, y): 
    canvas.create_oval(x, y, x + 100, y + 100, fill="honeydew4", width=0)
def draw_cloud6(canvas, x, y): 
    canvas.create_oval(x, y, x + 100, y + 100, fill="honeydew4", width=0)



    




# Call the main function so that greenYellow
# this program will start executing.
main()