
class Board :
    def __init__(self):
        self.board_game1 = [['C','D','B','A'],['F','J','H','I'],['E','G','K',' ']]
        self.board_game2 = [['A','D','B','C'],['E',' ','H','G'],['K','I','F','J']]
        self.board_game3 = [[' ','A','E','D'],['F','C','G','I'],['J','K','H','B']]
        self.board_game4 = [['B','A','E','D'],['F','C','G','I'],['J','K','H',' ']]
        
        self.board_game = [['','','',''],['','','',''],['','','',' ']]


    def display_board(self,pos):
        print(pos[0][0] + '|' + pos[0][1] + '|' + pos[0][2] + '|' + pos[0][3])
        print('-------')
        print(pos[1][0] + '|' + pos[1][1] + '|' + pos[1][2] + '|' + pos[1][3])
        print('-------')
        print(pos[2][0] + '|' + pos[2][1] + '|' + pos[2][2] + '|' + pos[2][3])

    def play_game(self) :
        chosse_board = int(input("you want to play borad 1 or 2 or 3 or 4: "))
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

    
    def select_character(self,board_game,new_input): 
        pass   

    def check_winner(self,):
        if self.board_game ==   [['A','B','C','D'],['E','F','G','H'],['I','J','K',' ']]:
            print("ABC Block completed  You win")
             
       
   

class InputProcessor:
    def add_input(self) :
        pos = input("select you want to switch :  ")
        return pos
    pass


    


board = Board()
board.play_game()