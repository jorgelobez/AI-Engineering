incomes = [1500, 2500, 1800, 3200, 2000]
customers = ["Maria", "James", "Sofia", "Daniel", "Emma"]

def calculate_payment(income):
    if income > 2000:
        return income * 0.1
    else:
        return 0

saved_payments = []

for i in range(5):
    print(customers[i])
    payment = calculate_payment(incomes[i])
    saved_payments.append(payment)
    print(payment)
total_payments = sum(saved_payments)
print(total_payments)

average_payment = total_payments / len(saved_payments)
print(average_payment)

highest_payment = max(saved_payments)
print(highest_payment)

lowest_payment = min(saved_payments)
print(lowest_payment)
   
