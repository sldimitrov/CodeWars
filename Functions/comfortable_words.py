def comfortable_word(word):
    left, right = "qwertasdfgzxcvb", "yuiophjklnm"
    l = True if word[0] in left else False

    for letter in word[1:]:
        if letter in left and l:
            return False
        if letter in right and not l:
            return False
        l = not l
    return True
