import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

curses.initscr()

MAX_COLS = 80
MAX_ROWS = 20
terminal_window = curses.newwin(MAX_ROWS, MAX_COLS, 5, 10)
terminal_window.keypad(1) # this would return special keys from terminal
curses.noecho() #don't print anything after enter
curses.curs_set(0) # remove blinking curser
terminal_window.nodelay(1) # make get character non blocking
greetings = " Congratulations  you are amazing !"
key = KEY_LEFT
score = 0

bird = [18, 2] # row no 18 , col no 2
bird_initial = [18, 2]
how_mny_fruits = 4
fruits_initail = list()
for x in range(int(how_mny_fruits/2)):
    for y in range(2):
        y_ = randint(5, 18)
        x_ = randint(5, 75)
        if x_ != bird[1] and y_ != bird[0]:
            fruits_initail.append([y_, x_])
terminal_window.addch(bird[0], bird[1], "R")      

while key != 27:
    terminal_window.border(0)
    terminal_window.addstr(0, 5, 'Score: ' + str(score) + ' ')
    terminal_window.addstr(0, 35, "Mini Flying bird game")
    terminal_window.timeout(200 -10*(how_mny_fruits - len(fruits_initail)))
    event = terminal_window.getch()
    prevKey = key
    key = key if event == -1 else event

    terminal_window.addch(bird[0], bird[1], " ")
    shifted_x = bird[1] + 1 if bird[1] + 1 < MAX_COLS else 1 
    shifted_y = bird[0] if bird[0] < bird[0] - 1>0 else 19
    terminal_window.addch(bird[0], shifted_x, "R")
    bird = [ bird[0], shifted_x]

    for fruit in fruits_initail:
        terminal_window.addch(fruit[0], fruit[1], "@")

    if key == KEY_UP:
        terminal_window.addch(bird[0], bird[1], " ")
        shifted_y = bird[0] - 1 if bird[0] - 1 > 0 else bird_initial[0]
        terminal_window.addch(shifted_y, bird[1], "R")
        bird = [shifted_y, bird[1]]

    if key == KEY_DOWN:
        terminal_window.addch(bird[0], bird[1], " ")
        shifted_y = bird[0] + 1 if bird[0] + 1 < MAX_ROWS else 1
        terminal_window.addch(shifted_y, bird[1], "R")
        bird = [shifted_y, bird[1]]

    fruit_eaten = [] # [ [y,x ], [y,x ] ]
    for fruit in fruits_initail:
        if ( bird[0] == fruit[0] and bird[1] == fruit[1]):
            score += 1
            terminal_window.addch(fruit[0], fruit[1], " ")
            fruit_eaten.append([fruit[0], fruit[1]])
            curses.beep()
    
    for eaten in fruit_eaten:
        fruits_initail.remove(eaten)

    if len(fruits_initail) == 0:
        terminal_window.addnstr(int(MAX_ROWS/2), int(MAX_COLS/2), "Congratulations you won !!")

curses.endwin()    

# addnstr




