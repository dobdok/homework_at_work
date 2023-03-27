"""
# zadanie 1:
Napisz program, który będzie przypominał grę w kółko i krzyżyk
    program rysuje plansze do gry w kółko i krzyżyk
    komputer zaczyna rozgrywkę i wstawia "O" w dowolne pole
    program pyta użytkownika gdzie wstawić "X", użytkownik podaje dwie cyfry w formacie A B gdzie A to wiersz a B kolumna
    program sprawdza czy znak może być wprowadzony we wskazane pole
    program po każdym znaku rysuje aktualny układ planszy
    program po każdym znaku sprawdza czy ktoś nie wygrał rozgrywki
    program powtarza czynności do wykorzystania wszystkich pól
    skorzystaj z poznanych funkcji losujących aby program wybierał gdzie wstawić znak
    jeżeli nikt nie wygrał a skończyły się wolne pola, program informuje o tym użytkownika
"""


print("""
This is a Tic Tac Toe game for both human players.\n""")



board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


game_on = True


current_player = "X"



def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print('Accordingly fields numbers:\n0 1 2\n3 4 5\n6 7 8')
    print('* '*10+'\n')


def players():

    p1 = input("Select Player - X or O: ").upper()
    p2 = ""
    if p1 == "X":
        p2 = "O"
        print("The other Player2: " + p2)
    elif p1 == "O":
        p2 = "X"
        print("Player2: " + p2)
    elif p1 != "O" or p1 != "X":
        print("Sorry,invalid input. Type X or O")
        play_game()



def player_position():
    global current_player
    print("\nCurrent Player: " + current_player)
    position = input("Choose position from 1 - 9: ")


    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose position from 1 - 9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Position already selected, choose another position!")
    board[position] = current_player
    display_board()



def play_game():
    print("My Tic Tac Toe Game")
    display_board()
    players()


    while game_on:
        player_position()

        # Check winner
        def check_winner():
            global game_on


            if board[0] == board[1] == board[2] != "-":
                game_on = False
                print("Congratulations " + board[0] + " you WON!")
            elif board[3] == board[4] == board[5] != "-":
                game_on = False
                print("Congratulations " + board[3] + " you WON!")
            elif board[6] == board[7] == board[8] != "-":
                game_on = False
                print("Congratulations " + board[6] + " you WON!")


            elif board[0] == board[3] == board[6] != "-":
                game_on = False
                print("Congratulations " + board[0] + " you WON!")
            elif board[1] == board[4] == board[7] != "-":
                game_on = False
                print("Congratulations " + board[1] + " you WON!")
            elif board[2] == board[5] == board[8] != "-":
                game_on = False
                print("Congratulations " + board[2] + " you WON!")


            elif board[0] == board[4] == board[8] != "-":
                game_on = False
                print("Congratulations " + board[0] + " you WON!")
            elif board[2] == board[4] == board[6] != "-":
                game_on = False
                print("Congratulations " + board[6] + " you WON!")
            elif "-" not in board:
                game_on = False
                print("It's a Tie")
                exit()

        def flip_player():
            global current_player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

        flip_player()
        check_winner()


play_game()
