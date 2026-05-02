def main():
    user_input = input().strip()
    try:
        monthly_float = float(user_input)
        if not monthly_float.is_integer():
            print("Invalid amount")
            return
        monthly = int(monthly_float)
    except ValueError:
        print("Invalid amount")
        return

    annual_savings = monthly * 12
    interest = annual_savings * 0.008
    total = annual_savings + interest

    print(annual_savings)
    print(f"£{total:.2f}")

if __name__ == "__main__":
    main()
