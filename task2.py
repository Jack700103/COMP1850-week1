def main():
    try:
        monthly_savings = input()

        monthly_savings = int(monthly_savings)

        annual_savings = monthly_savings * 12
        total_amount = annual_savings * 1.008  # 0.8% interest

        print(f"{annual_savings}")
        print(f"£{total_amount:.2f}")
        
    except ValueError:
        print("Invalid amount")

if __name__ == "__main__":
    main()