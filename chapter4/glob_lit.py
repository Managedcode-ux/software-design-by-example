class Either:
    def __init__(self, left, right, rest=None):
        self.left = left
        self.right = right
        self.rest = rest

    def match(self, text, start=0):
        return self.left.match(text, start) or self.right.match(text, start)


class Any:
    def __init__(self, rest=None):
        self.rest = rest

    def match(self, text, start=0):
        if self.rest is None:
            # print("Inside rest is None condition")
            return True
        for i in range(start, len(text)):
            # print("Inside the condition where rest is NOT None")
            if self.rest.match(text, i):
                return True
        return False


class Lit:
    def __init__(self, chars, rest=None):
        self.chars = chars  # characters to be matched against
        self.rest = rest

    def match(self, text, start=0):
        # print("Match method from Lit called")
        end = start + len(self.chars)

        if text[start:end] != self.chars:
            return False
        if self.rest:
            return self.rest.match(text, end)

        # checking if we have traversed the whole user string
        return end == len(text)
