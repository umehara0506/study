class Money:
    
    def __init__(self, amount:int, currency: str):
        if amount < 0:
            raise ValueError('金額が0以上ではありません。')

        if currency == None:
            raise ValueError('通貨を指定してください。')

        self.amount = amount
        self.currency = currency
    
    def add(self, other):
        if not isinstance(other, Money):
            raise TypeError('Moneyクラスを入力してください。')
        if self.currency != other.currency:
            raise ValueError('通貨単位が違います')
        
        added = self.amount + other.amount
        return Money(added, self.currency)


first_product = Money(2000, '円')
print(first_product.amount)


secound_product = Money(3400, '円')

total = first_product.add(secound_product)
print(total.amount)


# # currencyeエラー
# thier_product = Money(340, 'ドル')
# total = first_product.add(thier_product)


# TypeError
# total.add(200) 

