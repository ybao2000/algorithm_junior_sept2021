import math
import matplotlib.pyplot as pyplot

# set up the lists
# xlist is [1, 2, 3, 4, ...100]
xlist = list(range(1, 101, 1))
labels = ['Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential', 'Factorial']
ylists = [] # this is a list of list
ylists.append([math.log2(x) for x in xlist])  # this is to generate the log(x)
ylists.append([x for x in xlist]) # this is x
ylists.append([x * math.log2(x) for x in xlist]) # x log x
ylists.append([x*x for x in xlist]) # x^2
ylists.append([x*x*x for x in xlist]) # x^3
ylists.append([2**x for x in xlist]) # 2^x
ylists.append([math.factorial(x) for x in xlist])  # x!

# plot setup
pyplot.figure(figsize = (12, 10))
pyplot.ylim(0, 10000)

for i in range(len(ylists)):
  pyplot.plot(xlist, ylists[i], label=labels[i])

pyplot.legend(loc=0)
pyplot.xlabel('n')
pyplot.ylabel('running time')
pyplot.show()