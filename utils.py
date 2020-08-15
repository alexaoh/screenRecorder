"Collection of utility functions that aren't a logical part of any other file."

import subprocess

def find_vacant_filename():
    "Find a name that is vacant in . directory. Counteracts overwriting old recordings."
    i = 1
    while True:
        find = "find . -name out"+str(i)+".mkv"
        search = subprocess.Popen(find.split(" "), stdout=subprocess.PIPE)
        out, err = search.communicate()
        if out.decode('ascii') == "":
            filename = "out" + str(i)
            break
        i = i + 1
    return filename
