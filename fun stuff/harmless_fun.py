import time
import random
import string
import os

def generate_registration_code():
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))
    return '-'.join([code[i:i+5] for i in range(0, len(code), 5)])

def load_balance_and_registration():
    try:
        with open("acc-info.txt", "r") as file:
            lines = file.readlines()
            balance_line = lines[0].strip()
            balance = float(balance_line.split(":")[1].strip().split()[0])
            registration_code = lines[1].strip().split(":")[1].strip()
            return balance, registration_code
    except FileNotFoundError:
        print("Account Infomation FILE not found. Starting with balance of 0.")
        return 0, generate_registration_code()

balance, registration_code = load_balance_and_registration()
while True:
    generated_amount = round(random.uniform(0.00001, 0.000090), 6)
    balance = round(balance + generated_amount, 6)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Balance: {balance:.6f}")
    print(f"Mined amount: {generated_amount:.6f}")
    print(f"Registration Code: {registration_code}")
    with open("acc-info.txt", "w") as file:
        file.write(f"Balance: {balance:.6f} RC\nRegistration Code: {registration_code}")
    
    for i in range(45, 0, -1):
        print(f"Next mine in {i} seconds...", end="\r")
        time.sleep(1)
    
    print()
