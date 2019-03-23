class BasketService(object):
    def __init__(self, sku_service):
        self.sku_service = sku_service

    def validate_basket(self, basket_string):
        """ Validates each letter in the basket string and returns true if all letters refer to a sku """
        if basket_string is None or not isinstance(basket_string, str):
            return False # this isn't even a proper string

        return True # just for now