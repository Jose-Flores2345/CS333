import turtle
import time
import functions


delay = 0.1
# Screen
wn = turtle.Screen()
wn.title('Snake game by Jose Flores')
wn.bgcolor("grey")
wn.setup(width=1920, height=1080)
wn.tracer(0)
# Movement
wn.listen()
wn.onkeypress(functions.go_up, 'w')
wn.onkeypress(functions.go_down, 's')
wn.onkeypress(functions.go_left, 'a')
wn.onkeypress(functions.go_right, 'd')




while True:
    wn.update()
    functions.move()
    time.sleep(delay)
wn.mainloop()

