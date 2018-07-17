heightinp= int(input("Enter the height of the board: "))
widthinp= int(input("Enter the width of the board: "))


def board_draw(heightinp,widthinp):
    for temp in range(heightinp):
        print(" --- " * widthinp)
        print("|    " * widthinp, end="")
        print("|")
    print(" --- " * widthinp)

board_draw(heightinp,widthinp)




