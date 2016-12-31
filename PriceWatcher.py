import InstanceTypes


class PriceWatcher:

    def __init__(self, prices):
       self.prices = prices

    def get_prices(self):
        """

        Returns:

        """
        return self.prices

    def set_prices(self, prices):
        self.prices = prices

    def get_cheapest_type(self):
        prices = self.price_watcher.get_prices()
        items = prices.items()
        e = list(items)[0]
        k = e[0]
        v = e[1]
        for (key, value) in items:
            if (value < v):
                k = key
                v = value
        return k