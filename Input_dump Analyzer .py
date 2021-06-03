# input dump Analyzer (more informative version)

print("Input Dumper")
print("------------")

file_path = input("Choose File (path):")

if file_path.endswith(".txt") is False:
    print("\nSorry, It's only support .txt files")
    exit()

with open(file_path, 'r') as file:
    raw_lines = file.readlines()
    lines = [lines.strip() for lines in raw_lines]

    accel_duration = {}  # number of press up / values

    # search for press up keywords
    for i in range(len(lines)):
        if "press up" in lines[i]:
            accel_duration[i] = lines[i].split("-")

            pressUp_start = accel_duration[i][0]
            pressUp_end = accel_duration[i][1][:-9]

            print(pressUp_start + " " + pressUp_end)
