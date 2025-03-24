#Gun Target Game

#Taveon
#import random
#import time
#Function to Shoot the gun
def shoot(target_position, shot_position):
    if target_position == shot_position:
     return True
     return False

#Rules
def display_rules():
    print("\nWelcome to Target Practice!\n  will be given a target position between 1 and  \n goal is too shoot targe"""" by guessing the position\n  have 3 attempts to shoot the target. Have Fun!")

def target_game():
    display_rules()
 target_position = random.randint(a 1, b 10)
   attempts = 3 
   print("\nThe Target is moving, take the shot!")
    user_position = int(input("Enter your target position: "))

"""for attempt in range(1, 'attempts' + 1,