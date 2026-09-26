from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        finale = ""
        for c in strs:
            finale += str(len(c)) + "#" + c
        print(finale)
        return finale

    def decode(self, s: str) -> List[str]:
        fin = []
        skip = 0
        for c in range(len(s)):
            if c < skip:  
                continue
            if s[c] == "#" and s[c - 1] != "#":
                start = c - 1
                # Bound start to skip so it doesn't bleed into digits of the previous string
                while start >= skip and s[start].isdigit():
                    start -= 1
                start += 1

                fin.append(s[c + 1 : c + 1 + int(s[start:c])])
                skip = c + 1 + int(s[start:c])
        return fin