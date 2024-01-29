# Link https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

'''
How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing)?
Three conditions must be met for a valid experiment:

    Float parameter "h" in meters must be greater than 0
    Float parameter "bounce" must be greater than 0 and less than 1
    Float parameter "window" must be less than h.

If all three conditions above are fulfilled, return a positive integer, otherwise return -1.
Note:

The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.
Examples:

- h = 3, bounce = 0.66, window = 1.5, result is 3

- h = 3, bounce = 1, window = 1.5, result is -1 

(Condition 2) not fulfilled).

'''
# My Answer
# def bouncing_ball(h, bounce, window):
#        mantul = h * bounce
#        pantulan = 0
#        j = []
#        if window < h > 0 and 1 > bounce > 0 and mantul <= window: 
#                 j.append(h)
#        else:
#         while  mantul > window :
#             mantul = h * bounce
#             if window < h > 0 and 1 > bounce > 0:
#                     pantulan += h * bounce // window
#                     h *= bounce
#                     j.append(h)
#             else:
#                 return -1
#        return len(j)*2-1

#  Best Practice
def bouncing_ball(h, bounce, window):
    if not 0 < bounce < 1: return -1
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or -1


print(bouncing_ball(2, 0.5, 1))