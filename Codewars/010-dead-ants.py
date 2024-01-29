# Links https://www.codewars.com/kata/57d5e850bfcdc545870000b7/train/python

'''
An orderly trail of ants is marching across the park picnic area.

It looks something like this:

..ant..ant.ant...ant.ant..ant.ant....ant..ant.ant.ant...ant..

But suddenly there is a rumour that a dropped chicken sandwich has been spotted on the ground ahead. The ants surge forward! Oh No, it's an ant stampede!!

Some of the slower ants are trampled, and their poor little ant bodies are broken up into scattered bits.

The resulting carnage looks like this:

...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t

Can you find how many ants have died?
Notes

    When in doubt, assume that the scattered bits are from the same ant. e.g. 2 heads and 1 body = 2 dead ants, not 3


'''

# My Answer
# def dead_ant_count (ants):
#     ants = ants.split()
#     alive, La, Lb, Lc = 0,0,0,0
#     dead = 0
#     totalScattered = 0
#     for a in ants:
#         alive += a.count('ant')
#         La += a.count('a')
#         Lb += a.count('n')
#         Lc += a.count('t')
#         scattered = [La,Lb,Lc]
#         totalScattered = La + Lb + Lc
#     if totalScattered % 3 == 0:
#         dead = La - alive
#     else:
#         dead = max(scattered) - alive
#     return dead
   
# Best Practice
def dead_ant_count (ants):
    return max(ants.count('a'), ants.count('n'), ants.count('t')) - ants.count('ant')   

print(dead_ant_count('ant a ant anatttt'))