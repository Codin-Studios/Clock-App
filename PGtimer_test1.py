import pygame
print("INSTRUCTIONS : Enter the time for timer in  seconds of whatever stamp ya want")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
hue = (12, 22, 38)
pygame.init()
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Timer")
done = False
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
frame_count = 0
frame_rate = 60
x = int(input("Enter the time stamp ya want : "))
start_time = x
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        print(event)
    screen.fill(hue)
    total_seconds = frame_count // frame_rate
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250, 200])
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250, 220])
    frame_count += 1
    clock.tick(frame_rate)
    pygame.display.flip()

pygame.quit()