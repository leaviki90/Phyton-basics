#2.	Half Sum Element
n = int(input());
largestNum = int(input());
sum1 = largestNum;

num = 0;
for i in range(1, n):
    num = int(input());
    sum1 += num;
    if(num > largestNum):
        largestNum = num;


if(largestNum == (sum1 - largestNum)):
    print("Yes");
    print(f"Sum = {largestNum}");
else:
    print("No");
    print(f"Diff = {abs(sum1 - largestNum - largestNum)}")