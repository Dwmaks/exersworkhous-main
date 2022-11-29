import pygame


def draw _picture(screen, x, y, widht, height):
    """
    Рисует картинку с домиком на фоне травы и неба.

    :param screen: дисплей pygame, на котором будет изображение
    :param x: левая координата прямоугольника с рисунком
    : param y: верхняя координата прямоугольника с рисунком
    : param widht:  ширина прямоугольника
    : param height: высота прямоугольника
    """
    draw_backgroun(screen, x, y, width, height)
    house_x = x + width // 2
    house_y = y + 3 * height // 4
    house_height = min(height, width) * 2 // 3
    house_width = int(house_height * 1.5)
    draw_house(screen, house_x, house_y, house_width, house_height )
    sun_radius = min(width, height) // 10
    draw_sun(screen, x, y, sun_radius)


def draw_bacground(screen, x, y, width, height):
    """
    Рисует прямоугольный фон для с домиком на фоне травой и небом.

    :param screen: дисплей pygame, на котором будет изображение
    :param x: левая координата прямоугольника с фоном
    : param y: верхняя координата прямоугольника с рисунком
    : param widht:  ширина прямоугольника
    : param height: высота прямоугольника
    """
    print("Типа рисую фон:", x, y, width, height)


def draw_house(screen, x, y, widht, height):
        """
        Рисует домик заданных размеров от точки (x, y).
        Внимание! Опорная точка находится посеридине внизу основания

        :param screen: дисплей pygame, на котором будет изображение
        :param x: Горизонтальная координата опорной точки
        : param y: Вертикальная координата опорной точки
        : param widht:  ширина прямоугольника
        : param height: полная высота домика
        """
    print("Типа рисую домик:", x, y, widht, height)


def draw_sun(screen, x, y, radius):
    """
           Рисует солнышко в виде четверти круга справа снизу от опорной точки

           :param screen: дисплей pygame, на котором будет изображение
           :param x: Горизонтальная координата опорной точки
           : param y: Вертикальная координата опорной точки
           :param radius:  радиус
           """
    print ("Типа рисую солнышко:", x, y, radius)


pygame.init()
width, height = screen_size = (300, 200)
screen = pygame.display.set_mode(screen_size)

#Здесь нужно рисовать
draw_picture(screen, 0,0, width, height)


pygame.display.update()

work_flag = True
while work_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            work_flag = False
print("Программа благополучно завершена.")
