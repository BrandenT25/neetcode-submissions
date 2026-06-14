class Solution {
public:
    int maxProfit(vector<int>& prices) {
        std::unordered_map<size_t, int> priceMap;
        for(const int& num: prices){
            int topProfit{0};
            int minPrice{10000};
            for(const auto& price: prices){
                int currentProfit = price - minPrice;
                if (price < minPrice) minPrice = price;
                if (currentProfit > topProfit) topProfit = currentProfit;
            }
            return topProfit;
        }
    }
};
