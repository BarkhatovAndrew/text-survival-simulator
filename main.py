import random

# Welcome & Rules of the game

print('Hello! This is simple homeless simulator')
name = input('Just enter your name to start the game: ')
input(f'Hello, {name}! To continue press "Enter"')
input('You have 3 indicators: health, money and fatigue')
input('Fatigue and health have a scale from 0 to 100. The amount of money is unlimited')
input('If one of the indicators reaches 0, you will lose')
input('Each turn you can do one of three actions: sleep, begg or eat')
input('All actions affect your characteristics')
input('"Begg" increases the amount of money, "Sleep" reduces fatigue and "Eat" heals you')
input('Sometimes it can happen random events that will affect you')
input('You can also write "Status" to find out your characteristics')
input('Now you can start the game. Press Enter to start')
print('Type here what you want to do: beg, sleep, eat, shop or status')
print('-----------------------------------------------------------')


# Do something

class Do:
    game = True
    day_count = 0

    def __init__(self):
        self.health = 100
        self.money = 100
        self.fatigue = 100

    def if_maximum_points(self):
        if self.health > 100:
            self.health = 100
        if self.fatigue > 100:
            self.fatigue = 100

    def lose(self):
        print('You lose. Game over!')
        print(f'You lived for {self.day_count} days')
        self.game = False

    def lose_conditions(self):
        if self.fatigue <= 0 or self.health <= 0 or self.money <= 0:
            self.lose()

    def win_conditions(self):
        if self.money >= 1000:
            print('You win!')
            print(f'You lived for {self.day_count} days')
            self.game = False

    # Begging

    def begg(self):
        self.health -= 5
        self.fatigue -= 5 - buyer.hat
        self.chance = random.randint(1, 10)
        if self.chance == 1:
            self.chance = random.randint(20, 50)
            print(f"Wow! It's a nice day today! You earned an extra {self.chance}$")
            self.money += self.chance
        else:
            self.money += 10
            print('You earned 10$')

    # Sleep

    def sleep(self):
        self.health -= 5
        self.money -= 5
        self.fatigue += 15
        print('You slept')

    # Eat

    def eat(self):
        self.health += 15
        self.money -= 15
        self.fatigue -= 5
        print('You ate')

    # Random events, drop your health

    def random_event_drop_health(self):
        self.random_events = ['Oh, shit! You were beaten by the police. Your health dropped',
                              'You have been poisoned by food. Your health dropped',
                              'Oh shit! You got beat up by teenagers. Your health dropped']
        self.event = random.choice(self.random_events)
        self.chance = random.randint(1, 10)
        if self.chance == 1:
            self.health -= 20
            print(self.event)

    # Character Status

    def get_status(self):
        print(f'Health: {self.health}, Money: {self.money}$, Fatigue: {self.fatigue}')


class Shop:
    def __init__(self):
        self.hat = 0
        self.stimulator = 0
        self.stimulator_count = 10

    # Hat

    def if_already_have(self):
        if self.hat == 3:
            print('You already have a hat')

    def buy_hat(self):
        if character.money >= 31:
            character.money -= 30
            self.hat = 3
            print('Now you get tired less when begging')
        else:
            print('You have no money')

    # Stimulator

    def buy_stimulator(self):
        if character.money >= 31:
            character.money -= 30
            self.stimulator += 1
            print(
                'You will not get tired and want to eat for 10 days, but after health and fatigue will decrease by 40')
        else:
            print('You have no money')

    # Overdose

    def overdose(self):
        if self.stimulator == 2:
            print('You used a stimulant until the effect of the previous one passed. You have died of an overdose.')
            character.lose()

    # 10 Stimulator's Days

    def is_stimulator_end(self):
        if self.stimulator == 1:
            if self.stimulator_count != 0:
                self.stimulator_count -= 1
            else:
                character.health -= 40
                character.fatigue -= 40
                self.stimulator = 0
                self.stimulator_count = 10

    # Game initialization


character = Do()
buyer = Shop()


# Regular things every turn

def regular_things():
    character.if_maximum_points()
    character.lose_conditions()
    character.random_event_drop_health()
    buyer.is_stimulator_end()
    buyer.overdose()
    character.win_conditions()
    character.day_count += 1

    # Game start


character.get_status()

while character.game:
    turn = input('What do we do: ')

    # Begging Turn

    if turn.lower() == 'begg':
        character.begg()
        regular_things()

    # Sleeping Turn

    if turn.lower() == 'sleep':
        character.sleep()
        regular_things()

    # Eating Turn

    if turn.lower() == 'eat':
        character.eat()
        regular_things()

    # Shopping Turn

    if turn.lower() == 'shop':
        print('Hat - 30$, Stimulator - 30$')
        buy = input('What do you want to buy: ')
        if buy.lower() == 'hat':
            if buyer.hat == 0:
                buyer.buy_hat()
            else:
                buyer.if_already_have()

        if buy.lower() == 'stimulator':
            buyer.buy_stimulator()

    # Status Turn

    if turn.lower() in ['status', 'stat']:
        character.get_status()

    # End Game, when type stop

    if turn.lower() == 'stop':
        character.lose()
