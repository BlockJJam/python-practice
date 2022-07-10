print(list(enumerate('abcde')))

class NumberSequence:
    def __init__(self, start = 0):
        self.current = start

    def next(self):
        current = self.current
        self.current += 1
        return current

seq = NumberSequence()
print(seq.next())
print(seq.next())

# li = list(zip(NumberSequence(),'abcde'))

class SequenceOfNumbers:
    def __init__(self, start = 0):
        self.current = start

    def __next__(self):
        current = self.current
        self.current += 1
        return current 

    def __iter__(self):
        return self
    
print(list(zip(SequenceOfNumbers(), 'abcde')))

# next()함수
word = iter('abced')
next(word)
next(word)
print(next(word))
next(word)
next(word)
print(next(word, 'default value'))

# generator 사용하기
def sequence(start = 0):
    while True:
        yield start
        start += 1


seq = sequence(5)
print(next(seq))
print(next(seq))