# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        results = []
        for word in word_list:
            if self.is_anagram(word):
                results.append(word)
        return results

    def is_anagram(self, other_word):
        word_list = sorted(list(self.word))
        other_word_list = sorted(list(other_word))
        return word_list == other_word_list