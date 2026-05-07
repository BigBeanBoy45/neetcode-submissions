class Solution:

    delim:str = "#"

    def encode(self, strs: List[str]) -> str:

        res: str = ""
        for s in strs: res += str(len(s)) + self.delim + s
        return res
    # end encode
        



    def decode(self, s: str) -> List[str]:

        res: list[str] = []

        lag: int = 0
        i: int = 0
        while i < len(s):
            # capture chunk and append to output
            len_string: int = 0
            if s[i] == self.delim: 
                len_string = int(s[lag : i])
                res.append(s[i + 1: i + len_string + 1])
                i += len_string + 1
                lag = i
            else:
                # parse number for length of chunk
                i += 1

        return res
    # end decode