#8. Tennis Ranklist

tournamentsNum = int(input());
initialPoints = int(input());

#•	Tournament stage reached – string – "W", "F" or "SF"
stage = ""
points = 0;
stageCount = 0
winnerCount = 0;
for i in range(1, tournamentsNum + 1):
    stage = input();
    if(stage == "W"):
     points += 2000;
     stageCount += 1
     winnerCount +=1
    if(stage == "F"):
     points += 1200;
     stageCount += 1
    if(stage == "SF"):
     points += 720
     stageCount += 1

totalPoints = initialPoints + points;
averagePoints = points // stageCount
totalWin = (winnerCount/stageCount) * 100

print(f"Final points: {totalPoints}")
print(f"Average points: {round(averagePoints)}")
print(f"{totalWin:.2f}%");
