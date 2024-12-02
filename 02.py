cellák = [False] * 400

for lepes in range(1, 401):
    for i in range(lepes - 1, 400, lepes):
        cellák[i] = not cellák[i]

# Nyitott cellák megtalálása
nyitott_cellák = []
for i in range(400):
    if cellák[i]:
        nyitott_cellák.append(i + 1)

# Kiírjuk a nyitott cellák számát
print("A nyitott cellák:", *nyitott_cellák, sep=", ")
