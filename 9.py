# NOT-WORKING
file_path = "FILE_PATH"

c = 0
with open(file_path) as file:
    for line in file:
        line = line.split()
        line = list(map(int, line))
        total_sum = sum(line)
        counter = 0
        for i in range(4):
            for j in range(i + 1, 5):
                if line[i] ** 3 + line[j] ** 3 > (total_sum - line[i] - line[j]) ** 2:
                    counter += 1

        if counter == 10:
            c += 1

print(c)
