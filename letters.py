word=input("enter the charecter")
x=len(word)
a=word[0]
#     print(a[i])
# print(x)
# print(a)
h=[1,2,3,4,5,4,3,2,4,5,2,5,3,3,5,3,5,3,5,2,6,1,4,2,1,0]
k=max([h[ord(char) - ord('a')] for char in word])
print(k*x)
# for i in range(1,26):
#      (a)==chr(h[i]+97)
# for i in range(len(h)):
