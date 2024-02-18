'''
Given an integer between 0 and 26, make a variable (self.answer). That variable would be assigned to a string in this format:

"nines:your answer, threes:your answer, ones:your answer"
You need to find out how many ones, threes, and nines it would at least take 
for the number of each to add up to the given integer when multiplied by one, three or nine (depends).

Examples
ones_threes_nines(10) ➞ "nines:1, threes:0, ones:1"

ones_threes_nines(15) ➞ "nines:1, threes:2, ones:0"

ones_threes_nines(22) ➞ "nines:2, threes:1, ones:1"

'''

class ones_threes_nines():
    def __init__(self, num):
        self.answer = " "
        count_9 = count_3 = count_1 = 0
        if num >= 9:
            count_9 = int(num/9)
            num = num%9
        if num >= 3:
            count_3 = int(num/3)
            num = num%3
        if num >= 1:
            count_1 = int(num/1)
            num = num%1
        self.answer = f"nines:{count_9}, threes:{count_3}, ones:{count_1}"
        print(self.answer)

ones_threes_nines(1)
ones_threes_nines(5)
ones_threes_nines(7)
ones_threes_nines(10)
ones_threes_nines(12)
ones_threes_nines(15)
ones_threes_nines(22)
ones_threes_nines(25)
