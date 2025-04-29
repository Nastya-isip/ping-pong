from pygame import *
# размеры окна
width = 600
height = 500
# создание окна
window = display.set_mode((width, height))
display.set_caption("Ping Pong")
back = (200, 255, 255)  # цвет заливки для фона
window.fill(back)  # заливка фона
# внутриигровые часы и ФПС
clock = time.Clock()
FPS = 60
game = True
# игровой цикл (как программы)
while game:
    # обработка нажатия кнопки закрыть окно
    for e in event.get():
        if e.type == QUIT:
            game = False  # завершение игрового цикла (как программы)
# обновляем все содержимое на экране
    display.update()
    clock.tick(FPS)
