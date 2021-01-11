let random = randint(1, 2)
let item = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    item == 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    item == 2
})
for (let i = 0; i < 5; i++) {
    if (random == item) {
        basic.showString("Win!")
    } else {
        basic.showString("Lose")
    }
    
}
