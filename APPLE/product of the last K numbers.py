class ProductOfNumbers:
    def __init__(self):
        self.prefix_products = [1]  # Start with 1 for easier multiplication
        self.last_zero_index = -1   # Track last zero's position

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1]  # Reset prefix products after zero
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix_products):
            return 0
        return self.prefix_products[-1] // self.prefix_products[-k-1]
