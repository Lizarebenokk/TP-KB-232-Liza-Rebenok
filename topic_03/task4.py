def bubble_sort(par):
    n = len(par)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if par[j] > par[j+1]: 
                par[j], par[j+1] = par[j+1], par[j]
                
    return par

def insert_and_sort(sorted_list, new_element):
    sorted_list.append(new_element)
    return bubble_sort(sorted_list)

sorted_list = [1, 3, 5, 7, 9]
new_element = 4
updated_list = insert_and_sort(sorted_list, new_element)
print(f"Позиція для вставки {new_element}, відсортований список: {updated_list}")
