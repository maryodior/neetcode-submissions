class Solution:

    def encode(self, strs: List[str]) -> str:
        returnedString = ""
        for val in strs:
            strLen = len(val)
            val = "😂" + val
            returnedString += val
        returnedString.strip()
        return returnedString

    def decode(self, s: str) -> List[str]:
        if len(s) < 1:
            return []
        pieces = s.split("😂")
        pieces.pop(0)
        return pieces




