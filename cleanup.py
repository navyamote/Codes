# import regular expression processor for string cleanup
import re
 
string1 = "this, is a string, with commas; 12,345.67"
print(string1)
string1 = string1.replace(',', '')
print(string1)
print()

string2 = "this is   a   string    with     extra     spaces"
print(string2)
string2 = re.sub(r' +', ' ', string2)
print(string2)
print()

string3 = "this is\n a string\n with newlines"
print(string3)
string3 = string3.replace('\n', '')
print(string3)

