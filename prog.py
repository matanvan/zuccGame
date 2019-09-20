
import pygame
import math, random, time

pygame.init()
screen = pygame.display.set_mode((625, 1000))
pygame.display.set_caption("The Zucc game")
logo = pygame.image.load('306c55c2c5f793c93af4a8b273c495aa_32_abc9a258b4298d486ff08542e2c94a70.png')
pygame.display.set_icon(logo)
Zuccy = pygame.image.load('the_zucc.png')
judge = 'judge.png'
background = pygame.image.load('background.png')
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.font.init()

gamemode = 'normal'
score = 0
clock_refresh = 100
release_token = 60
speedup_counter = 0
speedup_point = 2
token_picker = 60


class Token(object):
    attribute_list = []

    def __init__(self, x_pos, path):
        self.flag = path[:-4]
        self.x = x_pos
        self.y = -100
        self.image = pygame.image.load(path).convert()
        self.image.set_colorkey((163, 73, 164))
        self.token = None
        Token.attribute_list.append(self)

    def update(self):
        self.token = screen.blit(self.image, (self.x, self.y))
        self.y += 2
        if self.y >= 1000:
            Token.attribute_list.remove(self)

        if player.colliderect(self.token):
            Token.attribute_list.remove(self)
            global clock_refresh
            global speedup_counter
            global release_token
            global speedup_point
            global score
            global token_picker
            global running
            if self.flag == 'personal_data':
                clock_refresh += 5
                score += 100
                speedup_counter += 1
            elif self.flag == 'cop':
                score -= random.randint(0, 340)
            elif self.flag == 'judge' or self.flag == 'stalin':
                clock_refresh = 60
                release_token = 60
                speedup_point = 2
                speedup_counter = 0
                token_picker = 60
                score -= random.randint(340, 720)
            elif self.flag == 'prison_bars':
                running = False


start_button_color = (255, 255, 255)
time_mode_color = (255, 255, 255)
start_button = pygame.font.SysFont('Bradley Hand ITC', 60).render('Start', False, start_button_color)
time_mode = pygame.font.SysFont('Bradley Hand ITC', 60).render('Start in time mode', False, time_mode_color)
opening_text_dict = {'WELCOME TO THE ZUCC GAME!':(40, 10), '_____________________________________':(40, 15),
                     'In this game, you shall play the great Zuccy.':(30, 60),
                     'The great Zucc follows your mouse on the screen.':(30, 95),
                     'Catch this precious personal data to earn points.':(30, 130),
                     'Do not touch the the cops, for they will take your':(30, 165),
                     'points. The judges are even worse, they will take':(30, 200),
                     'your points and throw you back to level 1! And':(30, 235),
                     'lastly, prison bars will end the game, so make':(30, 270),
                     'sure not to touch \'em. Oh, and time mode':(30, 305),
                     ' does\'nt work yet, so don\'t even try.':(30, 340),
                     'Good luck!':(50, 380),
                     '©All of the rights for the background and the player':(25, 800),
                     'figure are reserved to Facebook and Mark Zuckerberg':(25, 830),
                     '©The rights for the song are reserved to Grandayy':(25, 880)}
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 312 - (start_button.get_width() // 2) <= pygame.mouse.get_pos()[0] <= 312 + (start_button.get_width() // 2) and 600 <= pygame.mouse.get_pos()[1] <= 600 + start_button.get_height():
                running = False
            elif 312 - (time_mode.get_width() // 2) <= pygame.mouse.get_pos()[0] <= 312 + (time_mode.get_width() // 2) and 700 <= pygame.mouse.get_pos()[1] <= 700 + time_mode.get_height():
                pass

    if 312 - (start_button.get_width() // 2) <= pygame.mouse.get_pos()[0] <= 312 + (start_button.get_width() // 2) and 600 <= pygame.mouse.get_pos()[1] <= 600 + start_button.get_height():
        start_button_color = (255, 0, 0)
        time_mode_color = (255, 255, 255)
    elif 312 - (time_mode.get_width() // 2) <= pygame.mouse.get_pos()[0] <= 312 + (time_mode.get_width() // 2) and 700 <= pygame.mouse.get_pos()[1] <= 700 + time_mode.get_height():
        start_button_color = (255, 255, 255)
        time_mode_color = (255, 0, 0)
    else:
        start_button_color = (255, 255, 255)
        time_mode_color = (255, 255, 255)
    for key in opening_text_dict.keys():
        opening_text = pygame.font.SysFont('Bradley Hand ITC', opening_text_dict[key][0]).render(key, False, (255, 255, 255))
        screen.blit(opening_text, (312 - (opening_text.get_width() // 2), opening_text_dict[key][1]))

    start_button = pygame.font.SysFont('Bradley Hand ITC', 60).render('Start', False, start_button_color)
    time_mode = pygame.font.SysFont('Bradley Hand ITC', 60).render('Start in time mode', False, time_mode_color)
    screen.blit(start_button, (312 - (start_button.get_width() // 2), 600))
    screen.blit(time_mode, (312 - (time_mode.get_width() // 2), 700))
    pygame.display.flip()

running = True
pygame.mouse.set_visible(False)
generate = 0
pygame.mixer.music.load('ZUCCY ZUCCY YES PAPA.mp3')
pygame.mixer.music.play(-1)
pause = 0
exit_display_color = (0, 0, 0)
exit_display = pygame.font.SysFont('Bradley Hand ITC', 30).render('Exit', False, exit_display_color)
player_pos = pygame.mouse.get_pos()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if pause == 0:
                    player_pos = pygame.mouse.get_pos()
                    pause = 1
                elif pause == 1:
                    pygame.mouse.set_pos(*player_pos)
                    pause = 0
            elif event.key == pygame.K_SLASH:
                if pause == 0:
                    player_pos = pygame.mouse.get_pos()
                    command = ''
                    show_cursor = True
                    pause = 2
                elif pause == 2:
                    pygame.mouse.set_pos(*player_pos)
                    pause = 0

        if 5 <= pygame.mouse.get_pos()[0] <= 5+exit_display.get_width() and 145 <= pygame.mouse.get_pos()[1] <= 145+exit_display.get_height():
            exit_display_color = (255, 0, 0)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pause == 1:
                running = False
        else:
            exit_display_color = (0, 0, 0)

    if pause == 0:
        pygame.mouse.set_visible(False)
        pygame.mixer.music.unpause()
        if generate == release_token:
            image_picker = random.randint(0, token_picker)
            if token_picker // 2 <= image_picker <= token_picker:
                picture = 'personal_data.png'
            elif token_picker // 8 <= image_picker < token_picker // 2:
                picture = 'cop.png'
            elif 0 < image_picker < token_picker // 8:
                picture = judge
            elif image_picker == 0:
                picture = 'prison_bars.png'
            new_token = Token(random.randint(30, 610), picture)
            generate = 0

        if generate <= release_token:
            generate += 1
        else:
            while generate > release_token:
                generate -= 1

        if speedup_counter % speedup_point == 0 and speedup_counter != 0:
            if release_token > 1:
                release_token -= 1
                token_picker -= 1
            speedup_counter = 0
            speedup_point += 1

        screen.blit(background, (0, 0))
        score_display = pygame.font.SysFont('Bradley Hand ITC', 30).render('score: '+str(score), False, (0, 0, 0))
        level_display = pygame.font.SysFont('Bradley Hand ITC', 30).render('level '+str(61-release_token), False, (0, 0, 0))
        goal_display = pygame.font.SysFont('Bradley Hand ITC', 30).render('goal for next level: '+str(speedup_point-speedup_counter)+' personal files', False, (0, 0, 0))
        screen.blit(score_display, (5, 5))
        screen.blit(level_display, (5, 40))
        screen.blit(goal_display, (5, 75))
        player = screen.blit(Zuccy, (pygame.mouse.get_pos()[0] - 50, pygame.mouse.get_pos()[1] - 62))
        for item in Token.attribute_list:
            item.update()
        pygame.display.flip()
        clock.tick(clock_refresh)

    elif pause == 1:
        pygame.mouse.set_visible(True)
        pygame.mixer.music.pause()
        pause_display = pygame.font.SysFont('Bradley Hand ITC', 30).render('|| paused', False, (0, 0, 0))
        exit_display = pygame.font.SysFont('Bradley Hand ITC', 30).render('Exit', False, exit_display_color)
        screen.blit(pause_display, (5, 110))
        screen.blit(exit_display, (5, 145))
        pygame.display.flip()

    elif pause == 2:
        screen.blit(background, (0, 0))
        pygame.mouse.set_visible(True)
        pygame.mixer.music.pause()
        show_cursor = not show_cursor

        if show_cursor:
            command_text = '/' + command + '_'
        else:
            command_text = '/' + command

        for i in range(len(pygame.key.get_pressed())):
            if pygame.key.get_pressed()[i]:
                if i == 8:
                    command = command[:-1]
                elif i == 13:
                    if command == 'set_gamemode ussr':
                        gamemode = 'ussr'
                        background = pygame.image.load('ussr_background.png')
                        Zuccy = pygame.image.load('the_soviet_Zucc.png')
                        judge = 'stalin.png'
                        pygame.mixer.music.load('National Anthem of USSR.mp3')
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.pause()
                    if command == 'set_gamemode meretz':
                        gamemode = 'meretz'
                        background = pygame.image.load('meretz_background.png')
                        Zuccy = pygame.image.load('TaMarkZandberg.png')
                        judge = 'judge.png'
                        pygame.mixer.music.load("meretz_soundtrack.mp3")
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.pause()
                    if command == 'set_gamemode normal':
                        gamemode = 'normal'
                        background = pygame.image.load('background.png')
                        Zuccy = pygame.image.load('the_zucc.png')
                        judge = 'judge.png'
                        pygame.mixer.music.load('ZUCCY ZUCCY YES PAPA.mp3')
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.pause()
                    if command == 'get_gamemode':
                        print(gamemode)
                    if command == 'clear_scoreboard':
                        scoreboard_content = open('local_scoreboard.txt', 'w')
                        scoreboard_content.write('Beat Me!;50000')
                        scoreboard_content.close()
                    if command[:9] == 'set_level':
                        try:
                            release_token = 61 - int(command[-2:])
                            release_token = 61 - int(command[-2:])
                            speedup_point = int(command[-2:]) + 1
                            speedup_counter = 0
                        except ValueError:
                            release_token = 61 - int(command[-1])
                            release_token = 61 - int(command[-1])
                            speedup_point = int(command[-1]) + 1
                            speedup_counter = 0
                        except ValueError:
                            pass
                    if command[:9] == 'set_score':
                        try:
                            score = int(command[10:])
                        except ValueError:
                            pass
                    if command[:9] == 'add_score':
                        try:
                            score += int(command[10:])
                        except ValueError:
                            pass
                    pause = 0
                elif i == 47:
                    pass
                elif i != 301 and i != 304:
                    if pygame.key.get_pressed()[301] or pygame.key.get_pressed()[304]:
                        if i == 45:
                            command += chr(i + 50)
                        else:
                            command += chr(i).upper()
                    else:
                        command += chr(i).lower()
                time.sleep(0.1)

        command_display = pygame.font.SysFont('Bradley Hand ITC', 30).render(command_text, False, (255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), [4, 110, command_display.get_width()+13, 30])
        screen.blit(command_display, (5, 110))
        pygame.display.flip()


pygame.mixer.music.fadeout(1000)
running = True
show_cursor = True
pygame.mouse.set_visible(True)
player_name = ''
addition = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for i in range(len(pygame.key.get_pressed())):
        if pygame.key.get_pressed()[i]:
            if i == 8:
                player_name = player_name[:-1]
            elif i == 13:
                running = False
            elif i != 301 and i != 304:
                if pygame.key.get_pressed()[301] or pygame.key.get_pressed()[304]:
                    if i == 45:
                        player_name += chr(i + 50).upper()
                    else:
                        player_name += chr(i).upper()
                else:
                    player_name += chr(i).lower()
            time.sleep(0.1)

    if show_cursor:
        name_text = 'name: {}_'.format(player_name)
        show_cursor = False
        addition = pygame.font.SysFont('Bradley Hand ITC', 40).render('_', False, (0, 0, 0)).get_width() - 8

    else:
        name_text = 'name: {}'.format(player_name)
        show_cursor = True
        addition = 0

    screen.fill((200, 200, 200))
    name_display = pygame.font.SysFont('Bradley Hand ITC', 40).render(name_text, False, (0, 0, 0))
    screen.blit(name_display, (312 - (name_display.get_width() // 2) + addition, 550))
    pygame.display.flip()


def get_score(score_line):
    return int(score_line.split(';')[1])


if player_name != '':
    with open('local_scoreboard.txt', 'a') as scoreboard:
        scoreboard.write('{};{}\n'.format(player_name, score))
else:
    pass
with open('local_scoreboard.txt', 'r') as scoreboard:
    scoreboard_content = scoreboard.read().split('\n')
while '' in scoreboard_content:
    scoreboard_content.remove('')
scoreboard_content = sorted(scoreboard_content, key=get_score)[::-1]
screen.fill((200, 200, 200))
for i in range(len(scoreboard_content)):
    if i < 10:
        name_display = pygame.font.SysFont('Bradley Hand ITC', 40).render('{}. {}'.format(i + 1, scoreboard_content[i].split(';')[0]), False, (0, 0, 0))
        score_display = pygame.font.SysFont('Bradley Hand ITC', 40).render(scoreboard_content[i].split(';')[1], False, (0, 0, 0))
        screen.blit(name_display, (10, 100 + (45 * i)))
        screen.blit(score_display, (620 - score_display.get_width(), 100 + (45 * i)))
else:
    pass

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
