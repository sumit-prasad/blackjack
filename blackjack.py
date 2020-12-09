import random
import art
import os
from termcolor import colored


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_line():
    print(colored(
        "----------------------------------------------------------------------",
        "white"),
          flush=True)


def deal_card():
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card_list)


def calc_score(hand):
    if len(hand) == 2 and sum(hand) == 21:
        return 21
    if 11 in hand and sum(hand) > 21:
        index = hand.index(11)
        hand[index] = 1
    return sum(hand)


def bust(score):
    if score > 21:
        return True
    else:
        return False


def print_result(player, hand, score):
    print_line()
    if player == "Your":
        print(colored("\t\t\t\tYou are the winner!!", "green", attrs=["bold"]))
    else:
        print(
            colored(f"\t\t\t\t{player} is the winner!",
                    "green",
                    attrs=["bold"]))
    print(f"\t\t\t\tFinal hand: {hand} | Score: {score}")
    print_line()
    return True


def choice():
    choice = input(
        colored(
            "Do you want to play the game of Blackjack again? Type 'y' or 'n': ",
            "red",
            attrs=["bold"]).center(40)).lower()[0]
    return choice


def blackjack(start, game_over):
    while start == "y":
        clear()
        # Hand for user and computer
        user_hand = []
        computer_hand = []

        # Print blackjack art
        print(colored(art.logo, "white", "on_red", attrs=["bold"]).center(40))
        print_line()
        # Initial Two cards for the start of the game
        for i in range(0, 2):
            user_hand.append(deal_card())
            computer_hand.append(deal_card())

        # Calculate the initial score of the each hand
        user_score = calc_score(user_hand)
        bot_score = calc_score(computer_hand)

        # Print the initial score for both players while hiding one card of the computer player
        print(f"\t\t\t\tYour cards: {user_hand} | Current Score: {user_score}")
        print(f"\n\t\t\t\tComputer's cards: {computer_hand[0]} -")
        print_line()
        # Check for blackjack for both players
        if user_score == 21:
            game_over = print_result("Your", user_hand, user_score)
        elif bot_score == 21:
            game_over = print_result("Computer", computer_hand, bot_score)

        # Loop for the drawing of the card and actual gameplay
        while not game_over:
            # Check for bust (score > 21) for both players
            if bust(user_score):
                game_over = print_result("Computer", computer_hand, bot_score)
            elif bust(bot_score):
                game_over = print_result("Your", user_hand, user_score)

            # If user has less than 21, ask whether to draw a card or pass drawing
            elif user_score < 21:
                print_line()
                next = input(
                    "\t\tType 'h' to HIT (get another card), type 's' to STAND: "
                )

                # Draw another card and add it to the list and update new score
                if next == "h":
                    user_hand.append(deal_card())
                    user_score = calc_score(user_hand)
                    print(
                        f"\t\tYour cards: {user_hand} | Current Score: {user_score}"
                    )

                # User passes to draw another card
                elif next == "s":
                    # Loop through different exception between the score of user and computer
                    while not game_over:
                        # # Draw scenario
                        if bot_score == user_score:
                            # Score less than 14 then draw another card and update the bot score
                            if bot_score < 14:
                                computer_hand.append(deal_card())
                                bot_score = calc_score(computer_hand)
                                print(
                                    f"\t\tComputer's cards: {computer_hand} | Computer Score: {bot_score}"
                                )
                            # Declare draw and end current game.
                            else:
                                print(
                                    colored(
                                        "\t\tGame Draw. Luck is spontaneous.",
                                        "yellow",
                                        attrs=["bold"]))
                                print(
                                    f"\t\tYour score: {user_score} | Computer's score: {bot_score}"
                                )
                                print_line()
                                game_over = True
                        # # Bot scores less, draw another card and update score and loop again
                        elif bot_score < user_score:
                            computer_hand.append(deal_card())
                            bot_score = calc_score(computer_hand)
                            print(
                                f"\t\tComputer's cards: {computer_hand} | Computer Score: {bot_score}"
                            )
                        # # Bot scores more than user and is less than 21, bot wins. update game_over to True
                        elif bot_score > user_score and bot_score <= 21:
                            game_over = print_result("Computer", computer_hand,
                                                     bot_score)
                        # # Bot scores more than 21, print result and update game_over to True
                        else:
                            game_over = print_result("Your", user_hand,
                                                     user_score)
                # Invalid choice by user. Declare bot as winner
                else:
                    print("Wrong choice. You lost")
                    print_result("Computer", computer_hand, bot_score)
            elif user_score == 21:
                game_over = print_result("Your", user_hand, user_score)
        # Choice for another round
        ch = choice()
        # Check if choice is either 'y' or 'no' and continue asking for choice if invalid choice
        while ch not in ["y", "n"]:
            print("Wrong Input. Try Again.")
            ch = choice()
            clear()
        # End the program
        if ch == "n":
            clear()
            break
        # Reset game over to false
        game_over = False


# # Start of the program
blackjack("y", False)
