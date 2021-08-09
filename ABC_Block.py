class Board :
    def __init__(self):
        self.board_array = [['A','B','C','D'],['F','E','G','H'],['I','K','J',' ']]

    def display_board(self,):
        print()
        for i in self.board_array:
            for j in i:
                print("|",end='')
                print(j,end="")
            print("|\n---------")
        print()
    #def change_player(self):
    


    #def add_position(self): 
   

class InputProcessor:
    pass

print("นนนี่มาทดสอบ commit จ้า")
    



c
board = Board()
board.display_board()