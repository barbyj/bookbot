def num_of_words(text):
    words = text.split()
    return len(words)

def count_of_characters(text):
    list_of_characters = list(text.lower())
    count_of_characters = {}
    for char in list_of_characters:
        count_of_characters[char] = count_of_characters.get(char, 0) + 1
    return count_of_characters

def sort_on(items):
    return items["num"]

def sorted_list_of_characters(count_of_characters):
    result = []
    for char, count in count_of_characters.items():
        if char.isalpha():
            result.append({"char": char, "num": count})
    result.sort(key=sort_on, reverse=True)
    return result