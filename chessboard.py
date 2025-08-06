"""
Exercise:
The 8 queens puzzle is the problem of placing 8 chess queens on an 8×8 chessboard so that no two queens threaten each other.
The exercise this time is to display "graphically" a possible setup. 
The chessboard is represented as an array (instead of a matrix), e.g. [7,3,0,2,5,1,6,4]. This means:
 in the 1st column a queen is located in the 8th row (from the bottom), in the 2nd column there is a queen in the 4th row, etc. (Indexation of rows starts with 0.) 

"""



def Queens(lst):
    print('+-----------------+')
    for i in range(7,-1,-1):
        idx = i
        string = '| '
        for j in lst:
            if j==idx:
                string += 'Q '
            else:
                string += '. '
        string += '|'
        print(string)
                
    print('+-----------------+')


#####################################################
if __name__ == "__main__":
    Queens([7,3,0,2,5,1,6,4])
    Queens([0,4,7,5,2,6,1,3])
    Queens([2,0,0,0,0,0,0,0])