random = randint(1, 2)

item = 0

def on_button_pressed_a():
    item == 1
input.on_button_pressed(Button.A, on_button_pressed_a)
    
def on_button_pressed_b():
    item == 2
input.on_button_pressed(Button.B, on_button_pressed_b)
    
for i in range(5):
    if random == item:
        basic.show_string("Win!")
    else:
        basic.show_string("Lose")

    
