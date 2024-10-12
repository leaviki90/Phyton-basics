# 6.	Building

floorNumbers = int(input())
roomsPerFloor = int(input())

for floor in range(floorNumbers, 0, -1):
    for room in range(roomsPerFloor):
        if floor == floorNumbers:
            print(f"L{floor}{room}", end=" ")
        elif floor % 2 == 0:
            print(f"O{floor}{room}", end=" ")
        else:
            print(f"A{floor}{room}", end=" ")
    print()  # Ovaj print služi da pređe u novi red nakon što ispiše sve sobe za jedan sprat
