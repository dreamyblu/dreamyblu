"""

THIS IS MYASCII.PY ! It contains the new function, 'ascii_drawing" which enables a way of
'visualizing' your boba drink! It also contains a new class, Cogs18, which just shows a
short and sweet message for those who grade my final. Thanks for everything!

"""
# this function opens up banner.txt, which contains the small ascii drawing of a boba cup
def ascii_drawing():
    f = open('banner.txt', 'r')
    content = f.read()
    print(content)
    
# this class, Cogs18, contains a function that offers a message
class Cogs18():

    def __init__(self, feelings = None, cogs = None):
        self.feelings = feelings
        self.cogs = cogs
        
# speaking_facts is a function that displays how I truly feel after finishing
# this project.
    def speaking_facts(self):
        if self.feelings == 'Happy' or self.cogs == 'Over':
            return 'COGS18 is over and I am happy! Thanks Professor, TAs, and IAs!'
        else:
            return 'COGS18 is over and I will miss it :('