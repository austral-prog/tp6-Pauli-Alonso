

def remove_elements(list):
     new_list = []
     if len(list) > 1:
          new_list += list[1:4]
     if len(list) > 6:
          new_list += list[6:]  


     return new_list


def add_elements(list_to_add_elements): 
     lista = ["Pink"] + list_to_add_elements
     lista.append("Yellow")
     return lista
       
def is_empty(list_to_check):    

     return len(list_to_check) == 0  


def check_lists(list_to_compare1, list_to_compare2):  
     if len(list_to_compare1) < 3 or len(list_to_compare2) < 3:
          return False  

     return list_to_compare1[2] == list_to_compare2[2]

def list_of_lists(list_of_lists_to_modify):         
     list_of_lists_to_modify[0] = list_of_lists_to_modify[0][:2] 
     list_of_lists_to_modify[1] =list_of_lists_to_modify[1][1:4]
     list_of_lists_to_modify[2] =list_of_lists_to_modify[2][-2:] 

     return list_of_lists_to_modify 
 
 
