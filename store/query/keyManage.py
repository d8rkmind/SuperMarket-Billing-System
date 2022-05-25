keyvalues=['name','category','subcategory','amount']

def keys(value:dict)->bool:
    for key,_ in value.items():
        if key not in keyvalues and len(value) != 1:
            return False
    return True