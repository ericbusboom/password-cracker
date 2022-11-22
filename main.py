
import string
from typing import List

class StrGen:

    state: List[int];

    def __init__(self, length: int):

        self.length = length
        self.chars = string.ascii_lowercase
        self.state = [0] * self.length
        self.done = False

    def __iter__(self):
        return self

    def __next__(self):

        if self.done:
            raise StopIteration

        v = ''.join([self.chars[i] for i in self.state])
        for i in range(self.length):
            if self.state[i] < len(self.chars) - 1:
                self.state[i] += 1
                return v
            else:
                self.state[i] = 0
        else:
            self.done = True
            return v

    # Generate the string recursively
    def gen(self, i: int, s: str):

        if i == self.length:
            yield s
            return

        for c in self.chars:
            yield from self.gen(i + 1, s + c)

# This class is constructed on the name of a has algorithm,
# and is used to check that a binary string is equal to a hashed
# clear text string
import hashlib

class HashChecker:
    def __init__(self, hash_name):
        self.hash_name = hash_name
        self.h = hashlib.new(hash_name)

    def check(self, clear_text, hashed_text):
        self.h.update(clear_text.encode())
        return self.h.hexdigest() == hashed_text

if __name__ == '__main__':
    l = list(StrGen(4))
    print(len(l))
    print(l[:5]+l[-5:])

    l = list(StrGen(4).gen(0, ''))
    print(len(l))
    print(l[:5]+l[-5:])



