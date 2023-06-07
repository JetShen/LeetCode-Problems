#242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#Example 1:                                 Example 2:
# Input: s = "anagram", t = "nagaram"       Input: s = "rat", t = "car"
# Output: true                              Output: false

s="anagram"
t="nagaram"


def anagram(s,t):
    if len(s)!=len(t):
        return False
    else:
        s=sorted(s)
        t=sorted(t)
        if s==t:
            return True
        else:
            return False
        
print(anagram(s,t))