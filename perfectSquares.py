from math import ceil, sqrt 

#Recursive version
def perfectSquaresRec(n): 
    # base cases 
    if n <= 3: 
        return n 
    #This variable holds solution but is initialized to the worst case scenerio or MAX sum, n
    solution = n 
    # Goes from 1 to n to find the smallest sum of perfect squares
    for x in range(1, n + 1): 
        #Holds the square of the numbers less than n as we go through every number
        temp = x * x
        #checks if the square is larger than n, if it is we stop checking
        if temp > n: 
            break
        #if it is less than n, we store the lesser- the old solution or the result of the
        #recursive call using n-temp
        else: 
            solution = min(solution, 1 + perfectSquaresRec(n  - temp)) 
    #returns the solution  
    return solution

##############################################################################
    
#Dynamic programming version
def perfectSquaresDP(n): 
    # List to store the minimum squares for numbers less than n in corresponding index
    #base case was if n <= 3 so we initialize to the line below
    squares = [0, 1, 2, 3] 
    # stores the rest of the minimum squares in the list by appending that number until n
    for i in range(4, n + 1): 
        squares.append(i) 
        #Goes through all of the less than numbers to find the minimum
        #Goes from 1 to the square root of 1 so we don't do the same thing over and over
        for x in range(1, int(ceil(sqrt(i))) + 1): 
            #stores the square which will be less than n because of the above range
            temp = x * x 
            if temp > i: 
                break
            else:
                #stores the minimum into the index either the current square or the min
                squares[i] = min(squares[i], 1 + squares[i-temp]) 
    # returns the index for n
    return squares[n]

##############################################################################

#Test cases for recursive version
print(perfectSquaresRec(0))  #Should return 0
print(perfectSquaresRec(1))  #Should return 1
print(perfectSquaresRec(2))  #Should return 2
print(perfectSquaresRec(3))  #Should return 3
print(perfectSquaresRec(6))  #Should return 3
print(perfectSquaresRec(12))  #Should return 3
print(perfectSquaresRec(13))  #Should return 2

#Test cases for dynamic programming version
print(perfectSquaresDP(0))  #Should return 0
print(perfectSquaresDP(1))  #Should return 1
print(perfectSquaresDP(2))  #Should return 2
print(perfectSquaresDP(3))  #Should return 3
print(perfectSquaresDP(6))  #Should return 3
print(perfectSquaresDP(12))  #Should return 3
print(perfectSquaresDP(13))  #Should return 2