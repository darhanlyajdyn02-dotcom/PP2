import pygame
import sys
import math

pygame.init()


WIDTH = 1000
HEIGHT = 700
TOOLBAR_H = 80

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 20)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)
GREEN = (0, 180, 0)
BLUE = (50, 100, 255)
YELLOW = (255, 215, 0)
GRAY = (220, 220, 220)
DARK_GRAY = (120, 120, 120)


canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_H))
canvas.fill(WHITE)

#
current_color = BLACK
brush_size = 6
tool = "pen"  

drawing = False
start_pos = None
last_pos = None

palette = [
    (BLACK, pygame.Rect(20, 20, 40, 40)),
    (RED, pygame.Rect(70, 20, 40, 40)),
    (GREEN, pygame.Rect(120, 20, 40, 40)),
    (BLUE, pygame.Rect(170, 20, 40, 40)),
    (YELLOW, pygame.Rect(220, 20, 40, 40)),
]



def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_H))

   
    for color, rect in palette:
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

   
    pygame.draw.rect(screen, current_color, (290, 20, 40, 40))
    pygame.draw.rect(screen, BLACK, (290, 20, 40, 40), 2)

    
    text1 = font.render(f"Tool: {tool}", True, BLACK)
    text2 = font.render(f"Brush size: {brush_size}", True, BLACK)
    text3 = font.render("P-pen  R-rect  C-circle  E-eraser  1..5-colors", True, BLACK)

    screen.blit(text1, (360, 12))
    screen.blit(text2, (360, 35))
    screen.blit(text3, (520, 25))


def draw_line(surface, color, start, end, width):
    
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))

    if distance == 0:
        pygame.draw.circle(surface, color, start, width)
        return

    for i in range(distance + 1):
        x = int(start[0] + dx * i / distance)
        y = int(start[1] + dy * i / distance)
        pygame.draw.circle(surface, color, (x, y), width)


def get_canvas_pos(mouse_pos):
    
    return (mouse_pos[0], mouse_pos[1] - TOOLBAR_H)


def inside_canvas(mouse_pos):
    return mouse_pos[1] >= TOOLBAR_H



while True:
    preview_canvas = canvas.copy()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                tool = "pen"
            elif event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = GREEN
            elif event.key == pygame.K_4:
                current_color = BLUE
            elif event.key == pygame.K_5:
                current_color = YELLOW
            elif event.key == pygame.K_UP:
                brush_size += 1
            elif event.key == pygame.K_DOWN:
                brush_size = max(1, brush_size - 1)

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

           
            for color, rect in palette:
                if rect.collidepoint(mouse_pos):
                    current_color = color

            
            if inside_canvas(mouse_pos):
                drawing = True
                start_pos = get_canvas_pos(mouse_pos)
                last_pos = start_pos

                
                if tool == "pen":
                    pygame.draw.circle(canvas, current_color, start_pos, brush_size)
                elif tool == "eraser":
                    pygame.draw.circle(canvas, WHITE, start_pos, brush_size)

        
        if event.type == pygame.MOUSEMOTION and drawing:
            mouse_pos = pygame.mouse.get_pos()

            if inside_canvas(mouse_pos):
                current_pos = get_canvas_pos(mouse_pos)

               
                if tool == "pen":
                    draw_line(canvas, current_color, last_pos, current_pos, brush_size)
                    last_pos = current_pos

              
                elif tool == "eraser":
                    draw_line(canvas, WHITE, last_pos, current_pos, brush_size)
                    last_pos = current_pos

        
        if event.type == pygame.MOUSEBUTTONUP and drawing:
            mouse_pos = pygame.mouse.get_pos()

            if inside_canvas(mouse_pos):
                end_pos = get_canvas_pos(mouse_pos)

                
                if tool == "rect":
                    x = min(start_pos[0], end_pos[0])
                    y = min(start_pos[1], end_pos[1])
                    w = abs(end_pos[0] - start_pos[0])
                    h = abs(end_pos[1] - start_pos[1])
                    pygame.draw.rect(canvas, current_color, (x, y, w, h), 2)

           
                elif tool == "circle":
                    radius = int(math.dist(start_pos, end_pos))
                    pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

            drawing = False
            start_pos = None
            last_pos = None

 
    screen.fill(DARK_GRAY)
    draw_toolbar()

    
    if drawing and tool in ("rect", "circle") and inside_canvas(pygame.mouse.get_pos()):
        current_pos = get_canvas_pos(pygame.mouse.get_pos())

        if tool == "rect":
            x = min(start_pos[0], current_pos[0])
            y = min(start_pos[1], current_pos[1])
            w = abs(current_pos[0] - start_pos[0])
            h = abs(current_pos[1] - start_pos[1])
            pygame.draw.rect(preview_canvas, current_color, (x, y, w, h), 2)

        elif tool == "circle":
            radius = int(math.dist(start_pos, current_pos))
            pygame.draw.circle(preview_canvas, current_color, start_pos, radius, 2)

        screen.blit(preview_canvas, (0, TOOLBAR_H))
    else:
        screen.blit(canvas, (0, TOOLBAR_H))

    pygame.display.update()
    clock.tick(60)