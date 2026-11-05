import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Фрактал Серпинского (Метод Хаоса)")
turtle.tracer(50, 0)  # Отрисовка пачками по 50 точек для скорости

t = turtle.Turtle()
t.hideturtle()
t.up()

# Три опорные вершины треугольника (X, Y)
vertices = [(-300, -200), (0, 300), (300, -200)]
colors = ["#ff4757", "#2ed573", "#1e90ff"]  # Цвета для каждой вершины

# Начальная случайная точка внутри треугольника
current_pos = [0, 0]

# Ставим 20 000 точек
for _ in range(20000):
    # Выбираем случайную вершину из трех
    target_idx = random.randint(0, 2)
    target = vertices[target_idx]
    
    # Находим середину пути до нее
    current_pos[0] = (current_pos[0] + target[0]) / 2
    current_pos[1] = (current_pos[1] + target[1]) / 2
    
    # Прыгаем туда и рисуем пиксель цветом выбранной вершины
    t.goto(current_pos[0], current_pos[1])
    t.dot(2, colors[target_idx])

screen.update()
turtle.done()
