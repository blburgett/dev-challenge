# Exercises for chapter 2:

# Name: Bonnie Burgett

# 2.1
#The leading '0' switches the numeral system to a octal based system. 1114 is decimal system value for 02132 in the octal system.

#2.2
#In the interpreter the answers 5 prints out when 5 is entered, nothing prints out when x=5 is entered, and 6 prints out when x+1 is entered.

5
x=5
x+1

#There is no output when this is run except to see that it finished in 0.0s.

print '5'
x=5
print 'x=5'
print 'x+1='
print x+1

#2.3
width = 17
height = 12.0
delimiter = '.'

#2.3.1
answer = width/2
print answer
print type (answer)
#output is 8 and 'int'

#2.3.2
answer2 = width/2.0
print answer2
print type (answer2)
#output 8.5 and 'float'

#2.3.3
answer3 = height/3
print answer3
print type (answer3)
#output is 4.0 and 'float'

#2.3.4
answer4 = 1+2*5
print answer4
print type (answer4)
#output is 11 and 'int'

#2.3.5
answer5 = delimiter*5
print answer5
print type (answer5)
#output is '....' and 'str'

#2.4
#2.4.1
r=5
volume=(4.0/3.0)*3.14159*(r**3.0)
print volume
# answer is 523.598333 - must make the numbers floats instead of integers for floor division

#2.4.2
price = 24.95
discount = 0.40
shipping1 = 3.00
shipping2 = 0.75
order = 60
cost = (shipping1+shipping2*(order-1))+(price*order*(1-discount))
print cost
#answer = $945.45

#2.4.3
pace = 8.0+(15.0/60.0)
tempo = 7.0+(12.0/60.0)
pace_miles = 2
tempo_miles = 3
minutes = (pace * pace_miles)+(tempo*tempo_miles)
min_after7 = minutes - 8
mins2 = int(min_after7)
seconds = (min_after7-mins2)*60
print mins2
print 'minutes and'
print seconds
print 'seconds after 7 oclock am'
#answer = 7:30 and 6 seconds










