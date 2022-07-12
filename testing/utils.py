def winCheck(arr, char):
    # Check all possible winning combinations
    matches = [[0, 1, 2], [3, 4, 5],
               [6, 7, 8], [0, 3, 6],
               [1, 4, 7], [2, 5, 8],
               [0, 4, 8], [2, 4, 6]]
 
    for i in range(8):
        if(arr[matches[i][0]] == char and
            arr[matches[i][1]] == char and
            arr[matches[i][2]] == char):
            return True
    return False
 
def isValidBoard(arr):
    # Count number of 'X' and 'O' in the given board
    xcount = arr.count('X')
    ocount = arr.count('O')
     
    # Board can be valid only if either xcount and ocount
    # is same or count is one more than oCount
    if(xcount == ocount+1 or xcount == ocount):
        # Check if O wins
        if winCheck(arr, 'O'):
            # Check if X wins, At a given point only one can win,
            # if X also wins then return Invalid
            if winCheck(arr, 'X'):
                return False
 
            # O can only win if xcount == ocount in case where whole
            # board has values in each position.
            if xcount == ocount:
                return True
 
        # If X wins then it should be xc == oc + 1,
        # If not return Invalid    
        if winCheck(arr, 'X') and xcount != ocount+1:
            return False
         
        # if O is not the winner return Valid
        if not winCheck(arr, 'O'):
            return True
         
    # If nothing above matches return invalid
    return False