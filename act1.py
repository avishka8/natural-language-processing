import re
p = re.compile('[a-e]')
print(p.findall("Bob, said Mr. Aldren soloman to go for a walk"))

import re
p = re.compile('\d')
print(p.findall("I visited to college at 9 A.M. on 10th June 2022"))
p = re.compile('\d+')
print(p.findall("I visited to college at 9 A.M. on 10th June 2022 "))

import re
p = re.compile('\w')
print(p.findall("He said * in some_lang."))
p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he \
said *** in some_language."))
p = re.compile('\W')
print(p.findall("he said *** in some_language."))

import re
p = re.compile("ba*")
print(p.findall("babaabbbaaa"))

from re import split
print(split('\W+', "Names, names , Names"))
print(split('\W+', "Name's names Names"))
print(split('\W+', "On 25th Jan 2025, at 02:50 PM"))
print(split('\d+', "On 25th Jan 2025, at 02:50 PM"))


import re
print(re.sub('ub', '~*', 'Subject has Uber booked already',

flags=re.IGNORECASE))

print(re.sub('ub', '~*', 'Subject has Uber booked already'))
print(re.sub('ub', '~*', 'Subject has Uber booked already',

count=1, flags=re.IGNORECASE))

print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam',

flags=re.IGNORECASE))


import re
print(re.escape("This is Awesome even 1 AM"))
print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))


import re
regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "I was born on June 24")
if match != None:
   print ("Match at index %s, %s" % (match.start(), match.end()))
   print ("Full match: %s" % (match.group(0)))
   print ("Month: %s" % (match.group(1)))
   print ("Day: %s" % (match.group(2)))
else:
    print ("The regex pattern does not match.")


import re
s = "start .learning NLP"
#without using \
match = re.search(r'.', s)
print(match)
#using \
match = re.search(r'\.', s)
print(match)


import re
string = "Write a pattern which places the first word of an English sentence in a register"
pattern = "[a-m]"
result = re.findall(pattern, string)
print(result)


import re
regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
for string in strings:
    if re.match(regex, string):
        print(f'Matched: {string}')
    else:
        print(f'Not matched: {string}')


import re
string = "Hello World!"
pattern = r"World!$"
match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")    


import re
test_string = '123abc456789abc123ABC'
pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)   