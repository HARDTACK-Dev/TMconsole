# input dump Analyzer (more informative version)

print("Input Dumper")
print("------------")

file_path = input("Choose File (path):\n")

if file_path.endswith(".txt") is False:
    print("\nSorry, It's only support .txt files")
    exit()

with open(file_path, 'r') as file:
    raw_lines = file.readlines()
    lines = [lines.strip() for lines in raw_lines]

    accel_duration = {}  # number of press up / values
    a1 = []

    # search for press up keywords, get accelerated seconds
    for i in range(len(lines)):
        if "press up" in lines[i]:
            accel_duration[i] = lines[i].split("-")

            pressUp_start = int(accel_duration[i][0])
            pressUp_end = int(accel_duration[i][1][:-9])

            print("[Acceleration]: " + str((pressUp_end - pressUp_start) / 1000) + "s")


            a1[i] = str((pressUp_end - pressUp_start)/1000)

            pressUp_start = 0
            pressUp_end = 0

    print("[Release]: " + str(a1[1] - a1[0]) + "s")