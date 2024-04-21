import random

def generate_random_code():
    code = 'L-' + ''.join(random.choice('0123456789') for _ in range(9))
    return code

# Example: Generate a random code of 10 digits starting with 'L'
random_code = generate_random_code()
print("Random code:", random_code)

