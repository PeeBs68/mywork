#calculate average

ages = [20, 30, 50]
incomes = [10000, 54000, 99090, 878888]

def calculateAverage(list):
    sum = 0
    for i in list:
        sum = sum + i
        print(sum)
    return sum/len(list)

print(calculateAverage(incomes))