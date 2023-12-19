file_path = "YOUR FILE PATH"


counter = 0
minn = 100000
min_sum = 200000
maxx = 0
lines = list()
with open(file_path) as f:
    for line in f:
        line = int(line.rstrip("\n"))
        if line != 8 and line % 8 == 0 and line < minn:
            minn = line
        lines.append(line)

for i in range(len(lines) - 1):
    a, b = lines[i], lines[i + 1]
    if a % minn == 0 and b % minn == 0:
       counter += 1
       if (a + b) < min_sum:
           min_sum = a + b
           maxx = max(a, b)

print(counter, maxx)