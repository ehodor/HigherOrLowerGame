# Created by Emma Hodor on 1/4/2023
# GameData and art files created by @angelabauer

import GameData
import random
import art

print(art.logo)


def game():
    score = 0

    def rerun():
        while True:
            replay = input("Would you like to play again? Type 'y' or 'n': ")
            if replay == 'y':
                game()
            elif replay == 'n':
                quit()
            else:
                print('Please type in valid input.\n')

    print("Welcome to the Higher or Lower Game! Here you will be guessing who of the two options you are given has "
          "more Instagram followers! Please type 'A' or 'B' to make your choice!")
    first_option = None
    while True:
        print(f'Score: {score}')
        if first_option is None:
            first_option = random.choice(GameData.data)
        print(
            f'Compare choice A, {first_option["name"]}, a {first_option["description"]} from {first_option["country"]}')
        print(art.vs)
        second_option = random.choice([x for x in GameData.data if x != first_option])
        print(f'Vs choice B, {second_option["name"]}, a {second_option["description"]} from {second_option["country"]}')
        while True:
            AorB = input("Who do you think has more followers? Type 'A' or 'B': ")
            if AorB == 'A' or AorB == 'a':
                AorB = first_option
                break
            elif AorB == 'B' or AorB == 'b':
                AorB = second_option
                break
            else:
                print('Please type in valid input.\n')

        if first_option['follower_count'] > second_option['follower_count']:
            winner = first_option
        else:
            winner = second_option
        if winner == first_option:
            if AorB == first_option:
                print('Correct! Score increased by 1.\n')
                score += 1
            else:
                print(f'Sorry, that was incorrect. Final score is {score}')
                break
        elif winner == second_option:
            if AorB == second_option:
                print('Correct! Score increased by 1.\n')
                score += 1
                first_option = AorB
            else:
                print(f'Sorry, that was incorrect. FInal score is {score}')
                break

    rerun()


game()
