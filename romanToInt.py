# romanToInt completed by Oomat Latipov
def romanToInt():
    
    romanInts = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    s = "MCMXCIV"
    result = 0
    
    for i in range(len(s) - 1):
        if romanInts[s[i]] >= romanInts[s[i+1]]:
            result += romanInts[s[i]]
        else:
            result -= romanInts[s[i]]
    
    result += romanInts[s[-1]]
    print(result)
    
romanToInt()


# Leet Code version of romanToInt
def romanToInt():
    
    romanInts = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    
    s = "MCMXCIV"
    
    values={'I':1,"V":5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=0
    i=0
    if len(s)==1:
        return values[s]
    while i<len(s)-1:
        if(values[s[i]]>=values[s[i+1]]):
            total+=values[s[i]]
            i+=1
        elif(values[s[i]]<values[s[i+1]]):
            total+=values[s[i+1]]-values[s[i]]
            i=i+2
        #print(values[s[i]])
        if(i==len(s)-1):
            total+=values[s[i]]
            break

    return total