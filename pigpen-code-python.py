def key():
  a="_|"
  b="|_|"
  c="|_"
  d="]"
  e="[]"
  f="["
  g="-|"
  h="|-|"
  i="|-"
  j="._|"
  k="|._|"
  l="|._"
  m=".]"
  n="[.]"
  o="[."
  p=".-|"
  q="|.-|"
  r="|.-"
  s="v"
  t=">"
  u="<"
  v="^"
  w=".v"
  x=".>"
  y=".<"
  z=".^"

def main():
message = input()
for letter in message:
   letter = letter.lower()
   message.append(key.get(letter, letter))
   return ''.join(message)
main()
