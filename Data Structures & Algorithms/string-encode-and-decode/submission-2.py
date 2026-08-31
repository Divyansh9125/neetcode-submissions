class Solution:

    # bruteforce:
    ## each character can be represented as 3-digit ASCII value
    ## 1. Convert each character to it's corresponding 3 digit ASCII Code
    ## 2. concatinate these code as characters and when there is a break, add '999' to represent the break
    ## 3. in the decoder step, take chunks of 3 characters from that encoded string and convert that to character, if there is '999', break the string.

    # improved
    ## key idea: we don't need to encode the individual strings.. they can be sent as they are.. we just need to figure out where each of the string were in original list at decode step
    ## 1. make a hash_map: key: individual string, value: list of its positions in the original list
    ## 2. compute the len of str (which is always < 200) and append it as 3-chars before the str, also get the chars of that value list with \n as delimiter
    def encode(self, strs: List[str]) -> str:
        ## Convert each character to it's corresponding 3 digit ASCII Code
        def _stringify(int):
            if len(str(int)) == 1:
                return "00"+str(int)
            if len(str(int)) == 2:
                return "0"+str(int)
            return str(int)

        def _stringifyv2(pos: List) -> str:
            _str = ""
            for num in pos:
                _str += str(num)+"|"
            return _str

        # concatinate these code as characters and when there is a break, add '999' to represent the break
        pos = {}
        for idx, _str in enumerate(strs):
            if _str not in pos.keys():
                pos[_str] = [idx]
            else:
                pos[_str].append(idx)
        print(pos)
       
        _encoded_str_list = ""
        print(f'Encoded str: {_encoded_str_list}')
        const = "00000"
        for _str in pos.keys():
            _encoded_str_list += _stringify(len(_str)) + _str
            print(f'Encoded str: {_encoded_str_list}')
            _str_pos_list = _stringifyv2(pos[_str])
            _encoded_str_list +=  const[:len(const) - len(str(len(_str_pos_list)))] + str(len(_str_pos_list))
            print(f'Encoded str: {_encoded_str_list}')
            _encoded_str_list += _str_pos_list
        print(f'Encoded str: {_encoded_str_list}')
        return _encoded_str_list

    def decode(self, s: str) -> List[str]:
        # in the decoder step, take chunks of 3 characters from that encoded string and convert that to character, if there is '999', break the string.
        idx = 0
        pos = {}
        _max_len = 0
        while idx < len(s):
            _len_of_string = s[idx:idx+3]
            _len_of_string = int(_len_of_string)
            idx += 3

            _str = s[idx:idx + _len_of_string]
            idx += _len_of_string

            _len_of_pos_list = s[idx:idx+5]
            _len_of_pos_list = int(_len_of_pos_list)
            idx += 5

            _pos_list = s[idx:idx + _len_of_pos_list]
            print(_pos_list)
            _pos_list = _pos_list.split('|')
            print(_pos_list)
            _pos_list_int = [int(_pos) for _pos in _pos_list if _pos != '']
            idx += _len_of_pos_list

            if max(_pos_list_int) > _max_len:
                _max_len = max(_pos_list_int)
            pos[_str] = _pos_list_int
        
        print(_max_len)
        if not pos:
            return []
        _str_list = [""]*(_max_len+1)
        print(_str_list)
        for _str in pos.keys():
            for idx in pos[_str]:
                print(f'idx: {idx}')
                _str_list[idx] = _str
            
        return _str_list
