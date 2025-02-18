class Match():
    def __init__(self, rest):
        self.rest = rest if rest is not None else Null()

    def match(self, text):
        result = self._match(text, 0)
        return result == len(text)


class Null(Match):
    def __init__(self):
        self.rest = None

    def match(self, text, start):
        return start

class Lit(Match):
    def __init__(self,char,rest=None):
        super().__init__(rest)
        self.chars = chars 

    def _match(self,text,start):
        end = start + len(self.chars)
        if text[start:end] !=  self.chars:
            return None 
        return self.rest._match(text,end)
