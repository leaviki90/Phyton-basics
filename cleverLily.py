#4.	Clever Lily
age = int(input())
washMachinePrice = float(input())
toyPrice = int(input())
birthdayMoney = 10
toysCount = 0
money = 0

for i in range(1, age + 1):
    if i % 2 == 0:  #even birthdays
        money += birthdayMoney  #add money to total money from even birthdays
        money -= 1  #brother takes money
        birthdayMoney += 10
    else:  #odd birthdays
        toysCount += 1


totalMoney = money + toysCount * toyPrice

if totalMoney >= washMachinePrice:
    print(f"Yes! {(totalMoney - washMachinePrice):.2f}")
else:
    print(f"No! {(washMachinePrice - totalMoney):.2f}")
