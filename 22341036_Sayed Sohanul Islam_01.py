from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Global variables
num_raindrops = 100
raindrops = [[random.uniform(0, 500), random.uniform(0, 500)] for _ in range(num_raindrops)]
rain_vx = 0.0  # Here Sir, I am setting horizontal velocity for rain direction
rain_vy = -5.0  # Here Sir, I am setting vertical velocity (falling)
bg_color = 0.5  # Here Sir, I am setting background color (grayscale, 0 to 1)

def draw_raindrop(x, y, length=5):
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x, y - length)
    glEnd()

def draw_tree(x, y, height, width):
    glColor3f(0.0, 0.6, 0.0)  # Dark green for trees
    glBegin(GL_TRIANGLES)
    glVertex2f(x - width / 2, y)
    glVertex2f(x + width / 2, y)
    glVertex2f(x, y + height)
    glEnd()

def draw_house():
    # Here Sir, I am drawing house base (rectangle) with GL_TRIANGLES, full white
    glColor3f(1.0, 1.0, 1.0)  # White for house base
    glBegin(GL_TRIANGLES)
    glVertex2f(200, 150)  # Bottom-left
    glVertex2f(300, 150)  # Bottom-right
    glVertex2f(200, 250)  # Top-left
    glVertex2f(300, 150)  # Bottom-right
    glVertex2f(300, 250)  # Top-right
    glVertex2f(200, 250)  # Top-left
    glEnd()

    # Here Sir, I am drawing roof (triangle) with GL_TRIANGLES, full violet
    glColor3f(0.5, 0.0, 0.5)  # Violet for roof
    glBegin(GL_TRIANGLES)
    glVertex2f(200, 250)
    glVertex2f(300, 250)
    glVertex2f(250, 300)
    glEnd()

    # Here Sir, I am darwing door (rectangle) with GL_TRIANGLES, full green
    glColor3f(0.0, 1.0, 0.0)  # Green for door
    glBegin(GL_TRIANGLES)
    glVertex2f(235, 150)
    glVertex2f(265, 150)
    glVertex2f(235, 190)
    glVertex2f(265, 150)
    glVertex2f(265, 190)
    glVertex2f(235, 190)
    glEnd()

    # Here Sir, I am putting first window (leftmost) (rectangle) with GL_TRIANGLES, full blue
    glColor3f(0.0, 0.0, 1.0)  # Blue for window
    glBegin(GL_TRIANGLES)
    glVertex2f(205, 200)  # Leftmost edge
    glVertex2f(225, 200)
    glVertex2f(205, 230)
    glVertex2f(225, 200)
    glVertex2f(225, 230)
    glVertex2f(205, 230)
    glEnd()
    # Here Sir, I am using horizontal lines inside first window with GL_LINES, black border
    glColor3f(0.0, 0.0, 0.0)  # Black
    glBegin(GL_LINES)
    glVertex2f(205, 210)
    glVertex2f(225, 210)
    glVertex2f(205, 220)
    glVertex2f(225, 220)
    glEnd()

    # Here Sir, I am putting second window (rightmost) (rectangle) with GL_TRIANGLES, full blue
    glColor3f(0.0, 0.0, 1.0)  # Blue for window
    glBegin(GL_TRIANGLES)
    glVertex2f(275, 200)  # Rightmost edge
    glVertex2f(295, 200)
    glVertex2f(275, 230)
    glVertex2f(295, 200)
    glVertex2f(295, 230)
    glVertex2f(275, 230)
    glEnd()
    # Here Sir, I am trying to get horizontal lines inside second window with GL_LINES, black border
    glColor3f(0.0, 0.0, 0.0)  # Black
    glBegin(GL_LINES)
    glVertex2f(275, 210)
    glVertex2f(295, 210)
    glVertex2f(275, 220)
    glVertex2f(295, 220)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # Here Sir, I am setting background color (grayscale for day/night)
    glClearColor(bg_color, bg_color, bg_color, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    # Here Sir, I am drawing ground (soil color) with GL_TRIANGLES
    glColor3f(0.4, 0.2, 0.1)  #Here Sir, I am putting brown soil color
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(500, 0)
    glVertex2f(0, 150)
    glVertex2f(500, 0)
    glVertex2f(500, 150)
    glVertex2f(0, 150)
    glEnd()

    # Here Sir, I am trying to draw trees behind the house, two on each side
    # Left side trees
    draw_tree(100, 150, 50, 30)  # First tree on left
    draw_tree(150, 150, 50, 30)  # Second tree on left
    # Right side trees
    draw_tree(350, 150, 50, 30)  # First tree on right
    draw_tree(400, 150, 50, 30)  # Second tree on right

    # Here Sir, I am drawing house
    draw_house()

    #Here Sir, I am drawing raindrops
    glColor3f(0.0, 0.0, 1.0)  # Here Sir, I am using blue for rain
    for raindrop in raindrops:
        draw_raindrop(raindrop[0], raindrop[1])

    glutSwapBuffers()

def animate():
    global raindrops, rain_vx, rain_vy
    for raindrop in raindrops:
        raindrop[0] += rain_vx  # Here Sir, I am adjusting horizontal position
        raindrop[1] += rain_vy  # Here Sir, I am moving downward
        # Here Sir, I am resetting to top if below screen
        if raindrop[1] < 0:
            raindrop[1] = 500
            raindrop[0] = random.uniform(0, 500)
        # Here Sir, I am clamping x within bounds
        raindrop[0] = max(0, min(500, raindrop[0]))
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global rain_vx
    if key == GLUT_KEY_LEFT:
        rain_vx -= 0.1  # Here, I am bending rain left
    elif key == GLUT_KEY_RIGHT:
        rain_vx += 0.1  # Here, I am bending rain right
    glutPostRedisplay()

def keyboardListener(key, x, y):
    global bg_color
    if key == b'd':  # 'd' for day (here, im using it for lighten background)
        bg_color = min(1.0, bg_color + 0.1)
    elif key == b'n':  # 'n' for night (here, im using it for darken background)
        bg_color = max(0.0, bg_color - 0.1)
    glutPostRedisplay()

# Here Sir, I;m initializing GLUT
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"House with Rainfall made by Sayed Sohanul Islam")  # Here Sir, I am updating window title
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMainLoop()



#TASK_2
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

# Here Sir, I am setting window dimensions
W_Width, W_Height = 500, 500

# Global variables
speed = 0.1
freeze = False
blinking = False
blink_timer = 0
blink_interval = 0.5

points = []

def draw_points(x, y, color):
    glColor3f(*color)
    glPointSize(5)  # Here Sir, I am setting point size to 5 pixels
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

# Here Sir, I am setting up the OpenGL projection and viewport
def iterate():
    glViewport(0, 0, W_Width, W_Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, W_Width, 0.0, W_Height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Here Sir, it is the display callback
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  #Here Sir, I am clearing the screen with black
    glLoadIdentity()
    iterate()
    current_time = time.time()
    for point in points:
        # If blinking is active, alternate between point color and background color
        if blinking and (current_time - blink_timer) % (2 * blink_interval) < blink_interval:
            draw_points(point['x'], point['y'], (0, 0, 0))  # Background color (black)
        else:
            draw_points(point['x'], point['y'], point['color'])  # Original color
    glutSwapBuffers()

# Here Sir, I am idling callback to update point positions
def animate():
    if not freeze:  #  update if not frozen
        for point in points:
            # Here Sir, I am updating position based on velocity and speed
            point['x'] += point['dx'] * speed
            point['y'] += point['dy'] * speed
            if point['x'] <= 0 or point['x'] >= W_Width:
                point['dx'] = -point['dx']
            if point['y'] <= 0 or point['y'] >= W_Height:
                point['dy'] = -point['dy']
    glutPostRedisplay()  # Here Sir, I am requesting a redraw

# Here Sir, I am using mouse callback to handle left and right clicks
def mouseListener(button, state, x, y):
    global blinking, blink_timer
    if state == GLUT_DOWN and not freeze:
        if button == GLUT_RIGHT_BUTTON:
            dir_x = random.choice([-1, 1])
            dir_y = random.choice([-1, 1])
            color = (random.random(), random.random(), random.random())
            points.append({
                'x': x,
                'y': W_Height - y,
                'dx': dir_x,
                'dy': dir_y,
                'color': color
            })
        elif button == GLUT_LEFT_BUTTON:
            blinking = not blinking
            if blinking:
                blink_timer = time.time()
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global speed
    if not freeze:
        if key == GLUT_KEY_UP:
            speed *= 1.5
        elif key == GLUT_KEY_DOWN:
            speed /= 1.5
    glutPostRedisplay()

def keyboardListener(key, x, y):
    global freeze
    if key == b' ':
        freeze = not freeze
    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)  # Here Sir, I am doubling buffering with RGBA
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Amazing Box Created By Sayed Sohanul Islm")  # Window title

# Here Sir, I am registering callback functions
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)

# Here Sir, I am setting background color to black
glClearColor(0, 0, 0, 0)

glutMainLoop()
