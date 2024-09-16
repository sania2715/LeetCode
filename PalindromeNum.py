#Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome( x):
        str_num= str(x)
        rev_str_num=str_num[::-1] #Reverse it
        if(str_num==rev_str_num):
            return True
        else:
            return False

print(isPalindrome(454))

#Output : true
 
