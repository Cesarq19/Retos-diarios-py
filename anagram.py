def anagrams(word, words):
    anagram = []
    for element in words:
        if len(element) == len(word):
            if sorted(word) == sorted(element):
                anagram.append(element)      
    return anagram