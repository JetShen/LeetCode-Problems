#49. Group Anagrams
# Given an array of strings, group anagrams together.
#
# Example 1:                                                Example 2:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]       Input: strs = [""]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]       Output: [[""]]


lista = ["eat","tea","tan","ate","nat","bat"]
# def GroupAnagrams(lista):                 
#     group = []                            
#     for i in lista:                               --------------------------------------------------------------
#         g = []                                    --------------------------------------------------------------
#         for j in lista:                           --------------------------------------------------------------
#             if sorted(i) == sorted(j):            ----------------------SLOOOOOOOOOOOOOOOW----------------------
#                 g.append(j)                       --------------------------------------------------------------
#         if g not in group:                        --------------------------------------------------------------
#             group.append(g)                        --------------------------------------------------------------                     
#     return group[::-1]


def GroupAnagrams(lista):
    dic = {}
    for word in lista:
        temp = ''.join(sorted(word))
        if temp in dic:
            dic[temp].append(word)
        else:
            dic[temp] = [word]
    return dic.values()

GroupAnagrams(lista)