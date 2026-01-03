with open(r'.\files\24_9753.txt') as file:
    data = file.readline()

ans = 0
data =data.split('Y')
for i in range(len(data) - 150):
    text = 'Y'.join(data[i:i + 151])
    ans = max(ans, len(text))
print(ans)