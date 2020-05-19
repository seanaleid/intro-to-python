import random 

score = {
    "wins": 0,
    "ties": 0,
    "losses": 0
}

historical_data_message = "Wins: %s, Ties: %s, Losses %s"
quit_message = "Thanks for playing Rock, Paper, Scissors!"
win_message = "Congratulations, you won!"
loss_message = "Sorry, you lost!"
tie_message = "It was a tie."

historical_data = #TODO
score["wins"] = historical_data['wins']
score["ties"] = historical_data['ties']
score["losses"] = historical_data['losses']

choice_options = {
    1: "rock",
    2: "paper",
    3: "scissors",
    9: "quit"
}

computer_choice = random.randint(1, 3) # use the random module imported above
user_choice = None

### Procedures
### 1. display welcome_message
### 2. load historical_data and populate variables with data
### 3. display historical_data_message with historical data
### 4. prompt user to make a choice between rock, paper, scissors, or quit
    ### 4.1 if quit, update text file with current wins, ties, losses data and exit game
    ### 4.2 if not quit, move on to step 5
### 5. computer makes a choice between rock, paper, and scissors
### 6. compare user choice and computer choice
### 7. display message based on result of comparison
### 8. update wins, ties, and losses
### 9. return to step 4

### 1. display welcome_message
def show_welcome_message():
    welcome_message = "Welcome to Rock, Paper, Scissors!"
    print(welcome_message)

### 2. load historical_data and populate variables with data
def get_historical_data():
    text_file = open("history.txt", "r")
    text_data = text_file.read().split(",")
    text_file.close()
    return {
        "wins": int(text_data[0]),
        "ties": int(text_data[1]),
        "losses": int(text_data[2])
    }

### 3. display historical_data_message with historical data
def show_historical_data_message():
    print(historical_data_message %
            (score["wins"], score["ties"], score["losses"]))

### 4. prompt user to make a choice between rock, paper, scissors, or quit
def get_user_choice():
    choice = input("[1] rock [2] paper [3] scissors [9] quit\n")
    return choice_options[int(choice)]

### 4.1 if quit, update text file with current wins, ties, losses data and exit game
def quit_ame(wins, ties, losses):
    text_file = open("history.txt", "w")
    text_file.write(str(wins) + "," + str(ties) + "," + str(losses))
    text_file.close()

### 4.2 if not quit, move on to step 5
### 5. computer makes a choice between rock, paper, and scissors

### 6. compare user choice and computer choice
def compare_choices_and_get_result(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "win"
    else:
        return "loss"

### 7. display message based on result of comparison
### 8. update wins, ties, and losses
def display_result_message_and_update_score(result):
    if result == "tie":
        print(tie_message)
        score["ties"] += 1
    elif result == "win":
        print(win_message)
        score["wins"] += 1
    else:
        print(loss_message)
        score["losses"] += 1