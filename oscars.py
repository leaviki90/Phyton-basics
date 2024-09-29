# 6.	Oscars
actorName = input()
academyPoints = float(input())
assessorsNumber = int(input())


if academyPoints > 1250.5:
    print(f"Congratulations, {actorName} got a nominee for leading role with {academyPoints:.1f}!")
else:

    for i in range(assessorsNumber):
        assessorsName = input()
        score = float(input())
        academyPoints += (len(assessorsName) * score) / 2

        if academyPoints > 1250.5:
            print(f"Congratulations, {actorName} got a nominee for leading role with {academyPoints:.1f}!")
            break

    if academyPoints <= 1250.5:
        print(f"Sorry, {actorName} you need {(1250.5 - academyPoints):.1f} more!")
