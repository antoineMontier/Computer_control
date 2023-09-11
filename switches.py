start_switch = "<Switch\nandroid:id=\"@+id/switch"
end_switch = "\"\nandroid:layout_width=\"wrap_content\"\nandroid:layout_height=\"wrap_content\"\nandroid:text=\"add_text\"\nandroid:checked=\"true\"\nandroid:textOn=\"ON\"\nandroid:padding=\"20dp\"\nandroid:thumbTint=\"#FFFF00\"\nandroid:trackTint=\"#FFFF00\"/>"

nb_switch = 276 # 276 = 1104 / 4
file = open("res_switch.txt", "w")

for i in range(nb_switch):
    file.write(start_switch + str(i) + end_switch)
    file.write("\n\n")

file.close()
