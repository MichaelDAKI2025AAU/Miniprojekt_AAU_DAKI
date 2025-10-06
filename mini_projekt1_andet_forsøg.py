import math #import af pakker i python
import time
import pygame 

pygame.init()
screen = pygame.display.set_mode((800,800)) #grundlæggende variabler
clock = pygame.time.Clock()
center = (400,400)

run_flag = True #hovedløkke
while run_flag is True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False 
   
    screen.fill((255,255,255)) # Baggrundsfarve

    now = time.localtime() # tid og variabler hertil
    seconds = now.tm_sec
    minutes = now.tm_min
    hour = now.tm_hour%12

    pygame.draw.circle(screen,(0,0,0),(center),300) # tegning af urskiver
    pygame.draw.circle(screen,(255,255,255),(265,400),115)
    pygame.draw.circle(screen,(255,255,255),(535,400),115)

    pygame.draw.rect(screen,(255,255,255),(325,200,150,50)) # Visning af ugedagen
    day = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]
    weekday = day[now.tm_wday]
    font_wday=pygame.font.SysFont(None,50)
    tekst = font_wday.render(weekday, True, (0, 0, 0))
    tekst_rect = tekst.get_rect(center=(400, 225))
    screen.blit(tekst, tekst_rect)
    
    pygame.draw.rect(screen,(255,255,255),(300,550,200,50)) # Visning af måned og dato
    months = ["Januar", "Februar", "Marts", "April", "Maj", "Juni",
    "Juli", "August", "September", "Oktober", "November", "December"]
    month = months[now.tm_mon - 1] 
    font_month=pygame.font.SysFont(None,50)
    tekst = font_wday.render((f"{now.tm_mday}. {month}"), True, (0, 0, 0))
    tekst_rect = tekst.get_rect(center=(400, 575))
    screen.blit(tekst, tekst_rect)

    font_hour = pygame.font.SysFont(None, 48) # tal på urskiven
    for i in range (1,13):
        angel_hour= math.radians(i * 30 - 90)
        radius_hour = 270
        x_hour = int(400 + radius_hour * math.cos(angel_hour))
        y_hour = int(400 + radius_hour * math.sin(angel_hour))
        tekst = font_hour.render(str(i), True, (255, 255, 255))
        tekst_rect = tekst.get_rect(center=(x_hour, y_hour))
        screen.blit(tekst, tekst_rect)
    
    hour_length=235 #timeviseren
    hour_angel=math.radians(hour * 30 -90)
    x_hour_pos=(400+hour_length*math.cos(hour_angel))
    y_hour_pos=(400+hour_length*math.sin(hour_angel))
    pygame.draw.line(screen,(255,0,0),(center),(x_hour_pos,y_hour_pos), 5)
    pygame.draw.aaline(screen, (255,0,0), center, (x_hour_pos,y_hour_pos))


    font_min=pygame.font.SysFont(None, 20) #Tal i minutcirkel
    for i in range (1,13):
        min_angel= math.radians(i * 30 - 90)
        min_radius= 100
        x_min = int(400-radius_hour/2 + min_radius * math.cos(min_angel))
        y_min = int(400 + min_radius * math.sin(min_angel))
        tekst = font_min.render(str(i*5), True, (0, 0, 0))
        tekst_rect = tekst.get_rect(center=(x_min, y_min))
        screen.blit(tekst, tekst_rect)
        
    tekst = font_min.render('min', True, (0, 0, 0)) # Skrivning af 'min' i minutviseren
    tekst_rect = tekst.get_rect(center=(x_min, y_min+150))
    screen.blit(tekst, tekst_rect)

    min_length= 80 #minutviser
    min_angel=math.radians(minutes*6-90)
    x_min_pos=(400-radius_hour/2+min_length*math.cos(min_angel))
    y_min_pos=(400+min_length*math.sin(min_angel))
    pygame.draw.line(screen,(0,0,0),((400-radius_hour/2,400)),(x_min_pos,y_min_pos),2)

    font_sec=pygame.font.SysFont(None, 20) #tal i sekundtviser
    for i in range (1,13):
        sec_angel= math.radians(i * 30 - 90)
        sec_radius= 100
        x_sec = int(400+radius_hour/2 + sec_radius * math.cos(sec_angel))
        y_sec = int(400 + sec_radius * math.sin(sec_angel))
        tekst = font_sec.render(str(i*5), True, (0, 0, 0))
        tekst_rect = tekst.get_rect(center=(x_sec, y_sec))
        screen.blit(tekst, tekst_rect)
        
    tekst = font_sec.render('sec', True, (0, 0, 0)) #skrivning af "sec" i sekundtcirklen
    tekst_rect = tekst.get_rect(center=(x_sec, y_sec+150))
    screen.blit(tekst, tekst_rect)

    sec_length= 80 #sekundtviser
    sec_angel=math.radians(seconds*6-90)
    x_sec_pos=(400+radius_hour/2+sec_length*math.cos(sec_angel))
    y_sec_pos=(400+sec_length*math.sin(sec_angel))
    pygame.draw.line(screen,(0,0,0),((400+radius_hour/2,400)),(x_sec_pos,y_sec_pos),2)

    pygame.display.flip() #genopfriskning af skærm
    clock.tick(60)