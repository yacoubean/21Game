from random import randrange


def explain_game():
    print("Welcome to 21 Game\n")
    print("You will play against the computer.")
    print("You will take turns picking a number from 1 to 3.\n"
          "The game starts at 0. Each number played is added\n"
          "to the game total. The first player to bring the\n"
          "game total to exactly 21 wins!\n")


def begin_game(self):
    # randomly pick from 0 to 1 to decide who goes first
    dice_roll = randrange(2)
    if dice_roll == 0:
        start_player = 'The computer'
    else:
        start_player = 'You'

    self.first_player = dice_roll

    print("{0} will be the first player \n".format(start_player))

    self.game_total = 0

    take_turn(self)


def choose_difficulty():
    print("What game difficulty do you want?\n")
    print("(1) Easy")
    print("(2) Medium")
    print("(3) Hard")
    return input("")


def take_turn(self):
    if self.first_player == 0:  # computer is first player
        if (self.game_total > 17) & (self.game_difficulty == 3):
            # computer is going to win because we're in hard mode, calculate winning num
            comp_play = 21 - self.game_total
            print("The computer played {0} ".format(comp_play))
            self.game_total = 21
            print("Game total: {0}".format(self.game_total))
            self.computer_won = True
        else:
            comp_play = comp_strategy(self.game_total, self.game_difficulty)
            print("The computer played {0} ".format(comp_play))
            self.game_total += comp_play
            print("Game total: {0}".format(self.game_total))
            player_play = input("Play a number: ")
            self.game_total = verify_num_played(self.game_total, player_play)
            print("Game total: {0}".format(self.game_total))
    else:  # player goes first
        player_play = input("Play a number: ")
        self.game_total = verify_num_played(self.game_total, player_play)
        print("Game total: {0}".format(self.game_total))
        if self.game_total == 21:
            # player won, exit so game can end
            return
        elif (self.game_total > 17) & (self.game_difficulty == 3):
            # computer is going to win, calculate winning num and end game
            comp_play = 21 - self.game_total
            print("The computer played {0} ".format(comp_play))
            self.game_total = 21
            print("Game total: {0}".format(self.game_total))
            self.computer_won = True
        else:
            comp_play = comp_strategy(self.game_total, self.game_difficulty)
            print("The computer played {0} ".format(comp_play))
            self.game_total += comp_play
            print("Game total: {0}".format(self.game_total))


def verify_num_played(game_total, num):
    num_valid = 0
    while num_valid == 0:
        try:
            num = int(num)
        except ValueError:
            num = input("Please choose a number between 1 and 3: ")
        else:
            num_valid = 1

    while (num > 3 or num < 1) or (game_total+num > 21):
        if num > 3 or num < 1:
            num = int(input("Please choose a number between 1 and 3: "))

        if game_total+num > 21:
            num = int(input("You can't play above 21. Choose a different number: "))

    game_total += num
    return int(game_total)


def comp_strategy(game_total, game_difficulty):
    comp_play = 0
    if game_difficulty == 1:  # Easy difficulty, no strategy just randomly pick a number
        comp_play = randrange(1,4)
        if comp_play + game_total > 21:  # make sure the computer doesn't play over 21
            comp_play = 21 - game_total
    elif game_difficulty == 2:  # Medium difficulty
        # randomly pick a luck factor between 1 and 2
        luck_factor = randrange(1, 3)
        if luck_factor == 1:
            # if 1 we're going easy. just randomly pick number
            comp_play = randrange(1, 4)
            if comp_play + game_total > 21:  # make sure the computer doesn't play over 21
                comp_play = 21 - game_total
        else:
            # for medium difficulty, 50% of the time use the hard strategy
            comp_play = hard_comp_strategy(game_total)
    else:  # Hard difficulty
        comp_play = hard_comp_strategy(game_total)

    return comp_play


def hard_comp_strategy(game_total):
    comp_play = 0
    if 13 < game_total < 17:
        # if game_total is 17 the computer's next play will put the total close
        # to 21, but it can't reach 21, so the other player can win. so we don't
        # want to give them a 17
        comp_play = 17 - game_total
    elif 9 < game_total < 13:
        # if game_total is 14, the other player can force a 17, so we want to
        # land on 13 instead of 14
        comp_play = 13 - game_total
    elif 5 < game_total < 9:
        # if game_total is 10, the other player can force a 13, so we want to
        # land on 9 instead of 10
        comp_play = 9 - game_total
    elif 1 < game_total < 5:
        # if game_total is 6, the other player can force a 10, so we want to
        # land on 5 instead of 6
        comp_play = 5 - game_total
    else:
        comp_play = 1

    return comp_play


def game_over(self):
    if self.computer_won:
        print("The computer won. :(")
    else:
        print("You won!")
    print("\n")


def play_again(self):
    play_yes_no = input("Do you want to play again (yes or no)? ")
    if (play_yes_no == "no") or (play_yes_no == "n"):
        self.quit_game = True
    else:
        print("\n")
        self.game_total = 0
        self.computer_won = False
        self.quit_game = False
        self.__init__()


class MainGame:

    def __init__(self):
        super().__init__()
        self.game_total = 0
        self.first_player = 0
        self.game_difficulty = 0
        self.computer_won = False
        self.quit_game = False

        explain_game()
        self.game_difficulty = choose_difficulty()
        self.game_difficulty = int(self.game_difficulty)
        begin_game(self)

        while self.game_total < 21:
            take_turn(self)

        game_over(self)

        while not self.quit_game:
            play_again(self)


if __name__ == "__main__":
    MainGame()
