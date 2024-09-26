from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        answer = []
        products.sort()
        l, r = 0, len(products) - 1
        for i in range(len(searchWord)):
            c = searchWord[i]

            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1

            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1

            suggestions = []
            for j in range(min(3, r - l + 1)):
                suggestions.append(products[l + j])
            answer.append(suggestions)

        return answer
