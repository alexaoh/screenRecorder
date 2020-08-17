"""Collection of utility functions that aren't a logical part of any other file."""

import subprocess

def find_vacant_filename():
    """Find a name that is vacant in . directory. Counteracts overwriting old recordings."""
    i = 1
    while True:
        find = "find . -name out"+str(i)+".*"
        search = subprocess.Popen(find.split(" "), stdout=subprocess.PIPE)
        out, err = search.communicate()
        if out.decode('ascii') == "":
            filename = "out" + str(i)
            break
        i = i + 1
    return filename

def give_name_of_date():
    """Give name based on the week number and date."""
    echo_week_number = "echo $(date +%V)"
    week_query = subprocess.Popen(echo_week_number, stdout=subprocess.PIPE, shell=True)
    week_num = week_query.communicate()[0]

    echo_date = "echo $(date +%d/%m/%Y)"
    date_query = subprocess.Popen(echo_date, stdout=subprocess.PIPE, shell=True)
    date = date_query.communicate()[0]

    filename = "DiskMatUke" + week_num.decode('ascii')[:-1] + "_" + date.decode('ascii')
    
    return filename
