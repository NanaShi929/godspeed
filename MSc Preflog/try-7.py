def is_matrix(m): 
    return isinstance(m, list) and all(isinstance(r, list) for r in m) and len(set(len(r) for r in m)) == 1

x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[9,8,7],[6,2,5],[3,2,1]]  

print(is_matrix(x))  
print(is_matrix(y)) 

if is_matrix(x) and is_matrix(y) and len(x)==len(y) and len(x[0])==len(y[0]):
    res = [[x[i][j]+y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
    for r in res: print(r)
else:
    print("Invalid matrices")
    
 

