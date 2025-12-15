# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to encode or decode

print("************* Encode & Decode *************")

def encode():
 if(len(word)>=3):
  tmp=word.strip(word[0])+word[0]
  new_word="zedf"+tmp+"zedf"
  print("The encoded value is:",new_word)
 else:
  print(word[::-1])

def decode():
 if(len(word)<3):
  print(word[::-1])
 else:
  tmp=word[4:-4]
  new_word=tmp[len(tmp)-1]+tmp.strip(tmp[len(tmp)-1])
  print("The decoded value is:",new_word)

inp_tuple=("encode","decode","zedf")
inp=input("You want to 'Encode' or 'Decode':")
word=input("Enter a String:")

if inp=="encode" in inp_tuple:
 encode()

if inp=="decode" in inp_tuple:
 decode()
