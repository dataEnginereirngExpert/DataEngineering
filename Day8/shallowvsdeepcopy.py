import copy

#shalow Copy

org_list=[[1,2],[3,4]]
scopy_list=copy.copy(org_list)
scopy_list [0][0]='A'
print(scopy_list)
print(org_list)
print('--------------------')

#Deep Copy

org_list1=[[1,2],[3,4]]
dcopy_list=copy.deepcopy(org_list1)
dcopy_list [0][0]='A'
print(dcopy_list)
print(org_list1)

