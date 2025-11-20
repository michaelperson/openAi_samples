

def calculate_totalRate(items, tax_rate=0.2):
    subtotal = sum(items)
    return subtotal * (1 + tax_rate)