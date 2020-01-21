import pygame
import pygame.camera
import pygame.image
import pygame.font

# camera
pygame.init()  # pylint: disable=no-member
pygame.camera.init()
pygame.font.init()

webcam = pygame.camera.Camera(0)
webcam.start()

screen = pygame.display.set_mode((700, 640))
screen.fill((79,99,103))
pygame.display.set_caption("camera")

over_btn = False

capture = pygame.draw.rect(screen,(122,158,159), (30, 500, 640, 65))

text = pygame.font.SysFont('Comic Sans MS', 35, 1)
textsurface = text.render('i d e n t i f y   o b j e c t', False, (238,245,216))


while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pylint: disable=no-member
            open = False

    img = webcam.get_image()
    screen.blit(img, (30, 30))
    screen.blit(textsurface, (116,510))
    
    if capture.collidepoint(pygame.mouse.get_pos()):
      over_btn = True
    else:
        over_btn = False

    if over_btn:
       pygame.image.save(img,"picture.jpg")
   
    pygame.display.update()
