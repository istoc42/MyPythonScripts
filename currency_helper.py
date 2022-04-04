def convert_currency(amount, rate, margin = 0):
    return amount * rate * (1 + margin)

def compute_gbp_total(amount_in_rub = 0, amount_in_gbp = 0):
    total = 0
    total += convert_currency(amount_in_rub, 0.01)
    total += convert_currency(amount_in_gbp, 100, 0.1)
    print(total)
    
compute_gbp_total(amount_in_gbp = 10)
compute_gbp_total(amount_in_rub = 100)
compute_gbp_total(amount_in_rub = 13520)
compute_gbp_total(amount_in_gbp = 120.75)

