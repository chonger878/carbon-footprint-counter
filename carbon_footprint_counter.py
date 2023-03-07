def main():
    print("So, how much carbon footprint did you make today?")
    getSum = 0
    int1 = int(input("How many days this week did you drive a car?"))
    getSum =sum(getSum,int1)
    print(getSum)
    int2 = int(input("How many days this week did you throw away food?"))
    getSum= sum(getSum, int2)
    print(getSum)
    yesOrNo1 = input("Did you turn off the lights every time you leave empty rooms?")
    getSum =subtractScore(yesOrNo1,getSum)
    yesOrNo2 = input("Did you work completely remote this week?")
    getSum = subtractScore(yesOrNo2, getSum)
    print(getSum)
    int3 = int(input("How many days did you use public transportation?"))
    getSum = sum(getSum, int3)
    score(getSum)

def sum(num,addNum):
    return num + addNum 

def subtractScore(yesOrNo1, score):
    if yesOrNo1.casefold() == 'yes':
        return score-1
    elif yesOrNo1.casefold() == 'no':
        return score + 7

def score(score):
    if score >= 18:
        print("Gotta work on reducing your carbon footprint!")
    elif score < 18:
        print("Doing good!")
    
if __name__ == "__main__":
    main()
