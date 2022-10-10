# for imbricat - for in for

hotel = {
    "parter": ["Birou management", "Toalete oaspeti", 10, 11, 12, 13, 14], # etaj parter
    "etaj 1": [20, 21, 22, 23, 24, 25, 26, 27], # etaj 1
    "etaj 2": [30, 31, 32, 33, 34, 35, 36, 37], # etaj 2
    "etaj retras": [40, 41, 42, 43] # ultimul etaj
}

for nume_etaj in hotel:
    print(f"Etaj nou: {nume_etaj}")
    for camera in hotel[nume_etaj]:
        print(f"    camera: {camera}")

# tabla inmultirii
for i in range(1, 11): # 0 1 2 3 4
    for j in range(1, 11): # 0 1 2 3
        print(f"{i} * {j} = {j * i}")
    print()