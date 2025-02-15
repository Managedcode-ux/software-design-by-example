class Any:
    def __init__(self, rest=None):
        self.rest = None

    def match(self, text, start=0):
        if self.rest is None:
            return True
        for i in range(start, len(text)):
            if self.rest.match(text, i):
                return True
        return False


class Lit:
    def __init__(self, chars, rest=None):
        self.chars = chars  # characters to be matched against
        self.rest = rest

    def match(self, text, start=0):
        end = start + len(self.chars)

        if text[start:end] != self.chars:
            return False
        if self.rest:
            return self.rest.match(text, end)

        # checking if we have traversed the whole user string
        return end == len(text)
