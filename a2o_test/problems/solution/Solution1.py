def createMatrix(n):
     matrix=[]
     for i in range(n):
             row = []
             for j in range(n):
                 element=0    
                 row.append(element)
             matrix.append(row)
     return matrix       
def addObstacles(matrix,obstacles,obstacle):
     for i in range(len(obstacles)):
         matrix[obstacles[i][0]-1][obstacles[i][1]-1 ]=  obstacle
     return matrix
def countQuenMoves(board,row,col):
            move_count = 0
            board[row][col] = 1
            
            move_count += count_moves(board, row - 1, col, -1, 0) 
            move_count += count_moves(board, row + 1, col, 1, 0)  
            move_count += count_moves(board, row, col - 1, 0, -1)  
            move_count += count_moves(board, row, col + 1, 0, 1)   
            move_count += count_moves(board, row - 1, col - 1, -1, -1) 
            move_count += count_moves(board, row - 1, col + 1, -1, 1)   
            move_count += count_moves(board, row + 1, col - 1, 1, -1)   
            move_count += count_moves(board, row + 1, col + 1, 1, 1)  

            board[row][col] = 0
            return move_count
def count_moves(board, row, col, row_increment, col_increment):
            move_count = 0
            n = len(board)

            if 0 <= row < n and 0 <= col < n and board[row][col] == 0:
                move_count += 1
                move_count += count_moves(board, row + row_increment, col + col_increment, row_increment, col_increment)

            return move_count
def  queensAttack(n,k,rq,cq,obstacles): 
            board=createMatrix(n)
            if k==len(obstacles) and k>0 :
                board=addObstacles(board,obstacles,1)
            quenMoves=countQuenMoves(board,rq,cq)
            return quenMoves
