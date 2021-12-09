
def remove_characters(string, *args):
    for s in args:
        string = string.replace(s, "")
    return string
