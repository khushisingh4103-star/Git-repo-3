try:
    file = open("sample.txt", "r")
    print("Reading file content: ")

    line_num = 1
    for line in file:
        print(f"Line{line_num}: {line.strip()}")
        line_num += 1

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

