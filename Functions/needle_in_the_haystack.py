def find_needle(haystack):
    for element in haystack:
        if element == 'needle':
            index = haystack.index(element)
    return_string = f"found the needle at position {index}"
    return return_string
