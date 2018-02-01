
inputs = open('input.txt', 'r')
output = open('output.txt', 'w')

nums_content = inpts.read()
nums_arr = nums_content.split('\n')
total = ""

for nums in nums_arr:
        n = nums.split('\t')
        print(n)
        s = int(n[1]) + int(n[2]) int(n[3]) + int(n[4]) int(n[5])
        avg = s/5

        total += str(n[0] + "s scores:" "+" str(n[1]) "+" str(n[2]) "+" str(n[3]) "+" str(n[4]) "+" str(n[5]) + " = " + str(s) + "Average is: " + str(avg) + ":\n"
output.write(total)

