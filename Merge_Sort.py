def merge(list1, list2):
    #this function merge two sorted arrays in a single sorted array
    j,k = 0,0
    merged_list = []
    
    for i in range(len(list1)+len(list2)):
        if j>=len(list1) or k >=len(list2):
            merged_list= merged_list + list1[j:] + list2[k:]
            break
        
        elif list1[j]<list2[k]:
            merged_list.append(list1[j])
            j+=1
            
        else:
            merged_list.append(list2[k])
            k+=1
        
    return merged_list

def sort(my_list):
    #this function sorts an array by recursively merge_sorting
    if len(my_list)>1:
        left = my_list[:len(my_list) // 2]
        right = my_list[len(my_list) // 2:]
        sorted_l = sort(left)
        sorted_r = sort(right)
        return merge(sorted_l, sorted_r)
    else:
        return my_list
    
print(sort([5, 4, 1, 10, 2])) 
