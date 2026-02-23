with open("first_file.txt", "r") as f:
    for line in f:
        print(f"Обрабатываю строку: {line.strip()}")
