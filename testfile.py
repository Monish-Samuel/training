class AlphaCheck:

    def __init__(self, sentence, word):
        self.sentence = sentence
        self.word = word

#This method is used to find the number of characters in a string without spaces
    def word_length(self, sentence):
        self.sentence = sentence
        r = self.sentence.replace(" ", "")
        size = len(r)
        print(f'The number of characters in "{sentence}" is {size}')

#This method for finding matching statement
    def matching_char(self, sentence, word):
        self.sentence = sentence
        self.word = word
        i = 0
        for char in self.sentence:
            if char == self.word:
                i += 1
        print(f'No. of {self.word} in "{self.sentence}" is {i}')

#This method is to reverse the string
    def reverse(self, sentence):
        self.sentence = sentence
        print('The reverse of String: ' +self.sentence[::-1])

#This method is to Capitalize all the characters in a string
    def capital_case(self, sentence):
        self.sentence = sentence
        print('Capitalized string: ' +self.sentence.upper())


n = True
while n:

    a = input('Enter the String: ')
    b = input('Enter the character to be counted (CASE SENSITIVE): ')
    result = AlphaCheck(a, b)

    result.word_length(a)
    result.matching_char(a, b)
    result.reverse(a)
    result.capital_case(a)

    print('Check new string? Y or N')
    c = input()
    if c.lower() == 'y':
        n = True
    else:
        n = False