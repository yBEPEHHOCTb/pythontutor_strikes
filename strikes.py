N,K=list(map(int,input().split()))
lst=[]
for i in range(K):
    lst.append(set())
    a_i,b_i=list(map(int,input().split()))
    while a_i<=N:
        if a_i%6!=0 and a_i%7!=0:
            lst[i].add(a_i)
        a_i+=b_i
print(len(set.union(*lst)))
