# def merge_the_tools(string, k):
#     # Divide the string into parts of length k
#     parts = [string[i:i + k] for i in range(0, len(string), k)]
#     for part in parts:
#         unique_chars = []
#
#         for char in part:
#             if char not in unique_chars:
#                 unique_chars.append(char)
#
#         # Print the unique characters without duplicates
#         print(' '.join(unique_chars))
def merge_the_tools():
    s=input()
    s1=int(input())
    k=input()
    li=[]
    return(s[:s1]+k+s[s1+1:])



