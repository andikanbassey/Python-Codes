with open ('input.txt', 'r') as inp:
  content =inp.readlines()
  total = int(content[0]) + int(content[1])

with open('output.txt', 'w') as out:
    out.write(content[0] +' + '+ content[1]+ '=' + str(total))

print(content)

with open('output.txt', 'r') as outr:
    content2 = outr.read()
    print(content2)
