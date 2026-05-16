with open(r'../files/24-384.txt') as file:
    data = file.readline()

dat = '***Z**ZZ*ZZZ**Z*****Z**Z*ZZZ'

data = data.replace('Z', 'Z Z')
data = data.split()
# print(data)
ans = 1000000000000
for i in range(len(data) - 268):
    line = ''.join(data[i:i+269]).replace('ZZ', 'Z')
    # print(line)
    ans = min(ans, len(line))


print(ans)