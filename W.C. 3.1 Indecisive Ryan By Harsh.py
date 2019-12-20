m = int(input("Please Enter The Value M : "))
n = int(input("Please Enter The Value N : "))
p = int(input("Please Enter The Value P : "))
mnList = list(range(m, n+1))
numberOfElements = len(mnList)
a = 0
for i in range(0, numberOfElements):
    mnListNumber = int(mnList[i])
    mnListNumberReverse = int(str(mnList[i])[::-1])
    answerInEachCase = (abs(mnListNumber - mnListNumberReverse))
    if answerInEachCase % p == 0:
        a = a + 1
print("The Number Of Magical Days In This Interval Are :",a,"Days.")






