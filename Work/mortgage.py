# mortgage.py
#
# Exercise 1.7
principal = 500_000.0
rate = 0.05
payment = 2_684.11
total_paid = 0.0
months_to_pay = 0

extra_payment_start_month = int(input("Start month = "))
extra_payment_end_month = int(input("End month = "))
extra_payment = int(input("Extra payment = "))

while principal > 0:
    months_to_pay += 1
    if extra_payment_start_month <= months_to_pay <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid += payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid += payment
    if principal < 0:
        total_paid += principal
        principal = 0
    print(f"{months_to_pay} {round(total_paid,2)} {round(principal,2)}")
        
print(f"Total paid  {round(total_paid,2)}")
print(f"Months to pay {months_to_pay}")
