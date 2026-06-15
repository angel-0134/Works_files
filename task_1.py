with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

line_count = len(lines)

word_count = 0
for line in lines:
    word_count += len(line.split())

with open("statistics.txt", "w", encoding="utf-8") as file:
    file.write(f"Количество строк: {line_count}\n")
    file.write(f"Количество слов: {word_count}\n")
