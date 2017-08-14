class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.price = price
        self.special = special
        self.needs = needs
        self.getValidOffers()

    



s = Solution()
price = [2,3,4]
special = [[1,1,0,4],[2,2,1,9]]
needs = [1,2,1]
s.shoppingOffers(price, special, needs)

