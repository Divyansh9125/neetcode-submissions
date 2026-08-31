class Solution:

    # bruteforce:
    ## each character can be represented as 3-digit ASCII value
    ## 1. Convert each character to it's corresponding 3 digit ASCII Code
    ## 2. concatinate these code as characters and when there is a break, add '999' to represent the break
    ## 3. in the decoder step, take chunks of 3 characters from that encoded string and convert that to character, if there is '999', break the string.
    def encode(self, strs: List[str]) -> str:
        ## Convert each character to it's corresponding 3 digit ASCII Code
        def _stringify(int):
            if len(str(int)) == 1:
                return "00"+str(int)
            if len(str(int)) == 2:
                return "0"+str(int)
            return str(int)

        # concatinate these code as characters and when there is a break, add '999' to represent the break
        _encoded_str_list = ""
        for _str in strs:
            _encoded_str = ""
            for ch in _str:
                code = ord(ch)
                _str_code = _stringify(code)
                _encoded_str += _str_code
            # print(f'Encoded str for {_str} is: {_encoded_str}')
            _encoded_str_list += _encoded_str + "999"
        # print(f'Completed Encoded str is: {_encoded_str_list}')
        return _encoded_str_list

    def decode(self, s: str) -> List[str]:
        # in the decoder step, take chunks of 3 characters from that encoded string and convert that to character, if there is '999', break the string.
        _str_list = []
        _str = ""
        for i in range(0, len(s), 3):
            _str_code = s[i:i+3]
            if _str_code == "999":
                _str_list.append(_str)
                _str = ""
            else:
                _str += chr(int(_str_code))
            
        return _str_list
