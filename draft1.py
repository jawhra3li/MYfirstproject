import os
folder ="C:/Users/DELL/Desktop/Jouhara/math"
for file_name in os.listdir(folder):
    f = open(folder + "/" + file_name, "r", encoding="utf-8")
    name = f.readline().strip()
    number = f.readline().strip()
    description = ""
    example = ""
    is_example = False  
    for line in f:
        line = line.strip()
        if "Example" in line:
            is_example = True
            continue   
        if is_example:
            example = example + " " + line
        else:
            description = description + " " + line
    print("Name:", name)
    print("Number:", number)
    print("Description:", description)
    print("Example:", example)
    print("----------------")
f.close()