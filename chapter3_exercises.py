# Exercises for chapter 3:

# Name: Bonnie Burgett

#3.1

#Answer:
#Traceback (most recent call last):
#  File "<string>", line 1, in <module>
#NameError: name 'repeat_lyrics' is not defined

#3.2
#Traceback (most recent call last):
#  File "<string>", line 1, in <module>
#NameError: name 'repeat_lyrics' is not defined

#3.3
s=str
def right_justify(s):
    spaces_no=70-len(s)
    spaces=' '*spaces_no
    justify = spaces + s
    print justify

print right_justify('allen')

#3.4

#3.4.1
print '#3.4.1'
def do_twice(f):
	f()
	f()

def print_spam():
	print 'spam'

do_twice(print_spam)
#returns:
#spam
#spam

#3.4.2
print'#3.4.2'
def do_twice2(f, val):
	f(val)
	f(val)

def print_spam(spam):
	print spam

do_twice2(print_spam, 'spam')

#3.4.3
def print_twice(p):
	print p
	print p

#3.4.4
print '#3.4.4'
do_twice2(print_twice, 'spam')

#3.4.5
print '#3.4.5'
def do_four(f2, val2):
	do_twice2(f2, val2)
	do_twice2(f2, val2)

do_four(print_twice, 'spam')