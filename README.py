# Mars_Lion
#It is stuff for mars

import pygam
Pygame.inut()

fps = 45
timer = pygame.time.Clock()
WHITH = 1200
HEIGHT = 1000
active_size = 0
active_color = (255, 0, 0)
screen = pygame.display.set_mode([WIDTH, Height])
pygame.display.set_caption('Paint!')
painting = []

def draw_menu():
  pygame.draw.rect(screen, (0, 127, 127), [0, 0, WHITH, 100])
  pygame.draw.line(sreen, 255, 0, 0), (0, 70), (WIDTH,100), 3)
  m_brush = pygame.draw.rect(screen, (255,0,0), [10, 10, 50, 50])
  pygame.draw.circle(screen, (0, 255, 255), (50, 35), 20)
  s_brush = pygame.draw.rect(screen, (255, 0, 0), [60, 10, 50, 50])
  pygame.draw.circle(screen, (0, 255 ,255), (100, 35), 10)
  brush_list = [m_brush, s_brush]

  blue = pygame.draw.rect(screen, (0, 0, 255), []WIDTH -50, 10, 50,50])
  pink = pygame.draw.rect(screen, (255, 0, 255), []WIDTH -50, 50, 50,50])
  cyan = pygame.draw.rect(screen, (0, 255, 255), []WIDTH -100, 10, 50,50])
  green = pygame.draw.rect(screen, (0, 0, 255), []WIDTH -100, 50, 50,50])
  white = pygame.draw.rect(screen, (255, 255, 255), []WIDTH -160, 10, 50,50])
  black = pygame.draw.rect(screen, (0, 0, 0), []WIDTH -160, 60, 50,50])
  yellow = pygame.draw.rect(screen, (255, 255, 0), []WIDTH -200, 60, 50,50])
  red = pygame.draw.rect(screen, (255, 255, 0), []WIDTH -255, 10p;, 50,50])
  color_rect = [blue, pink, cyan, green, white, black, yellow, red]
  rgb_list = [(0, 0, 255), (255, 0, 255), (0, 255, 255), (255, 255, 255), (0, 0, 0), (255, 255, 0), (255, ,0 ,0)]
  return brush_list, color_rect, rgb_list

def draw_painting(paints):
  for i in range (len(paints)):
    pygame.draw.circle(screen, paint[i][0], paints[i][1], paints[i][2])
  

run = True 
while run:  
  timer.tick(fps)
  screen.fill(0, 255, 255)
  mouse = pygame.mouse.get_pos()
  left_click = pygame.mouse.get_pressed()[0]
  if mouse[1] > 100:
    pygame.draw.circle(screen, active_color, mouse, active_size)
  if left_click and mouse[1] > 100:
    painting.append((active_color, mouse, active_size))
  draw_painting(painting)
  brushes, colors, rgbs = draw_menu()
    
  for event in pygame.event.get():
     if event.type == pygame.QUIT:
        run = False
       
     if event.type == pygame.MOUSEBUTTONDOWN:
       for i in range(lan(brushes)):
         if brushes[i].collidepoint(event.pos)
           active_size = 5 - i

        for i in range(lan(colors)):
          if colors[i].collidepoint(event.pos)
            active_corlor = rgb[i]
         
  Pygame.display.flip()
Pygame.quit()
#Mars
