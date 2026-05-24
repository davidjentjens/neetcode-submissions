class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}#{s}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            str_size_str = ""

            while s[i] != '#':
                str_size_str += s[i]
                i += 1
            i += 1

            str_size = int(str_size_str)
            current_string = s[i: i + str_size]
            i += str_size
            
            decoded_strs.append(current_string)

        return decoded_strs
            
                