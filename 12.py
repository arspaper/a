counter = 0
for n in range(1, 101):
    line = "1" + "0" * n
    while "10" in line or "1" in line:
        if "10" in line:
            line = line.replace("10", "0001", 1)
        else:
            if "1" in line:
                line = line.replace("1", "0", 1)
    if len(line) % 7 == 0:
        counter += 1

print(counter)