listik = [2, 5, 2, 6, 5]

def duplic(lst):
    setik = set(lst)
    if len(setik) == len(lst):
        return True
    else:
        return False

print(duplic(listik))