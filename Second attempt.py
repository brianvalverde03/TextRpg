import sys
import os
import random
import pickle
import time

screen_width = 100

# player #
class player:
    def __init__(self):
        self.attack_power = 0
        self.damage = 20 * (self.attack_power + 3)
        self.vitality = 10
        self.health = 320
        self.status_effects = []
        self.location = 'c1'
        self.game_over = False
        self.bosses_beat = 0

player1 = player

#############
# map setup #
#############

# 8x8 flat plane with 8 sections #

zone_map = {#complete this later on#
}

class mobs:
    def enemy_gen():
        if player1.location in ['a1', 'b1', 'b2', 'c2', 'd2']:
            chance = random.randint(1, 101)
            if chance in range(96, 101):
                name = 'Ashina Soilder'
                hp = random.randint(100, 150)
                atk = random.randint(10, 20)
                defence = random.randint(5, 10)

                return Enemy(hp, atk, defence, name)
        elif player1.location in ['e1', 'e2', 'f2', 'g1', 'g2', 'h1', 'h2']:
            chance = random.randint(1, 101)
            if chance in range(96, 101):
                name = 'Spear Adept'
                hp = random.randint(100, 200)
                atk = random.randint(10, 20)
                defence = random.randint(5, 10)

                return Enemy(hp, atk, defence, name)
        elif player1.location in ['a4', 'b3', 'b4', 'c3', 'c4', 'd3']:
            chance = random.randint(1, 101)
            if chance in range(96, 101):
                name = 'Nightjar Ninja'
                hp = random.randint(100, 200)
                atk = random.randint(10, 20)
                defence = random.randint(5, 10)

                return Enemy(hp, atk, defence, name)
        elif player1.location in ['e3', 'e4', 'f3', 'g3', 'h3', 'h4']:
            chance = random.randint(1, 101)
            if chance in range(96, 101):
                name = 'Sunken Valley Clan'
                hp = random.randint(100, 200)
                atk = random.randint(10, 20)
                defence = random.randint(5, 10)

                return Enemy(hp, atk, defence, name)
        elif player1.location in ['a6', 'b5', 'b6', 'c5', 'c6', 'd5', 'd6']:
            chance = random.randint(1, 101)
            if chance in range(96, 101):
                name = 'Hammer Monk'
                hp = random.randint(100, 200)
                atk = random.randint(10, 20)
                defence = random.randint(5, 10)

                return Enemy(hp, atk, defence, name)
        elif player1.location in ['a7', 'a8', 'b7', 'c7', 'c8', 'd7', 'd8']:
            chance = random.randint(1, 101)
            if chance in range(96, 101):
                name = 'Red Guard'
                hp = random.randint(100, 200)
                atk = random.randint(10, 20)
                defence = random.randint(5, 10)

                return Enemy(hp, atk, defence, name)
        elif player1.location in ['e5', 'e6', 'f5', 'g5', 'g6', 'h5', 'h6']:
            chance = random.randint(1, 101)
            if chance in range(96, 101):
                name = 'Mibu Villager'
                hp = random.randint(100, 200)
                atk = random.randint(10, 20)
                defence = random.randint(5, 10)

                return Enemy(hp, atk, defence, name)
        elif player1.location in['e7', 'e8', 'f7', 'f8', 'g7', 'g8', 'h8']:
            chance = random.randint(1, 101)
            if chance in range(96, 101):
                name = 'Okami Warrior'
                hp = random.randint(100, 200)
                atk = random.randint(10, 20)
                defence = random.randint(5, 10)

                return Enemy(hp, atk, defence, name)

class Enemy:
    def __init__(self, hp, atk, defence, name,):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.defence = defence

class Bosses:
    def enemy_gen():
        if player1.location in ['a2']:
            print('You see a giant menacing snake.',
                  'You understand that if you make one more move that you will die.')
            move(myAction)
        elif player1.location in ['a3']:
            print('You see a giant menacing snake.',
                  'You see that you have the opportunity to kill it.',
                  'Will you kill it or run?')
            option = input('> ')
            if option.lower() in ['kill it', 'kill']:
                print('You jump from the cliff that you are and stab the snake in the head',
                      'The snake starts shaking in agony.',
                      'You the snake falls to the ground. You have killed it')
                player1.bosses_beat = +1
            elif option.lower() in ['run', 'run away']:
                print('You tread safley away from the snake so that you can see another day.')
                move(myAction)
        elif player1.location in ['b8']:
            print('You find your father, Owl.')
            print('Your father wants you to stop helping the prince and join his side again')
            print('Will go against the prince or will keep protecting the prince')
            option = input('> ')
            if option.lower in ['go against the prince', '1', 'against']:
                print('You have decided to go against the prince')
                print('Bad ending')
                sys.exit()
            if option.lower in ['protect', '2', 'keep protecting the prince']:
                print('You have decided to go against your father')
                print('Your father has gone into his stance to fight')
                print('GET READY!')

                name = 'Owl'
                hp = 750
                atk = 35
                defence = 25

                return Enemy(hp, atk, defence, name)
        elif player1.location in ['f4']:
            print('You see a giant ape with a sword in his neck guarding something.\n',
                  'Do you approach the ape or run away?')
            option = input('> ')
            if option.lower in ['yes', 'approach', '1']:
                print('You approach the ape and he senses your presence.\n',
                      'He is ready to fight. GET READY!')
                name = 'Guardian Ape'
                hp = 750
                atk = 35
                defence = 25

                return Enemy(hp, atk, defence, name)
        elif player1.location in ['f6']:
            print('You stumble upon a semi-translucent figure.\n',
                  "It's a ghost monk with a ominous feeling.\n",
                  'He comes running towards giving you no other option but to fight.')
            name = 'Corrupted Monk'
            hp = 750
            atk = 35
            defence = 25

            return Enemy(hp, atk, defence, name)
        elif player1.location in ['h7']:
            print('You stand before a dragon that hundreds of times your size\n',
                  'Your only option is to fight.')
            name = 'Divine Dragon'
            hp = 750
            atk = 35
            defence = 25

            return Enemy(hp, atk, defence, name)
        elif player1.bosses_beat == 6 and player1.location in ['d4']:
            print('You see your final enemy.\n',
                  'Sword Saint Isshin.')
            name = 'Sword Saint Isshin'
            hp = 750
            atk = 35
            defence = 25

            return Enemy(hp, atk, defence, name)

def enemy_gen1():
    en1 = Mobs.enemy_gen(Enemy)
    print('You have encountered {}'.format(en1.name))
    input('> ')
    fight(en1)

def fight():
    os.system('cls')

def events():
    pass

def inventory():
    pass

def game_menu():
    #print_map_town()
    print('Player Stats')
    print('Health: {}\{}'.format(player.base_hp, character.hp_max))
    print('Attack: {}'.format(player1.damage))
    print('Defense: {}'.format(player1.defense))
    print('Current Location: {}'.format(player1.location))
    print('-----------------------------')
    print('1.) Examine your surroundings')
    print('2.) Teleport')
    print('3.) Save')
    print('4.) Back')
    print('5.) Exit')
    option = input('> ')
    if option == '1':
        examine()
    elif option == '2':
        teleport()
    elif option == '3':
        save()
    elif option == '4':
        move()
    elif option == '5':
        exit_check()

def save():
    if os.path.exists('save_file'):
        print('Are you sure that you want to overwrite your current save? Y/N')
        option = input('> ')
        if option.lower() == 'y':
            with open('save_file', 'wb') as f:
                pickle.dump(player1, f)
                print('Game has been saved.')
        else:
            print("Game hasn't been saved.")
    else:
        with open('save_file', 'wb') as f:
            pickle.dump(player1, f)
            ('Game has been saved.')
    input('> ')
    game_menu()

def auto_save():
    with open('save_file', 'wb') as f:
        pickle.dump(player1, f)

def exit_check():
    os.system('cls')
    print("Are you sure that you want to exit? Make sure that you have saved your game first. Y/N")
    decision = input('> ')
    if decision.lower() == 'y':
        sys.exit()
    else:
        game_menu()

def teleport():
    os.system('cls')
    if player1.location == 'd1':
        if player1.d1_event_1:
            print('You finally meet up with the prince and he tells you to explore the world.\n',
                  "With all the items in the world the curse of the dragon's blood")
            print('You can now teleport back to the prince')
            input('> ')
            event_check()
    if player1.location == 'f2':
        if player1.f2_event_1:
            print('You find a monk in the temple.\n',
                  "He doesn't say a word, just holds out a scroll")

def print_map():
    pass


def title_screen_selection():
    os.system('cls')
    option = input('> ')
    if option.lower() == ('play'):
        start_game()
    elif option.lower() == ('help'):
        help_menu()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print ('Please enter a valid command.')
        option = input('> ')
        if option.lower() == ('play'):
            start_game()
        elif option.lower() == ('help'):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()

def title_screen():
    os.system('cls')
    print('*' * 31)
    print('* Welcome to the text-based RPG')
    print('*    Made by Brian Valverde   *')
    print('*' * 31)
    print('           :Play:              ')
    print('           :Help:              ')
    print('           :Quit:              ')
    title_screen_selection()

def help_menu():
    os.system('cls')
    print('')
    print('*' * 45)
    print('Created by Brian Valverde')
    print('#' * 45)
    print('To move around type commands such as\n'
          '"move" then "left".\n')
    print('To interact with the world type commands\n'
          'such as "look" or "examine".\n')
    print('To beat the game you will need to collect\n'
          'the items around the world and from the bosses.\n')
    print('*' * 31)
    print('\n')
    print('Please select one of the options to continue')
    print('*' * 31)
    print('                  :Play:                    ')
    print('                  :Help:                    ')
    print('                  :Quit:                    ')
    title_screen_selection()

# handeling the game #
quitgame = 'quit'

def print_locatoin():
    os.system('cls')
    print('\n' + ('*' * (4 + len(player1.location))))
    print('*' + player1.location.upper() + '*')
    print('*' * (4 + len(player1.location)))
    print('\n' + (zone_map[player1.location][DESCRIPTION]))

def prompt():
    os.system('cls')
    #pass#
    if player1.bosses_beat == 6:
        print('Something in the world has changed.....')
    print('\n-------------------------')
    print('What would you like to do?')
    action = input('> ')
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'inspect', 'examine', 'look', 'search']
    while action.lower() not in acceptable_actions:
        print("Unknown action command, please try again.\n")
        action = input("> ")
    if action.lower() == quitgame:
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        move(action.lower())
    elif action.lower() in ['inspect', 'examine', 'look', 'search']:
        examine()

def move(myAction):
    os.system('cls')
    option = str(input(print('Where would you like to move to.\n',
                             'Enter M for the menu.')))
    if option == 'forward':
        move_dest = zone_map[player1.location][SIDE_UP]  # if you are on ground, should say north
        move_player(move_dest)
    elif option == 'left':
        move_dest = zone_map[player1.location][SIDE_LEFT]
        move_player(move_dest)
    elif option == 'right':
        move_dest = zone_map[player1.location][SIDE_RIGHT]
        move_player(move_dest)
    elif option == 'back':
        move_dest = zone_map[player1.location][SIDE_DOWN]
        move_player(move_dest)
    elif option.lower() == 'm':
        game_menu()
    else:
        print("Invalid direction command, try using forward, back, left, or right.\n")
        move(myAction)

def move_player(move_dest):
    os.system('cls')
    print('\nYou have moved to the ' + move_dest + '.')
    player1.location = move_dest
    print_location()


def main_game_loop():
    total_bosses = 8
    while player1.won is False:
        prompt()

def intro():
    os.system('cls')
    print('Welcome to the game\n')
    print('This is where your adventure begins\n')
    print('You are the samurai in the edo period of Japan and ')

def fight():
    pass


def start_game():
    print("hello there")
    move()


title_screen()
