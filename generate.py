import os
def mai():

    with open('pose.txt', 'w') as fout:
        for i in range(1,50):
            fout.write("{} {} {}\n".format(i, random.randint(0,50), random.randint(0,1)))
