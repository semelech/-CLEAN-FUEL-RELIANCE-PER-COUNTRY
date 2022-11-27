class Invoice:
    def __init__(self):
        self.items = {}
    def addProducts(self, qnt, price, discount):
        self.items['qnt'] =qnt
        self.items['unit_price'] =price
        self.items['discount'] =discount
        self.items['pen'] =pen
        return self.items
    def totalImpurePrice(self, products):
        total_impure_price =0
        for k, v in products.items():
            total_impure_price += float(v['unit_price'])* int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price
    def totalDiscount(self, products):
        total_discount =0
        for k, v, in products.items():
         total_discount += (int(v['qnt']) * float(v['unit_price'])) * float(v['discount'])/100
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount

    def totalPurePrice(self, products):
      total_pure_price = self.totalImpurePrice(products)-self.totalDiscount(products)
      return total_pure_price
    def inputAnswer(self, input_value):
          while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
             return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
      while True:
        try:
             userInput = float(input(input_value))
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
             return userInput


    def totalCount(self, products): # function of the total number of quantities
        total_count = 0
        for k, v in products.items():
            total_count += (int(v['qnt']))  # calculate total quantity
            self.total_count = total_count   # return total quantity of product.
        return total_count

    def totalRoundImpurePrice(self, products): # function total product price and roundup to 2 decimal places
        total_round_impure_price = 0
        for k, v in products.items():
            total_round_impure_price += float(v['unit_price']) * int(v['qnt'])  # calculate total product price
        total_round_impure_price = round(total_round_impure_price, 2) # round the product price to decimal 2.
        return total_round_impure_price # return values of total product prices

    def totalunitprice(self, products):
        total_unit_price = 0
        for k, v in products.items():
            total_unit_price += float(v['unit_price'])
            self.total_unit_price = total_unit_price
        return total_unit_price

    def totalSalesTax(self, products):  # Function that calculates Sales Tax after discounts
        total_sales_tax = self.totalPurePrice(products) * .0475  # Sales tax of 4.75%
        total_sales_tax = int(total_sales_tax * 100) / 100
        total_sales_tax = round(total_sales_tax, 2)  # Rounding the amount to two decimals places
        return total_sales_tax  # return amount
