# Libraries
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, tan, sinh, cosh, tanh
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Themes
sg.theme('DarkAmber')
plt.style.use('seaborn-darkgrid')

# Global Variables
font = ("cobber black", 14)
canvas: FigureCanvasTkAgg = None
fig: any = plt.figure()
window: any
layout = [
    [sg.Text("Enter The Equation as Function of X:", font=font, background_color='#030314'),
     sg.InputText(font=font, background_color='#505050')],
    [sg.Text(text="Min X:", font=font, background_color='#030314'),
     sg.InputText(background_color='#505050', font=font, size=(10, 5)),
     sg.Text(text="Max X:", font=font, background_color='#030314'),
     sg.InputText(background_color='#505050', font=font, size=(10, 5))],
    [sg.Button('Plot', font=font)],
    [sg.Canvas(key='canvas', background_color='#030314', border_width=0)]
]


def verify(equ, min, max):
    # Empty fields check
    if not equ:
        sg.popup_error("Error: Equation field is empty", background_color='#030314')
        return 0
    elif (not min) or (not max):
        sg.popup_error("Error: Min or Max fields are empty", background_color='#030314')
        return 0
    # valid numbers for range checks
    try:
        float(min)
        float(max)
    except:
        sg.popup_error("Error: Max and min must be numbers", background_color='#030314')
        return 0
    if min > max:
        sg.popup_error("Error: Max must be greater than min", background_color='#030314')
        return 0

    equ = equ.replace('^', '**')
    x = np.linspace(float(min), float(max))

    # evaluation check
    try:
        eval(equ)
    except ZeroDivisionError:
        sg.popup_error("Error: Division by zero found", background_color='#030314')
        return 0
    except NameError:
        sg.popup_error("Error: Unknown characters existed in the equation", background_color='#030314')
        return 0
    except FloatingPointError:
        sg.popup_error("Error: Computing Error", background_color='#030314')
        return 0
    except:
        sg.popup_error("Error: This function can't be evaluated", background_color='#030314')
        return 0

    return 1


def plot(equ, min, max):
    global fig, canvas, window

    # clean the canvas
    if canvas:
        canvas.get_tk_widget().forget()

    # prepare x and y for plotting
    x = np.linspace(float(min), float(max))
    equ = equ.replace('^', '**')

    y = eval(equ)

    # handle constants case
    if (equ.find('x') == -1) and (equ.find('X') == -1):
        y = np.linspace(float(min), float(max))
        y.fill(float(equ))

    plt.clf()
    plt.plot(x, y, 'b')
    canvas = FigureCanvasTkAgg(fig, window['canvas'].TKCanvas)
    canvas.draw()
    canvas.get_tk_widget().pack(side='bottom', fill='both')


# Window Initialisation
window = sg.Window('Function Plotter',
                   layout,
                   finalize=True,
                   location=(200, 100),
                   element_justification="center",
                   background_color='#030314',
                   enable_close_attempted_event=True
                   )

# Driver
while True:
    # take inputs
    event, values = window.read()
    if event == "Plot":
        if verify(values[0], values[1], values[2]):
            plot(values[0], values[1], values[2])
        values.clear()
    elif event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
        if sg.popup_yes_no('Are you sure that you want to exit?', background_color='#030314') == 'Yes':
            break

window.close()
