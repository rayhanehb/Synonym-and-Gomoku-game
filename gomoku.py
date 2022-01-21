"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 26, 2020
"""

# rayhaneh continued

def is_empty(board):

    for i in range (len(board)):
        for j in range (len(board[i])):
            if board[i][j] != " ":
                return False
    return True


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    length = length

    if d_y == 0 and d_x ==1:
        return bounded_leftright(board, y_end, x_end,length, d_y, d_x)

    elif d_y == 1 and d_x == 0:
        return bounded_updown(board, y_end, x_end,length, d_y, d_x)

    elif d_y == 1 and d_x == 1:
        return bounded_leftdiag(board, y_end, x_end, length, d_y, d_x)

    elif d_y == 1 and d_x == -1:
        return bounded_rightdiag(board, y_end, x_end, length, d_y, d_x)


def bounded_leftright(board, y_end, x_end, length, d_y, d_x):

    open= True
    semiopen=True
    closed = True

    if x_end-length<0:
        open = False
        if x_end+1 > len(board)-1:
            semiopen= False
        else:
            if board[y_end][x_end+1]==" ":
                closed=False
            else:
                semiopen=False
    else:
        if board[y_end][x_end-length] == " ":
            closed= False
            if x_end+1 > len(board)-1:

                open= False
            else:
                if board[y_end][x_end+1]==" ":
                    closed=False
                else:
                    open=False

        else:
            open= False
            if x_end+1 > len(board)-1:
                semiopen= False
            else:
                if board[y_end][x_end+1]==" ":
                    closed=False
                else:
                    semiopen=False

    if open == True:
        semiopen = False
        return "OPEN"
    elif semiopen == True:
        return "SEMIOPEN"
    elif closed== True:
        return "CLOSED"


def bounded_updown(board, y_end, x_end, length, d_y, d_x):


    ''' board= [["b"  ,"w",  "b", "w", "b"], #0,4
                [" " , "w",  "w", "w", " "],
                ["w",  "w", " ", " ", "b"],
                ["w" , "b",  "w", "b", "w"],
                [" " , "w",  "w", " ", "w"]] '''

    open= True
    semiopen=True
    closed = True

    if y_end-length<0:
        open = False
        if y_end+1 > len(board)-1:
            semiopen= False
        else:
            if board[y_end+1][x_end]==" ":
                closed=False
            else:
                semiopen=False
    else:
        if board[y_end-length][x_end] == " ":
            closed= False
            if y_end+1 > len(board)-1:
                open= False
            else:
                if board[y_end+1][x_end]==" ":
                    closed=False
                else:
                    open=False

        else:
            open= False
            if y_end+1 > len(board)-1:
                semiopen= False
            else:
                if board[y_end+1][x_end]==" ":
                    closed=False
                else:
                    semiopen=False

    if open == True:
        semiopen = False
        return "OPEN"
    elif semiopen == True:
        return "SEMIOPEN"
    elif closed== True:
        return "CLOSED"

def bounded_leftdiag(board, y_end, x_end, length, d_y, d_x):

    ''' board= [["w"  ,"b",  " ", "b", "b"], #0,4
                [" " , "w",  "w", "b", " "],
                ["w",  "w", " ", " ", "b"], (3,1)
                ["w" , "w",  "w", " ", "w"],
                [" " , "w",  " ", " ", "w"]] '''
    open= True
    semiopen=True
    closed = True

    if y_end-length<0 or x_end-length<0:
        open = False
        if y_end+1 > len(board)-1 or x_end+1 > len(board)-1:
            semiopen= False
        else:
            if board[y_end+1][x_end+1]==" ":
                closed=False
            else:
                semiopen=False
    else:
        if board[y_end-length][x_end-length] == " ":
            closed= False
            if y_end+1 > len(board)-1 or x_end+1 > len(board)-1 :
                open= False
            else:
                if board[y_end+1][x_end+1]==" ":
                    closed=False
                else:
                    open=False

        else:
            open= False
            if y_end+1 > len(board)-1 or x_end+1 > len(board)-1 :
                semiopen= False
            else:
                if board[y_end+1][x_end+1]==" ":
                    closed=False
                else:
                    semiopen=False
    if open == True:
        semiopen = False
        return "OPEN"
    elif semiopen == True:
        return "SEMIOPEN"
    elif closed== True:
        return "CLOSED"

def bounded_rightdiag(board, y_end, x_end, length, d_y, d_x):
    '''board= [["w"  ,"b",  " ", "b", "b"], #0,4
            [" " , "w",  "w", "b", " "],
            ["w",  "w", " ", "w", "b"],
            ["w" , "w",  "w", "b", "w"],
            [" " , " ",  " ", " ", "w"]]'''

    open= True
    semiopen=True
    closed = True

    if y_end-length<0 or x_end+length> len(board)-1:
        open = False
        if y_end+1 > len(board)-1 or x_end-1 < 0:
            semiopen= False
        else:
            if board[y_end+1][x_end-1]==" ":
                closed=False
            else:
                semiopen=False
    else:
        if board[y_end-length][x_end+length] == " ":
            closed= False
            if y_end+1 > len(board)-1 or x_end-1 < 0:
                open= False
            else:
                if board[y_end+1][x_end-1]==" ":
                    closed=False
                else:
                    open=False

        else:
            open= False
            if y_end+1 > len(board)-1 or x_end-1 < 0 :
                semiopen= False
            else:
                if board[y_end+1][x_end-1]==" ":
                    closed=False
                else:
                    semiopen=False
    if open == True:
        semiopen = False
        return "OPEN"
    elif semiopen == True:
        return "SEMIOPEN"
    elif closed== True:
        return "CLOSED"


def detect_row(board, col, y_start, x_start,length, d_y, d_x):
    count =0
    open_seq_count = 0
    semi_open_seq_count = 0

    if d_y == 0 and d_x==1:
        for i in range(x_start,len(board)):
            if board[y_start][i] == col and i != len(board)-1:
                count +=1
            else:
                if board[y_start][i] == col and i == len(board)-1:
                    count+=1
                    i+=1
                if count == length:
                    y_end = y_start
                    x_end = i-1
                    bound_res = is_bounded(board, y_end, x_end, length, d_y, d_x)
                    if bound_res == "OPEN":
                        open_seq_count+=1
                        count=0
                    elif bound_res == "SEMIOPEN":
                        semi_open_seq_count +=1
                        count = 0
                    elif bound_res=="CLOSED":
                        count =0
                else:
                    count =0

        return open_seq_count,semi_open_seq_count

    if d_y ==1 and d_x==0:

        for i in range(y_start,len(board)):
            if board[i][x_start] == col and i != len(board)-1:
                count +=1
            else:
                if board[i][x_start] == col and i == len(board)-1:
                    count+=1
                    i+=1
                if count == length:
                    y_end = i-1
                    x_end = x_start
                    bound_res = is_bounded(board, y_end, x_end, length, d_y, d_x)
                    if bound_res == "OPEN":
                        open_seq_count+=1
                        count=0
                    elif bound_res == "SEMIOPEN":
                        semi_open_seq_count +=1
                        count = 0
                    elif bound_res=="CLOSED":
                        count =0
                else:
                    count =0

        return open_seq_count,semi_open_seq_count

    if d_y==1 and d_x==1:
        '''board= [["w"  ,"b",  " ", "b", "b"],
                   [" " , "w",  "w", "b", " "],
                   ["w",  "w", " ",  "w", "b"],
                   ["w" , "w",  "w", "b", " "],
                   [" " , " ",  " ", " ", "w"]]'''


        n=max(y_start,x_start)
        for i in range(len(board)-n):
            if board[i+y_start][x_start+i] == col and i != len(board)-n-1:
                count +=1
            else:
                if board[i+y_start][x_start+i] == col and i == len(board)-n-1:
                    count+=1
                    i+=1
                if count == length:
                    y_end = i+y_start-1
                    x_end = x_start+i-1
                    bound_res = is_bounded(board, y_end, x_end, length, d_y, d_x)
                    if bound_res == "OPEN":
                        open_seq_count+=1
                        count=0
                    elif bound_res == "SEMIOPEN":
                        semi_open_seq_count +=1
                        count = 0
                    elif bound_res=="CLOSED":
                        count =0
                else:
                    count =0

        return open_seq_count,semi_open_seq_count

    if d_y == 1 and d_x == -1:

        m= x_start-y_start
        for i in range(m+1):
            if board[y_start + i][x_start - i] == col and y_start + i!= x_start :
                count +=1
            else:
                if board[y_start + i][x_start - i] == col and y_start + i == x_start:
                    count+=1
                    i+=1
                if count == length:
                    y_end = i+y_start-1
                    x_end = x_start-i+1
                    bound_res = is_bounded(board, y_end, x_end, length, d_y, d_x)
                    if bound_res == "OPEN":
                        open_seq_count+=1
                        count=0
                    elif bound_res == "SEMIOPEN":
                        semi_open_seq_count +=1
                        count = 0
                    elif bound_res=="CLOSED":
                        count =0
                else:
                    count =0

        return open_seq_count,semi_open_seq_count

def detect_rows(board, col, length):


    open_seq_count, semi_open_seq_count = 0, 0
    for x_start in range (len(board)):
        m = detect_row(board, col, 0, x_start,length, 1, 0)
        open_seq_count+=m[0]
        semi_open_seq_count+=m[1]
        m=detect_row(board, col, 0, x_start,length, 1, 1)
        open_seq_count+=m[0]
        semi_open_seq_count+=m[1]
        m=detect_row(board, col, 0, x_start,length, 1, -1)
        open_seq_count+=m[0]
        semi_open_seq_count+=m[1]

    for y_start in range(len(board)):
        if y_start==0:
            m=detect_row(board, col, y_start, 0,length, 0, 1)
            open_seq_count+=m[0]
            semi_open_seq_count+=m[1]
        else:
            m=detect_row(board, col, y_start, 0,length, 0, 1)
            open_seq_count+=m[0]
            semi_open_seq_count+=m[1]
            m=detect_row(board, col, y_start, 0,length, 1, 1)
            open_seq_count+=m[0]
            semi_open_seq_count+=m[1]
            m=detect_row(board, col, y_start, len(board)-1,length, 1, -1)
            open_seq_count+=m[0]
            semi_open_seq_count+=m[1]


    return open_seq_count, semi_open_seq_count

def search_max(board):
    score_coord={}
    count=0
    for i in range (len(board)):
        for j in range (len(board)):
           count+=1
           if board[i][j]==" ":
            board[i][j] = "b"
            score_coord[score(board)]=(i,j)
            board[i][j] = " "
           # if count==2:
           #     del score_coord[min(score_coord.values())]
           #     count=1

    move_y, move_x = score_coord[max(score_coord.keys())]

    return move_y, move_x

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win(board):
    count=0
    br= detect_rows(board,"b",5)
    if br[0]>=1 or br[1]>=1:
        return "Black won"
    wr=detect_rows(board,"w",5)
    if wr[0]>=1 or wr[1]>=1:
        return "White won"
    else:
        for i in range (len(board)):
            for j in range (len(board[i])):
                if board[i][j]==" ":
                    count+1
        if count == len(board)*len(board):
            return "Tie"
        else:
            return "Continue playing"



def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))






def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5
    print(is_bounded(board, y_end, x_end, length, d_y, d_x))
    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    print (detect_row(board, "w", 0,x,length,d_y,d_x))
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':
    make_empty_board(5)
    # is_empty(board)
    # play_gomoku(8)
    # test_is_bounded()

