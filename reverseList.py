# Iterative python program to reverse an array
# Function to reverse A[] from start to end
def reverseList(A):
    l = 0
    r = len(A) - 1 
	
    while(l < r):
        A[l], A[r] = A[r], A[l]
        l += 1
        r -= 1
    
        


# Driver function to test above function
a = [1, 2, 3, 4, 5, 6]
print(a)
reverseList(a)
print("Reversed list is")
print(a)
# This program is contributed by Pratik Chhajer
