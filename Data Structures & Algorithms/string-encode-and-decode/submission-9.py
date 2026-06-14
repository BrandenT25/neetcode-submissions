class Solution:

    def encode(self, strs: List[str]) -> str:
        send_string = ""
        for s in strs:
            send_string += str(len(s)) + "#" + s
        return send_string
    def decode(self, s: strs) -> List[str]:
        result_list = [];
        i=0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            
            word_start = j+1
            word_end = j + 1 + length
            word = s[word_start:word_end]
            result_list.append(word)
            i = word_end
        return result_list 
