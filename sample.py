def getMean(numericValues):
    return sum(numericValues)/len(numericValues)

my_list = [1, 2, 3]
try:
    result = getMean(my_list)
except ZeroDivisionError as detail:
    print "Output #142 (Error): " + str(float('nan'))
    print "Output #142 (Error):", detail
else:
    print "Output #142 (The mean is):", result
finally:
    print "Output #142 (Finally): The finally block is executed every time"