def sum_to_N(arr, N):

    '''This function finds the index of the elements in a list whose sum equals a number N.
    Time complexity is O(n)'''
    
    #initializing set
    s = set()

    #traverse through the list
    for num in arr:

        t = N - num 
        
        if t in s:
            return [arr.index(num), arr.index(t)] #returns a list containg both the index
        
        s.add(num)

if __name__ == "__main__":

    #taking input
    i = input("Enter numbers separated with spaces: ")
    N  = int(input("Enter N: "))

    arr = list(map(int,i.split()))   

    result = sum_to_N(arr, N)   
    print("The indexes of the numbers are: " + str(result[0]) + " and " + str(result[1]))
