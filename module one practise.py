def obrabotka(list)
    list_copy = list[:]
    list_copy = list_copy.append(99)
    return(list_copy)

original = [1, 2, 3]
new_list = obrabotka(original)
print(original)
print(new_list)
print(original is new_list)