def sort_inv_count(my_list, inv=0):
    '''
    This function counts the number of number inversions in an array,
    using the recursive merge sort algo. as basis. 
    '''
    if len(my_list) == 1:
        return my_list, 0
    else:
        left = my_list[:len(my_list) // 2]
        right = my_list[len(my_list) // 2:]

        sorted_l, inv_l = sort_inv_count(left)
        sorted_r, inv_r = sort_inv_count(right)
        sorted_list, inv_x = x_inv_count(sorted_l, sorted_r)
        
        return sorted_list, (inv_l + inv_r + inv_x)

def x_inv_count(list1, list2):
    '''
    This function merges two arrays, and counts the number of digit inversions
    between them
    '''
    j,k = 0,0
    x_inv = 0
    merged_list = []
    
    for i in range(len(list1)+len(list2)):
        if j>=len(list1) or k >=len(list2):
            merged_list= merged_list + list1[j:] + list2[k:]
            break
        
        elif list1[j]<=list2[k]:
            merged_list.append(list1[j])
            j+=1
            
        else:
            merged_list.append(list2[k])
            k+=1
            if j<len(list1):
                x_inv = x_inv + len(list1[j:])

    return merged_list, x_inv


'''
This snipet of code reads from a text file in which each line contains a number.
The number of inversions in this sequence of numbers is counted'''
sum_inv = 0
digit_list=[]
f = open("C:/Users/joaop/Desktop/IntegerArray.txt", "r")
for num in f:
    digit_list.append(int(num))
_, inv = sort_inv_count(digit_list)
print(inv)

