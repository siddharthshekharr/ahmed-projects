def recursive_length(lst):
    # Base Case
    if lst == []:
        return 0
    
    # Recursive Case
    else:
        return 1 + recursive_length(lst[1:])

print(recursive_length(["L", "m", "n", "o"]))

list = ["apple", "mango", "banana", "pear"]
list2 = list[1:] # ["mango", "banana", "pear"]
list3 = list[2:] # ["banana", "pear"]
list4 = list[3:] # ["pear"]
list5 = list[4:]