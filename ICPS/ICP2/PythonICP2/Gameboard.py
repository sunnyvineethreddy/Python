def horizontal_line ( size ):
    return " ---" * size + " \n"

def vertical_lines ( size ):
    return "|   " * size + "|\n"

def gameboard ( size ):
    board = """"""
    for i in range(size):
        board += horizontal_line(size)
        board += vertical_lines(size)
    board += horizontal_line(size)
    return board

if __name__ == "__main__":
    size = int(input("What size game board do You want? "))
    print(gameboard(size))