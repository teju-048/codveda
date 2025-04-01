#creating board with n number of rows and columns
n = int(input("Enter the value of n : ")) 
if n in [4,8,16,32]:
    board = [[0 for i in range(n)] for i in range(n)]

#checking for attacking of queens column,row and diagonal wise
    def check_column(board,row,column):
        for i in range(row,-1,-1):
            if board[i][column]==1:
                return False
        return True
    def check_diagonal(board,row,column):
        for i,j in zip(range(row,-1,-1),range(column,-1,-1)):
            if board[i][j]==1:
                return False
        for i,j in zip(range(row,-1,-1),range(column,n)):
            if board[i][j]==1:
                return False
        return True
    
    #backtracking
    def n_queens(board,row):
        if row==n:
            return True
        for i in range(n):
            if(check_column(board,row,i)==True and check_diagonal(board,row,i)==True):
                board[row][i]=1
                if n_queens(board,row+1):
                    return True
                board[row][i]=0
        return False
    n_queens(board,0)

    for row in board:
        print(row)
else:
    print("No solution")