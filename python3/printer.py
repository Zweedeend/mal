

def pr_str(value):
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "nil"
    if isinstance(value, type(lambda x:x)):
        return "#" + str(value)
    return str(value)
