#3.	Histogram

n = int(input())
p1Count = 0
p2Count = 0
p3Count = 0
p4Count = 0
p5Count = 0

for i in range(0, n):
    num = int(input())
    if num < 200:
        p1Count += 1
    elif 200 <= num <= 399:
        p2Count += 1
    elif 400 <= num <= 599:
        p3Count += 1
    elif 600 <= num <= 799:
        p4Count += 1
    elif num >= 800:
        p5Count += 1

sum1 = p1Count + p2Count + p3Count + p4Count + p5Count

print(f"{(p1Count * 100) / sum1:.2f}%")
print(f"{(p2Count * 100) / sum1:.2f}%")
print(f"{(p3Count * 100) / sum1:.2f}%")
print(f"{(p4Count * 100) / sum1:.2f}%")
print(f"{(p5Count * 100) / sum1:.2f}%")
