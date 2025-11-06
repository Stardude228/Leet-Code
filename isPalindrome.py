# isPalindrome completed by Oomat Latipov
def isPalindrome():
    
    x = 10
    string_x = str(x)
    isPalindromeCheck = True
    
    start = 0
    end = len(string_x) - 1
    
    while start < end:
        if string_x[start] != string_x[end]:
            isPalindromeCheck = False
            break
        start += 1
        end -= 1
    
    print(isPalindromeCheck)

isPalindrome()


# optimized version of isPalindrome (Leet Code)
def isPalindrome():
    x = 22233333222
    print(str(x) == str(x)[::-1])

isPalindrome()