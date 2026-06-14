class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_string;
        for(const auto& s : strs){
            encoded_string += to_string(s.length()) + "#" + s;
        }
        return encoded_string;
    }

    vector<string> decode(string s) {
        std::vector<string> decoded_strings;
        int i = 0;
        while(i < s.length()){
            int j = s.find("#" , i);
            int length = std::stoi(s.substr(i, j - i));
            string word = s.substr(j+1, length);
            decoded_strings.push_back(word); 
            i = j + 1 + length;
        }
        return decoded_strings;
    }
};
