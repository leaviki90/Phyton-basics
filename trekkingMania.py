#7. Trekking Mania

numberOfGroups = int(input())
firstGroup = 0;
secondGroup = 0;
thirdGroup = 0;
fourthGroup = 0;
fifthGroup = 0;
totalPeople = 0;

for i in range(1,numberOfGroups + 1):
    peopleInGroup = int(input());
    if peopleInGroup <= 5:
        firstGroup += peopleInGroup
    elif 6 <= peopleInGroup <= 12:
        secondGroup += peopleInGroup
    elif 13 <= peopleInGroup <= 25:
        thirdGroup += peopleInGroup
    elif 26 <= peopleInGroup <= 40:
        fourthGroup += peopleInGroup
    elif peopleInGroup >= 41:
        fifthGroup += peopleInGroup

totalPeople = firstGroup + secondGroup + thirdGroup + fourthGroup + fifthGroup;

print(f"{(firstGroup/totalPeople)*100:.2f}%");
print(f"{(secondGroup/totalPeople)*100:.2f}%");
print(f"{(thirdGroup/totalPeople)*100:.2f}%");
print(f"{(fourthGroup/totalPeople)*100:.2f}%");
print(f"{(fifthGroup/totalPeople)*100:.2f}%");