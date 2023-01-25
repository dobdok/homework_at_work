"""
Napisz program, który będzie przypominał grę w kółko i krzyżyk

    program rysuje plansze do gry w kółko i krzyżyk -------------- zadania_done

    komputer zaczyna rozgrywkę i wstawia "O" w dowolne pole TODO

    program pyta użytkownika gdzie wstawić "X", użytkownik podaje dwie cyfry w formacie A B gdzie A to wiersz a B kolumna -------------- zadania_done

    program sprawdza czy znak może być wprowadzony we wskazane pole TODO

    program po każdym znaku rysuje aktualny układ planszy  -------------- zadania_done

    program po każdym znaku sprawdza czy ktoś nie wygrał rozgrywki  -------------- TODO prawie

    program powtarza czynności do wykorzystania wszystkich pól  TODO

    skorzystaj z poznanych funkcji losujących aby program wybierał gdzie wstawić znak  -------------- zadania_done

    jeżeli nikt nie wygrał a skończyły się wolne pola, program informuje o tym użytkownika  TODO

    """


import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            A = []
            for j in range(3):
                A.append('-')
            self.board.append(A)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, A, B, player):
        self.board[A][B] = player

    def is_player_win(self, player):
        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        # for A in self.board:
        #     for item in A:
        #         if item == '-':
        #             return False
        # return True

    def is_board_filled(self):
        for A in self.board:
            for item in A:
                if item == '-':
                    return False
        return True

    def change_player(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for A in self.board:
            for item in A:
                print(item, end=" ")
            print()

    def start_game(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player ->   {player}  turn")

            self.show_board()

            # taking user input
            A, B = list(
                map(int, input("Enter row and column numbers to fix spot: \n [number 1-3] + [space] + [number 1-3]\nInput:  ").split()))
            print()

            # fixing the spot
            self.fix_spot(A - 1, B - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.change_player(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start_game()