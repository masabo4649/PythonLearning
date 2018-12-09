#####
####  Lesson 2 string operation
####

multiple_line_strings = """Line 1
Line 2
LIne 3"""
print (multiple_line_strings)

parrot = "Norwegian Blue"
print (len(parrot))
#print (parrot.len()) -- not valid
print (parrot.lower())
#print (lower(parrot)) -- not valid
print (parrot.upper())

pi = 3.14
int1 = 111
#print (len(int1))  -- does not work

ministry = "The Ministry of Silly Walks"
print (len(ministry))
print (ministry.upper())
print ("Spam " + "and " + "eggs")
print ("The value of pi is around " + str(pi))

day = 6
print ("03 - %s - 2019" %  (day))
# 03 - 6 - 2019
print ("03 - %02d - 2019" % (day))
# 03 - 06 - 2019


# python3 ではraw_input()ではなく、input()となる
name = input("What is your name? ")
quest = input("What is your quest? ")
color = input("What is your favorite color? ")

print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))
