first_word = "Silent"
second_word = "Listen"

if sorted(first_word.lower()) == sorted(second_word.lower()):
    print(f"'{first_word}' и '{second_word}' являются анаграммами.")
else:
    print(f"'{first_word}' и '{second_word}' не являются анаграммами.")
