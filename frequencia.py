from collections import Counter


class Frequency:
    '''Check the frequency of characters and words in percentage'''

    def __init__(self, text):
        self._text = self.sanitize_text(text)

    def sanitize_text(self, text):
        return text.lower()

    def character_frequency(self):
        characters = Counter(self._text)
        total_characters = sum(characters.values())

        characters_frequency = [
            (character, float(f'{frequency / total_characters * 100 :.2f}')) for character, frequency in characters.items()]

        frequency = Counter(dict(characters_frequency))

        return frequency

    def word_frequency(self):
        words = Counter(self._text.split(' '))
        total_words = sum(words.values())

        words_frequency = [
            (character, float(f'{frequency / total_words * 100 :.2f}')) for character, frequency in words.items()]

        frequency = Counter(dict(words_frequency))
        return frequency

    def most_commom(self, frequency, amount):
        frequency = frequency.lower().strip()

        if(frequency == 'characters'):
            more_common = self.character_frequency()
        elif(frequency == 'words'):
            more_common = self.word_frequency()
        else:
            raise ValueError(
                'Verification accepts only two frequencies: words | characters')
        return more_common.most_common(amount)


text = 'Factory Method is to creating objects as Template Method is to implementing an algorithm. '


check = Frequency(text)

characters = check.character_frequency()
words = check.word_frequency()

most_common_characters = check.most_commom('characters', 3)
most_common_words = check.most_commom('words', 5)

print(most_common_words)  # [('to', 6.98), ('method', 4.65), ('is', 4.65)]
