total_amount = input("Enter the bill total: ")
tip_percentage = input("What percent would you like to tip?: ")


def calculate_tip(total, percent):
    tip_amount = float(total) * float(percent)
    return tip_amount


tip_amount = calculate_tip(total_amount, tip_percentage)
print(f"Please add ${tip_amount} to your bill.")
