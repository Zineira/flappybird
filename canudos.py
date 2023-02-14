import pygame


class Canudos:
    def __init__(self, x, height, image_top, image_bottom):
        self.x = x
        self.height = height
        self.gap = 50
        try:
            self.image_top = pygame.image.load(image_top)
            self.image_bottom = pygame.image.load(image_bottom)
        except Exception as e:
            print("Ocorreu um erro ao carregar a imagem:", e)
        self.image_top = pygame.transform.scale(self.image_top, (125, 500))
        self.image_bottom = pygame.transform.scale(
            self.image_bottom, (125, 500))

    def update(self):
        self.x -= 5

    def draw(self, screen):
        screen.blit(self.image_top, (int(self.x), -30))
        screen.blit(self.image_bottom,
                    (int(self.x), int(self.height+self.gap)))
