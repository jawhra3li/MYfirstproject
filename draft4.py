import os

folder = "C:/Users/DELL/Desktop/Jouhara/math"

for file_name in os.listdir(folder):
    f = open(folder + "/" + file_name, "r", encoding="utf-8")
    name = f.readline().strip()
    number = f.readline().strip()
    description = ""
    example = ""

    for line in f:
        line = line.strip()
        parts = line.split("Example")
        if len(parts) > 1:
            description += parts[0] + " "
            example += parts[1] + " "
        else:
            if example == "":
                description += line + " "
            else:
                example += line + " "

    print("Name:", name)
    print("Number:", number)
    print("Description:", description)
    print("Example:", example)
    f.close()