#6201012620040 คงเดช สมใจ 
#6201012620074 ณัฐชนน วะลับ 
#6201012620341 นางสาวตุลยา สารโพคา
import time
class Board :
    def __init__(self):
        self.gamerun = 1
        self.board_game1 = [['C','D','B','A'],['F','J','H','I'],['E','G','K',' ']]
        self.board_game2 = [['A','H','B','C'],['E','F','D','G'],['K','I','J',' ']]
        self.board_game3 = [['H','F','E','D'],['A','C','G','I'],['J','K','B',' ']]
        self.board_game4 = [['B','J','F','D'],['E','G','C','K'],['A','I','H',' ']]
        #self.board_game4 = [['A','B','C','D'],['E','F','G','H'],['I','J',' ','K']]#checkWinnertest
        self.board_game = [['','','',''],['','','',''],['','','',' ']]
        
    def display_board(self,pos):
        print(pos[0][0] + '|' + pos[0][1] + '|' + pos[0][2] + '|' + pos[0][3])
        print('-------')
        print(pos[1][0] + '|' + pos[1][1] + '|' + pos[1][2] + '|' + pos[1][3])
        print('-------')
        print(pos[2][0] + '|' + pos[2][1] + '|' + pos[2][2] + '|' + pos[2][3])

    def play_game(self) :
        print("Hello Player"); time.sleep(2.1)
        print("Welcome to ABC Block Game!!"); time.sleep(2.1)
        print("Umm..First we have to choose a board game."); time.sleep(2.1)
        chosse_board = int(input("You want to play borad 1 or 2 or 3 or 4: "))
        while self.gamerun == 1 :
            if chosse_board == 1:
                self.board_game = self.board_game1
                self.display_board(self.board_game)
            elif chosse_board == 2:
                self.board_game = self.board_game2
                self.display_board(self.board_game)
            elif chosse_board == 3:
                self.board_game = self.board_game3
                self.display_board(self.board_game)
            elif chosse_board == 4:
                self.board_game = self.board_game4
                self.display_board(self.board_game)
            new_position = InputProcessor.add_input(self)
            self.select_character(self.board_game,new_position)
            self.check_winner()
    
    def select_character(self,board_game,new_input): 
        for i in range(3) :
           for j in range(4) :
               if board_game[i][j] == " " :
                   self.blank_row = i
                   self.blank_column = j
        for a in range(3) :
           for b in range(4) :
               if board_game[a][b] == new_input :
                   self.row_input = a
                   self.column_input = b
        if self.blank_column - self.column_input == 0 and self.blank_row - self.row_input == 1:
            case = board_game[self.blank_row][self.blank_column]
            board_game[self.blank_row][self.blank_column] = board_game[self.row_input][self.column_input]
            board_game[self.row_input][self.column_input] = case
        elif self.blank_column - self.column_input == 0 and self.blank_row - self.row_input == -1:
            case = board_game[self.blank_row][self.blank_column]
            board_game[self.blank_row][self.blank_column] = board_game[self.row_input][self.column_input]
            board_game[self.row_input][self.column_input] = case
        elif self.blank_row - self.row_input == 0 and self.blank_column - self.column_input == 1:
            case = board_game[self.blank_row][self.blank_column]
            board_game[self.blank_row][self.blank_column] = board_game[self.row_input][self.column_input]
            board_game[self.row_input][self.column_input] = case    
        elif self.blank_row - self.row_input == 0 and self.blank_column - self.column_input == -1:
            case = board_game[self.blank_row][self.blank_column]
            board_game[self.blank_row][self.blank_column] = board_game[self.row_input][self.column_input]
            board_game[self.row_input][self.column_input] = case 

    def check_winner(self,):
        if self.board_game ==   [['A','B','C','D'],['E','F','G','H'],['I','J','K',' ']]:
            print("ABC Block completed  You win")
            self.gamerun = 0

class InputProcessor:
    def add_input(self) :
        pos = input("select you want to switch :  ")
        return pos

board = Board()
board.play_game()