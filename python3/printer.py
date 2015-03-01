

def pr_str(value):
    if isinstance(value, list):
        return "(" + " ".join(pr_str(item) for item in value) + ")"
    return str(value)
