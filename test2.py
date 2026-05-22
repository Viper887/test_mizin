import turtle

def draw_enhanced_figure():
    screen = turtle.Screen()
    screen.setup(600, 600)
    t = turtle.Turtle()
    t.speed(8)  # Швидкість малювання
    t.pensize(3)
    t.color("black", "#fcd5b5") # Колір контуру та заливки (тілесний)

    # Функція для малювання основи (яєчок)
    def draw_base():
        t.penup()
        t.goto(-45, -100)
        t.pendown()
        t.begin_fill()
        
        # Ліве
        t.setheading(180)
        t.circle(45, 180) 
        
        # Праве
        t.setheading(0)
        t.circle(-45, 180)
        
        # З'єднання знизу
        t.setheading(180)
        t.forward(90)
        t.end_fill()

    # Функція для малювання стовбура та головки
    def draw_shaft_and_head():
        # Стовбур
        t.penup()
        t.goto(-35, -20) # Початок стовбура трохи вище основи
        t.setheading(90)
        t.pendown()
        
        t.begin_fill()
        t.forward(140) # Висота стовбура
        
        # Головка (більш плавна форма)
        t.right(45)
        t.circle(-50, 90) # Закруглення верхівки
        t.right(45)
        
        # Спуск вниз
        t.forward(140)
        
        # З'єднання ліній стовбура внизу
        t.setheading(180)
        t.forward(70)
        t.end_fill()
        
        # Додаткова лінія для деталізації головки
        t.penup()
        t.goto(-35, 120) 
        t.pendown()
        t.setheading(0)
        # Використовуємо трохи темніший колір для лінії
        t.color("#e0ac81") 
        t.circle(-35, 180)

    # Виклик функцій
    draw_base()
    t.color("black", "#fcd5b5") # Повертаємо основний колір
    draw_shaft_and_head()

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_enhanced_figure()
