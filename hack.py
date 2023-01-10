from platform import architecture


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

ar = list(map(int, input().rstrip().split()))
count=0
for i in range(n):      
    for j in range(n):
        if((ar[i]+ar[j])%k==0 and ar[i] !=ar[j]):
            count +=1
print(int(count)/2)
#     # test_list =ar[i]
#     if((test_list)%k==0):
#         count +=1
# print(count)
# ar = list(map(int, input().rstrip().split()))
# count=0
# for i in range(len(ar)):
#     if((ar[i]+ar[i+1])%k==0):
#         count +=1
# print(count)

  
# # printing original list 
# print("The original list : " + str(ar))
  
# # All possible pairs in List
# # Using list comprehension + enumerate()
# res = [(a, b) for idx, a in enumerate(test_list) for b in test_list[idx + 1:]]
  
# # printing result 
# print("All possible pairs : " + str(res))
