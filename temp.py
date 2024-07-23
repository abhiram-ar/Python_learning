def encode(strs):
        #we will store the no. of characters of each word before the actual word
        #along with a delimiter #, because the word may contain a number in the begining
        
        res = ""
        for s in strs:
            res += str(len(s))+ "#" + s
            
        return res
        
        #time complexity = O(n)
        
def decode(s):
        res, i = [], 0  # i is pointer

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])

            i = j+1+length

        return res 


input= ["neet","code","love","you"]
encoded = encode(input)
print(encoded)

decoded = decode(encoded)
print(decoded)

