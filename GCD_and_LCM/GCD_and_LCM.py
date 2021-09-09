#author : @akash
def GCD(n,m):
   if m==0:
     return n
   return GCD(m,n%m)
   
def LCM(n,m):
   return (n*m)//GCD(n,m)


n,m=map(int,input().split())
ans=LCM(n,m)
print(ans)
