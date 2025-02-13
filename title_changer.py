import os

# change the title that you want to create a file for
title = "605. Can Place Flowers13213"

# replace space and dot with underscore
formatted_title = title.replace(" ", "_").replace(".", "")

# add .py extension
filename = f"{formatted_title}.py"

# check if the file already exists
if os.path.exists(filename):
    print(f"file already existed: '{filename}'")
else:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Solution for `{title}`\n")
    print(f"File created cuccessfully: {filename}")
