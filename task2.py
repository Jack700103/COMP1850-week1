def main():
    try:
        monthly_input = input().strip()

        if monthly_input == "":
            raise ValueError

        monthly_savings = int(monthly_input)

        annual_savings = monthly_savings * 12
        total_amount = annual_savings * 1.008  # 0.8% interest

        print(annual_savings)
        print(f"£{total_amount:.2f}")
        
    except ValueError:
        print("Invalid amount")

if __name__ == "__main__":
    main()