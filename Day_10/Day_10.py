# Functions with outputs

def format_name(f_name, l_name):
    """
    Takes a first and last name and formats it to return a title case version of the name.
    """
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    else:
        split_first_name = list(f_name.lower())
        split_first_name[0] = split_first_name[0].upper()
        split_last_name = list(l_name.lower())
        split_last_name[0] = split_last_name[0].upper()

        full_name = f"{''.join(split_first_name)} {''.join(split_last_name)}"

        return full_name


formatted_name = format_name("eRiC", "vanMEter")

print(formatted_name)
print(format_name("", ""))