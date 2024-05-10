from functools import partialmethod,partial
price=float(input('el precioes de :'))#solo input el precio
class SimpleOperations:
    def __init__(self,price,discount,tax_rate):
        self.price=price
        self.discount=discount
        self.tax_rate=tax_rate
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""
        return self.price-(self.price*self.discount)
    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""
        return self.price*self.tax_rate
    
# Crear una instancia de SimpleOperations
vat_tax= partial(SimpleOperations.calculate_tax(price,tax_rate= 0.15))#hago un pacial donde el tax rate es de 15%
twenty_percent_discount=partial(SimpleOperations.apply_discount(price, discount=0.2))#hago un parcial donde el descuento es de 20%
print('el descuento de tu producto con un 20 percent de descuento es de: ',twenty_percent_discount)
#hago un print de ambos parciales
print('el importe incluido en el precio es de: ',vat_tax)
# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
# twenty_percent_discount 
# vat_tax

# Usar las funciones preconfiguradas.
