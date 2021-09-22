import random
import time

# Welcome & Rules of the game

print('Hello! This is simple homeless simulator')
gamers_name = input('Just enter your name to start the game: ')
input(f'Hello, {gamers_name}! To continue press "Enter"')
input('You have 3 indicators: health, money and fatigue')
input('Each of the indicators has a scale from 0 to 100')
input('If one of the indicators reaches 0, you will lose')
input('Each turn you can do one of three actions: sleep, work or eat')
input('All actions affect your characteristics')
print('Type here what you want to do: work, sleep or eat')


# Do something

class Do:
    def __init__(self):
        self.health = 100
        self.money = 100
        self.fatigue = 100

    def if_maximum_points(self):
        if self.health > 100:
            self.health = 100
        if self.fatigue > 100:
            self.fatigue = 100

    def lose_conditions(self):
        if self.fatigue <= 0 or self.health <= 0 or self.money <= 0:
            print('You lose. Game over!')
            print(f'You lived for {count} days')
            global game
            game = False

    def work(self):
        self.health -= 5
        self.money += 10
        self.fatigue -= 5
        print('You worked')

    def sleep(self):
        self.health -= 5
        self.money -= 10
        self.fatigue += 15
        print('You slept')

    def eat(self):
        self.health += 15
        self.money -= 15
        self.fatigue -= 5
        print('You ate')

    def random_event_drop_health(self):
        self.random_events = ['Oh, shit! You were beaten by the police. Your health dropped',
                              'You have been poisoned by food. Your health dropped',
                              'Oh shit! You got beat up by teenagers. Your health dropped']
        self.event = random.choice(self.random_events)
        self.chance = random.randint(1, 10)
        if self.chance == 1:
            self.health -= 20
            print(self.event)

    def get_status(self):
        print(f'Health: {self.health}, Money: {self.money}, Fatigue: {self.fatigue}')


count = 0
game = True
character = Do()

while game:
    turn = input('What do we do: ')
    if turn.lower() == 'work':
        character.work()
        character.if_maximum_points()
        character.lose_conditions()
        character.random_event_drop_health()
        count += 1

    if turn.lower() == 'sleep':
        character.sleep()
        character.if_maximum_points()
        character.lose_conditions()
        character.random_event_drop_health()
        count += 1

    if turn.lower() == 'eat':
        character.eat()
        character.if_maximum_points()
        character.lose_conditions()
        character.random_event_drop_health()
        count += 1

    if turn.lower() == 'status':
        character.get_status()

    if turn.lower() == 'stop':
        print('Game over')
        print(f'You lived for {count} days')
        game = False
