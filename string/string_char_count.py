#author : @akash

s=str(input())
#aabbccdd
ans=""
for i in range(len(set(s))):
    ans+=s[0]+str(s.count(s[0]))
    s=s.replace(s[0],"")
    #remove all s[0] char form s
print(ans)

#time complexity T(n)=O(n)

"""
input : 
aaaabbbccd
output:
a4b3c2d1
"""
