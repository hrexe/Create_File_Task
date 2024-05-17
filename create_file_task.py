with open("original_text.txt", "w") as file:
    file.write("Fayl ugurla yaradildi !!!")
with open("original_text.txt", "r") as file:
    first_line = file.readline().upper()
with open("modified_text.txt", "w") as file:
    file.write(first_line)
