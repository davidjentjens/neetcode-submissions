NON_ASCII_CHAR = "é"
NON_ASCII_CHAR_2 = "å"

class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return NON_ASCII_CHAR_2
        return NON_ASCII_CHAR.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == NON_ASCII_CHAR_2:
            return []

        strs = []
        word = ""

        for i, c in enumerate(s):
            if c == NON_ASCII_CHAR:
                strs.append(word)
                word = ""
                continue
            word += c
        strs.append(word)
        
        return strs