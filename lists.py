

def remove_elements(list_to_remove_elements):
    
     list_to_remove_elements: ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']  
     list_to_remove_things.remove("Red","Pink","Yellow") 
     return 
           list_to_remove_elements

#Expected Output : ['Green', 'White', 'Black']


def add_elements(list_to_add_elements): 
     list_to_add_elements = ['Red', 'Green', 'White', 'Black'] 

     list_to_add_elements.insert("Pink ")
     list_to_add_elements.append("Yellow") 

     return 
             list_to_add_elements  

    print(add_elements(list_to_add_elements))

#Expected Output : ['Pink', 'Red', 'Green', 'White', 'Black', 'Yellow']


def is_empty(list_to_check):    

     list_to_check = ["Green", "White", "Black"]
     return len(list_to_check) == 0  

     print(is_empty(list_to_check)) 


def check_lists(list_to_compare1, list_to_compare2): return
    
     list_to_compare1 = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
     list_to_compare2 = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']

     if len(list_to_compare1) < 3 or len(list_to_compare2) < 3:
        return False  

     return list_to_compare1[2]==list_to_compare2[2]

     print(check_lists(list_to_compare1, list_to compare2)) 




def list_of_lists(list_of_lists_to_modify):  

    list_of_lists_to_modify = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]] 
       
    list_of_list_to_modify[0] = list_of_lists_to_modify[0],[:2] 
    list_of_lists_to_modify[1] =list_of_lists_to_modify[1],[1:4]
    list_of_lists_to_modify[2] =list_of_lists_of_modify[2],[-2:] 

     return list_of_lists_to_modify 
 
 list_of_lists(list_of_lists_to_modify) 
 
