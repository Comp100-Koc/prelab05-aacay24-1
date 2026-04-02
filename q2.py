
def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    for n in range(len(s)):
        for i in range (len(s)):
            if i< (len(s)-1):
                if s[i]==s[i+1]:
                    s= s[:i]+ s[i+2:]
    return s