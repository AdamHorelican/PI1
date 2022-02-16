#https://www.rapidtables.com/web/color/RGB_Color.html
import pyglet
from pyglet import shapes
from pyglet.window import key
#globalne
SIRKA = 960
VYSKA = 540
title = "Horelican-Tetris"
window = pyglet.window.Window(SIRKA, VYSKA, title)
batch = pyglet.graphics.Batch()


stripe = []
#farby
zlta = (255,255,255)
fialova = (229,204,255)
zelena = (204,255,229)
black = (0,0,0)

#hrube farby mid

collum_x = 360
for i in range(10):
    moja_farba = fialova
    if i % 2 == 0:
        moja_farba = zelena
    i = i + 1
    collum_x = collum_x + 20
    stripe.append(shapes.Rectangle(collum_x, 70, 20, 400, color=moja_farba, batch=batch))


collum_x2 = 380
for i in range(10):
    i = i + 1
    collum_x2 = collum_x2 + 20
    stripe.append(shapes.Rectangle(collum_x2, 470, 1, -400, color=black, batch=batch))


collum_y = 90
for i in range(20):
    i = i + 1
    collum_y = collum_y + 20
    stripe.append(shapes.Rectangle(380, collum_y, 200, 1, color=black, batch=batch))



"""
# tvar i
stripe.append(shapes.Rectangle(540, 310, 20, 80, color=black, batch=batch))

# tvar z
z = stripe.append(shapes.Rectangle(440, 290, 40, 20, color=black, batch=batch)),
stripe.append(shapes.Rectangle(460, 270, 40, 20, color=black, batch=batch))

# tvar t
stripe.append(shapes.Rectangle(420, 430, 60, 20, color=black, batch=batch))
stripe.append(shapes.Rectangle(440, 410, 20, 20, color=black, batch=batch))

# tvar L naopak
stripe.append(shapes.Rectangle(520, 230, 20, 60, color=black, batch=batch))
stripe.append(shapes.Rectangle(500, 230, 20, 20, color=black, batch=batch))
# tvar o
"""
"""
stripe.append(shapes.Rectangle(480, 110, 20, 20, color=black, batch=batch))
stripe.append(shapes.Rectangle(480, 90, 20, 20, color=black, batch=batch))
stripe.append(shapes.Rectangle(500, 110, 20, 20, color=black, batch=batch))
stripe.append(shapes.Rectangle(500, 90, 20, 20, color=black, batch=batch))

stripe.append(shapes.Rectangle(460, 110, 20, 20, color=black, batch=batch))
stripe.append(shapes.Rectangle(460, 90, 20, 20, color=black, batch=batch))
stripe.append(shapes.Rectangle(480, 110, 20, 20, color=black, batch=batch))
stripe.append(shapes.Rectangle(480, 90, 20, 20, color=black, batch=batch))

"""
def draw_palicka():
    x = 480
    y = 110
    for i in range(4):
        stripe.append(shapes.Rectangle(x, y, 20, 20, color=black, batch=batch))
      #  print("x ={} ".format(x))
        print("y ={} ".format(y))
      #  x = x - 20
        y = y + 20

"""
x = 480
y = 210
for i in range(4):
    stripe.append(shapes.Rectangle(x, y, 20, 20, color=black, batch=batch))
    print("x ={} ".format(x))
    #print("y ={} ".format(y))
    x = x - 20
  #  y = y + 20


# tvar L
stripe.append(shapes.Rectangle(400, 190, 20, 60, color=black, batch=batch))
stripe.append(shapes.Rectangle(420, 190, 20, 20, color=black, batch=batch))
"""
score_text = pyglet.text.Label('SCORE:',
                          font_name='Times New Roman',
                          font_size=60,
                          x=30, y=470,
                        )

next_shape = pyglet.text.Label('NEXT SHAPE'
                               '  ↓',
                          font_name='Times New Roman',
                          font_size=30,
                          x=620, y=420,
                        )
#farby textu
next_shape.color = (22,222,1,200)
score_text.color = (255,0,0,200)



@window.event
def on_draw():
    window.clear()
    batch.draw()
    score_text.draw()
    next_shape.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        draw_palicka()

    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')

pyglet.app.run()