
inputs = open('input.txt', 'r')
output = open('output.txt', 'w')

nums_content = inpts.read()
nums_arr = nums_content.split('\n')
total = ""

for nums in nums_arr:
        n = nums.split(' ')
        s = int(n[0]) + int(n[1])
        total += str(n[0] + " + " + str(n[1]) + " = " + str(s) + "\n"
output.write(total)
