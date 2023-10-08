import re
import pygame
pygame.init()

# replace one of examples with your text
# string examples
ex1 = "Metro - kolej przeznaczona do transportu pasażerów, o zdolności przepustowej umożliwiającej obsługę ruchu o dużym nasileniu oraz charakteryzująca się wyłącznymi prawami drogi, wielowagonowymi pociągami, dużą prędkością i dużym przyspieszeniem, złożonym systemem sygnalizacji, jak również brakiem skrzyżowań jednopoziomowych, w celu umożliwienia wysokiej częstotliwości jazdy pociągów oraz dużego obciążenia."
ex2 = "Poczuł  ogrom przyrody, grozę jej nieubłaganych praw, wielkość jej i obojętność. Obojętność jej wobec jego małej śmierci wstrząsnęła nim. Zimo mu się zrobiło w tym upale, włosy stanęły dęba, śmierć trawi go powoli, a przyroda nic, nic, nic nie zrobi, aby to odmienić - przypatruje się jego zgonowi, obojętna. Jakież miliardy umarły tak samo młodo."
ex3 = "ffffff d           ffffffffff fffffffff ffffffffff d ffff fff g fffffffff ggggggggggggggggggggggggggggggggggggggf"

# choose text
check = ex3
string = ""

# select just letters
for letter in check:
    if letter.isalpha() or letter.isnumeric() or letter == " ":
        string += letter

# clear exceeding spaces
string = re.sub(r'\s+', ' ', string)

# list of letters and colors - add new if you need more
colors = {
    "a": (255, 255, 255),
    "b": (204, 255, 255),
    "c": (102, 204, 255),
    "d": (0, 153, 255),
    "e": (0, 102, 204),
    "f": (0, 0, 153),
    "g": (102, 0, 102),
    "h": (153, 0, 153),
    "i": (255, 0, 102),
    "j": (255, 80, 80),
    "k": (255, 153, 102),
    "l": (255, 102, 0),
    "m": (255, 51, 0),
    "n": (204, 51, 0),
    "o": (102, 51, 0),
    "p": (153, 102, 51),
    "r": (255, 153, 0),
    "s": (204, 153, 0),
    "t": (153, 204, 0),
    "u": (0, 153, 0),
    "w": (0, 51, 0),
    "y": (51, 153, 51),
    "z": (102, 153, 153),
    "ą": (128, 0, 0),
    "ć": (204, 51, 0),
    "ę": (128, 0, 0),
    "ł": (153, 0, 51),
    "ń": (153, 51, 51),
    "ó": (0, 102, 102),
    "ś": (102, 102, 51),
    "ź": (255, 80, 80),
    "ż": (51, 51, 204), }

# character size
width = 10
height = width * 2

# character position
new_line = 00
x, y = new_line, height

# window res
wn_width = 1000

# window size check
iteration = 0
for letter in string:
    x += width * 2
    change = False
    if letter == " ":
        next_space = string.find(" ", iteration + 1) - iteration - 1
        if next_space < 0:
            next_space = len(string) - iteration - 1
        pos = x + next_space * width * 2
        if pos >= wn_width:
            x = new_line
            y += height * 2
            change = True
        else:
            change = True
    else:
        for entry, color in colors.items():
            if letter.lower() == entry:
                change = True
    if not(change):
        x += width
        change = False
    iteration += 1

# new window res
wn_height = y + height * 2
wn_width_new = wn_width + 10
res = (wn_width_new, wn_height)

# window
wn = pygame.display.set_mode(res)
pygame.display.set_caption("ColorCrypt")
pygame.draw.rect(wn, (150, 150, 150), (0, -5, wn_width_new, wn_height + 5), 5)
# wn.fill((30, 30, 30))   # uncomment if you want RGB_here background

# position reset
x, y = new_line, height

'''
# validation block - start
x = new_line + height
pygame.draw.rect(wn, (0, 230, 0), (x, y, width * 6, height))
pygame.draw.rect(wn, (0, 0, 0), (x + width, y + height / 4, width * 4, height / 2))
x += height * 3
'''

# main loop
iteration = 0
for letter in string:

    # move between letters
    x += width * 2
    change = False

    # new line - only when space is reached
    if letter == " ":

        next_space = string.find(" ", iteration + 1) - iteration - 1
        if next_space < 0:
            next_space = len(string) - iteration - 1

        pos = x + next_space * width * 2
        if pos >= wn_width:
            x = new_line
            y += height * 2
            change = True

        else:
            change = True

    else:
        for entry, color in colors.items():
            if letter.lower() == entry:
                pygame.draw.rect(wn, color, (x, y, width, height))
                change = True

    # other than letters will be printed as circle
    if not(change):
        x += width
        y += width
        pygame.draw.circle(wn, (255, 0, 0), (x, y), width)
        pygame.draw.circle(wn, (255, 255, 255), (x, y), int(width/1.5))
        y -= width
        change = False

    pygame.display.update()
    iteration += 1

'''
# validation block - end
x += width * 3
pygame.draw.rect(wn, (255, 0, 0), (x, y, width * 6, height))
pygame.draw.rect(wn, (0, 0, 0), (x + width, y + height / 4, width * 4, height / 2))
pygame.display.update()
'''

# sleep loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
