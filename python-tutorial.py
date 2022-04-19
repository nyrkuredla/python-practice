#### using Python as a calculator

2 + 2 # 4
50 - 5 * 6 # 20
8 / 5 # 1.6 - division always returns a floating point number

# integer numbers = int type; fractional/decimal = float -  more on numeric types later

# floor division - returning an integer result and discarding factions - use // operator

8 // 5 # 1

17 / 3 # 5.6666666666666667
17 // 3 # 5

# to return remainder use %
17 % 3 # 2

# use ** to calculate powers
2 ** 3 # 8
5 * 2 # 25

# operators with mixed operands convert integer to and return floating point:
4 * 3.75 - 1 # 14.0, not 14

# in interactive mode, the last printed expression is assigned to the variable _
print(_) # 14.0
# note: read-only; for pretty obvious reasons, don't use this to assign anything else to

### string theory

# strings can be enclosed in either single or double quotes
# \ escapes quotes
"spam eggs" # "spam eggs"
"doesn\'t" # "doesn't"
"\'Argh,\' she said" # "'Argh,' she said"

# in interactive mode, output is enclosed in quotes and special characters escaped with backslashes. input might look different (enclosing quotes), they are equivalent
# print() omits enclosing quotes and prints escaped/special characters:
print("\'Argh,\' she said") # 'Argh,' she said

# new line: \n
txt = "First line.\nSecond line."
txt # without print command, \n is included in the output
print(txt) # prints with the new line

# raw strings: what if I don't want to include \n in the output?
print("c:\some\name") # interprets \n as a new line
print(r"c:\some\name") # prints as entered

# string literals: expanding across multiple lines with """ or '''
# ends of lines are automatically included in the string; use \ to prevent this
print('''\
	Usage: thing [OPTIONS]
	-h				Display this usage message
	-H hostname		Hostname to connect to
	''') # does not include initial newline

# concatenating and multiplying strings - use same numeric operators
# 3 times "un" followed by "ium"
3 * "un" + "ium" # unununium

# two or more string literals next to each other are automatically concatenated
"Ry" "an" # Ryan

# useful when breaking/combining long strings
text = ('Put several strings within parentheses' ' to join them together')
print(text)

# auto concat doesn't work with variables
text ' in a phrase' # chucks an error
text + ' in a phrase' # add an operator and it works

## indexes
word = "Python"
word [0] # "P"
word [-1] # "n" - starts at the end, since -0 is the same as 0
word [-6] # "P" - back to the beginning

# slicing
word[0:3] # "Pyt"


