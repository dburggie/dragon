#!/usr/bin/python2
from dragon import Dragon

of = "test-05.png"

d = Dragon(1)

for i in range(19):
    print "\n### ROUND {} ###\n".format(i)
    d.iterate()

d.write(of)


