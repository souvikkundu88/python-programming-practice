# updating a list via Function
my_list = [10, 20, 30, 40]
print(my_list)

def modify_list(num_list):
    num_list[0] *= 10
    num_list[1] *= 20
    num_list[2] *= 30
    num_list[3] *= 40
    #return num_list

modify_list(my_list)

print(my_list)
