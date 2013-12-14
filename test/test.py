#!/usr/bin/python2
from dragon import Dragon

of = "test-03.png"

d = Dragon(3)

for i in range(14):
    print "\n### ROUND {} ###\n".format(i)
    d.iterate()

d.write(of)


