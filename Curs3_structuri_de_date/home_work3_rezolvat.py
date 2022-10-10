print("Ex 1")
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(f"1: {note_muzicale}")
note_muzicale = note_muzicale[::-1]
print(f"2: {note_muzicale}")
note_muzicale.reverse()
print(f"3: {note_muzicale}")

assert note_muzicale == ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do'], "Notele muzicale nu coincid"

print("Ex 2: De cate ori apare 'do'? ")
count_do = note_muzicale.count('do')
print(f"'do' apare de {count_do}")
assert count_do == 2

print("Ex 3: liste list1 = [3, 1, 0, 2], list2 = [6, 5, 4]")
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]

list3 = list1 + list2
list1.extend(list2)

assert list3 == list1