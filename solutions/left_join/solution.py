def left_join(synonyms, antonyms):
    """
    Perform a left join operation on two hashmaps, 'synonyms' and 'antonyms'.

    Args:
        synonyms (Hashtable): The hashmap containing word strings as keys and their synonyms as values.
        antonyms (Hashtable): The hashmap containing word strings as keys and their antonyms as values.

    Returns:
        list: A list of lists representing the left join result, where each inner list contains:
            - The key from the 'synonyms' hashmap.
            - The synonym value associated with the key, or "NULL" if not present.
            - The antonym value associated with the key, or "NULL" if not present.
    """
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
