s=str(input())
ans=[]
for i in range(len(set(s))):
   ans.append(s.count(s[0]))
   s=s.replace(s[0],"")
print(ans)

   
"""
input: 
aaabbc

output:
3 2 1
"""
