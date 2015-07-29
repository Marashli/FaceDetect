import pygame.camera
import pygame.image
import time

i = 1

pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()

while True:
    print(i)
    time.sleep(3)
    img = cam.get_image()
    pygame.image.save(img, str(i) + ".bmp")
    i += 1

