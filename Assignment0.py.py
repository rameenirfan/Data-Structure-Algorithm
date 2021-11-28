# # -*- coding: utf-8 -*-
# """
# Created on Thu Oct 29 15:29:53 2020
#
# @author: Dell
# """
#
# def Multiple(n):
#     lst = []
#     for i in range(n):
#         if i%3==0 or i%5==0:
#             lst.append(i)
#
#     print(lst)
#
#     sum=0
#     for i in range(len(lst)):
#         sum = sum + lst[i]
#
#
#     return sum
#
# x = Multiple(1000)
# print(x)
#
# def Inwords(num):
#     numbers =["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
#     try:
#         return numbers[num]
#     except:
#         return "Value doesn't exist"
#
#
# num = int(input("Enter number upto 10: "))
# x=Inwords(num)
# print(x)
# #
# def SplitandJoin(string):
#      return'-'.join(string.split())
#
#
# x = SplitandJoin("This is a string")
# print(x)
# #
# def LongestWord(word):
#     splited_word = word.split('&!!') #split word with&!! as per given requirement
#     s = ''
#     for eachword in range(len(splited_word)):
#         if len(splited_word[eachword]) > len(s):  # checks if length of splitted word > length of s
#             s = splited_word[eachword]
#     return s
#
#
# w=LongestWord("fun&!!time")
# print(w)

# def RunnerUp(n):
#
#     score_sheet = []
#     for score in n:
#         if score not in score_sheet:
#             score_sheet.append(score)
#
#     score_sheet.sort()
#     return score_sheet[-2]
#
# x = RunnerUp("2 2 5 6 6 7 7 8")
# print("Runnerup : ", x)
