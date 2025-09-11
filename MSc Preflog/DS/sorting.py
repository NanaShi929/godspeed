list=[[3,2,1],[6,5,4]]

'''
list=[[3,2,1],[6,5,4]]
#sorted_rows = [sorted(row) for row in list]
#print(sorted_rows)

sorted_rows = []
for row in list:
    sorted_row = sorted(row)  
    sorted_rows.append(sorted_row) 


print(sorted_rows)


row=list
for i in row:
   sorted=row[i].sort()
print(sorted)
'''
'''
def sortRows(mat):
    for row in mat:
        row.sort()

mat = [
    [77, 11, 22, 3],
    [11, 89, 1, 12],
    [32, 11, 56, 7],
    [11, 22, 44, 33]
]

sortRows(mat)

print(sortRows(mat))

for row in mat:
    print('  [', end='')
    print(', '.join(map(str, row)), end='')
    print(']')
print(']')
'''
'''
# sorting 2d array
list=[[3,2,1],[6,5,4]]
for row in list:
    sort=sorted(row)
    print(sort)
 '''
 
 
 
''' 
#Transpose



row=len(list[0])
col=len(list)
new=[]
for i in range(0,row):
    nrow=[]
    for j in range(0,col):
        nrow.append(list[j][i])
    new.append(nrow)
    
print(new) 
'''
'''
#sum
list=[3,2,1,6,5,4]
def sumList(list):
    return sumListItem(list,len(list)-1)
def sumListItem(list,index):
    if index<0:
        return 0
    return list[index] + sumListItem(list, index - 1)
print(sumList(list))
'''
#numpy

import numpy as np
arr = np.array([
    [3, 2, 1],
    [6, 5, 4]
])
sorted_arr = np.sort(arr, axis=1)  # Sort each row
print("Row-wise Sorted:\n", sorted_arr)
transposed_arr = np.transpose(arr)
print("Transposed:\n", transposed_arr)

arr = np.array([
    3, 2, 1,
    6, 5, 4
])
total_sum = np.sum(arr)
print("Total sum:", total_sum)
   
