def check_queen():
    '''
    Checks whether the queen can move to these cells
    :return: YES or NO
    '''
    if x1 > 8 or x2 > 8 or y1 > 8 or y2 > 8:
        return print('This is not a chessboard! Enter a value from 1-8.')
    if (x1, x2) == (y1, y2):
        return print('This is not a move.')
    if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
        print('YES')
    else:
        print('NO')


# Enter number split
print("Enter the number of cells on the chessboard for the Queen's move. \nExample: 2 2 8 8")
x1, x2, y1, y2 = map(int, input().split())

check_queen()
