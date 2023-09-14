def getMinMax(arr):
    n = len(arr)


    # if the array has even number of elements then
    # initialize the first two elements as min and max
    if(n % 2 == 0):
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])

        #set the start index for loop
        i = 2



    # if the array has odd number of elements then
    # initailize the first element as min and max\
    else:
        mx = mn = arr[0]

        #set the start of the loop
        i = 1

    # in the while loop, pick elements in pair and
    # compare the pair with max and min so far
    while(i < n - 1):
        if arr[i] < arr[i + 1]:
            mx = max(mx, arr[i + 1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i + 1])

        
        # increment the index by 2 as two
        # elements are proccessed in loop
        i += 2


    return (mx, mn)


#driver code

arr = [1000, 11, 445, 1, 330, 3000]
mx, mn = getMinMax(arr)
print("Minimum element is", mn)
print("Maximum element is", mx)



#source : https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/