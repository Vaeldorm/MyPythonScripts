import random
import logging
import os

# Get the directory of the current script file
script_dir = os.path.dirname(__file__)

# Configure Logging
log_file = os.path.join(script_dir, 'goodmorning_user_input.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

def get_goals():
    goals = []
    while True:
        goal = input("Goal for the day: ")
        if goal.lower() == 'q' or goal.lower() == 'quit':
            break
        goals.append(goal)
        print('Saved.')
        logging.info(f"User input: {goal}")
    return goals


def print_goals(goal_list):
    x = 1
    print('Stay focused! Here are your goals for the day.')
    for goal in goal_list:
        print(f"{x}. {goal}")
        x += 1


def greeting(list):
    print(inspirational_quotes[x])
    print()
    print('Today is a new day.')
    print()


inspirational_quotes = [
    '"If you\'re going through hell, keep going." -Winston Churchill',
    '"More is lost by indecision than wrong decision" -The Sopranos',
    '"A ship is safe in harbor, but that\'s not what ships are for." -William Shedd',
    '"The reason we struggle with insecurity is because we compare our behind-the-scenes with everyone else\'s highlight reel." -Steve Furtick'
]

x = random.randint(0,(len(inspirational_quotes)-1))

greeting(inspirational_quotes)
todays_goals = get_goals()
print()
print_goals(todays_goals)
