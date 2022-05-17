from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    """ Builds and returns the occurrence shift table """
    table = dict()
    for i in range(0, len(pattern)):
        table[pattern[i]] = max(1, len(pattern) - i - 1)
    return table


class Bm(object):
    """
    class Bm 
    Class that implements Boyer Moore String Search Algorithm.
    The algorithm scans the characters of the pattern from right to left beginning with the rightmost one, 
    uses a shift function window and aligns the pattern until it matches.

    Parameters
    ----------
    text: the input text to be matched
    pattern: the pattern to search in input text
    table: occurrence shift table
    """

    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)


    def decide_slide_width(self, c: str) -> int:
        """ Returns the shift corresponding with the current letter """
        assert len(c) == 1
        return self.table.get(c, 0)
        

    def search(self) -> int:
        """ Performs the BM algorithm given text and pattern, returns the first occurrence """
        i = len(self.pattern) - 1
        found = -1
        while i <= len(self.text) - 1:
            j = 0
            while j < len(self.pattern) and self.pattern[len(self.pattern) - j - 1] == self.text[i - j]: # loop if matches the whole pattern
                j += 1
            if j == len(self.pattern):
                found = i - len(self.pattern) + 1 # found, return occurrence index
                return found
            else:
                if i + j >= len(self.text):
                    # pattern was not found, e.g. both
                    # strings have same size
                    return found
                slide_width = self.decide_slide_width(self.text[i + j])
                # if not in the table use the pattern size
                if slide_width == 0:
                    slide_width = len(self.pattern) - 1
                slide = slide_width
                if slide_width != j:
                    slide -= j
                i += slide
        return found
