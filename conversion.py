def convert_rub_to_gbp(amount, rate = 100):
    return amount / rate

def convert_and_sum_list(rub_list, rate = 100):
    total = 0
    for amount in rub_list:
        total += convert_rub_to_gbp(amount, rate=rate)
    return total
print(convert_and_sum_list([10000, 32500]))

def convert_and_sum_list_kwargs(rub_list, **kwargs):
    total = 0
    for amount in rub_list:
        total += convert_rub_to_gbp(amount, **kwargs)
    return total
print (int(convert_and_sum_list_kwargs([10000, 32500], rate = 100)))
