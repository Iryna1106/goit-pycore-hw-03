import random

def get_numbers_ticket(min, max, quantity):
    if not (1<= min <= max <= 1000):
        return []
    if not (min <= quantity <= max-min+1):
        return[]
    result = random.sample(range(min,max+1),quantity)
    return sorted (result)
print (get_numbers_ticket(1,49,6))
        