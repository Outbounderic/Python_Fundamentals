# Functions with outputs

def format_name(f_name, l_name):
    split_first_name = list(f_name.lower())
    split_first_name[0] = split_first_name[0].upper()
    split_last_name = list(l_name.lower())
    split_last_name[0] = split_last_name[0].upper()

    full_name = f"{''.join(split_first_name)} {''.join(split_last_name)}"
    return full_name


formatted_name = format_name("eRiC", "vanMEter")

print(formatted_name)