class Board :
    def __init__(self):
        self.board_array = [['A','B','C','D'],['F','E','G','H'],['I','K','J',' ']]
        print(self.board_array)

    def display_board(self,):
        print()
        for i in self.board_array:
            for j in i:
                print("|",end='')
                print(j,end="")
            print("|\n---------")
        print()
        self.add_position()
    #def change_player(self):
    


    def add_position(self): 
            realInput = input("ใส่ตัวที่จะย้ายมาตำแหน่งนี้จร้า")
            x = int(realInput%3)
            y = int(realInput//3)
            if self.board_array[y][x] != "X" and self.board_array[y][x] != "Y":
                self.board_array[y][x] = self.player
                return True
            else :
                print("Invalid Try Again")
                return False
   

class InputProcessor:
    pass

print("นนนี่มาทดสอบ commit จ้า")
    


board = Board()
board.display_board()
