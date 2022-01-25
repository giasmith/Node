# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class HairNode:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
o1 = HairNode("Brazilian")
o2 = HairNode("Cambodian")
o3 = HairNode("Malaysian")

o1.nextval = o2
o2.nextval = o3

thisvalue = o1

while thisvalue:
    print(thisvalue.dataval)
    thisvalue = thisvalue.nextval


class linkedlist:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

hair = linkedlist()

hair.headval = HairNode("26 in")

e2 = HairNode("30 in")
e3 = HairNode("12 in")

# Link first Node to second node
hair.headval.nextval = e2
# Link second Node to third node
e2.nextval = e3

hair.listprint()