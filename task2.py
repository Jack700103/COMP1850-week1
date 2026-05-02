try:
    user_input = input()

    clean_input = user_input.strip()

    if not clean_input:
        raise ValueError

    monthly_savings = int(clean_input)

    annual_savings = monthly_savings * 12
    total_amount = annual_savings * 1.008  

    print(annual_savings)

    print(f"£{total_amount:.2f}")

except ValueError:
    print("Invalid amount")