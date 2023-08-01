def left_join(synonyms, antonyms):
    left_join_result = []
    for key in synonyms.keys():
        synonym_value = synonyms.get(key)
        antonym_value = antonyms.get(key)
        if synonym_value is None:
            synonym_value = "NULL"
        if antonym_value is None:
            antonym_value = "NULL"
        left_join_result.append([key, synonym_value, antonym_value])
    return left_join_result
