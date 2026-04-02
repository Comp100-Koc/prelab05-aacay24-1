def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    a=len(s)
    palindrome=""
    length=0
    for i in range(a):
        left, right= i, i
        while left>=0 and right<a and s[left] == s[right]:
            if (right -left+1)>length:
                length = right-left+1
                palindrome = s[left:right+1]
            left-=1
            right+=1


        left, right= i, i+1
        while left>=0 and right<a and s[left] == s[right]:
            if (right -left +1)>length:
                length = right-left+1
                palindrome = s[left:right+1]
            left-=1
            right+=1
           
          
    
    
    if length <2:
        return  ""
    
    
    
    return palindrome
            
    