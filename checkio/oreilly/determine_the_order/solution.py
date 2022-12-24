def determine_order(data):
    result = ""

    # Create a list of all unique letters which
    # appear somewhere in data, sorted in
    # alphabetical order
    letters = sorted(set("".join(data)))

    while letters:
        # We know a letter is next in the alphabet
        # if it is either at the beginning of a word,
        # or doesn't appear in it, for all words in data.
        # We do this for each of the letters, and then
        # check if there are any letters left again.
        for letter in letters:
            if all(word.startswith(letter) or letter not in word for word in data):
                result += letter
                letters.remove(letter)
                data = [word.replace(letter, "") for word in data]
                break
    return result
