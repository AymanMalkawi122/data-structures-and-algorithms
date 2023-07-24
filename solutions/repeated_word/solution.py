from solutions.hash_tables.solution import Hashtable
def repeated_word(input_string):
    
    word_table = Hashtable()

    input_string = input_string.lower()

    words = input_string.split()

    for word in words:
        if word_table.has(word):
            return word

        word_table.set(word, True)

    return None