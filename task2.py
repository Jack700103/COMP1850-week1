def main():
    try:
        monthly_savings = input("Enter the amount you want to save each month: ")

        monthly_savings = int(monthly_savings)

        annual_savings = monthly_savings * 12
        total_amount = annual_savings * 1.008  # 0.8% interest means multiply by 1.008

        print(f"You will save {annual_savings} per year.")
        print(f"You will have {total_amount:.2f} in total after 1 year including interest.")
        
    except ValueError:
        print("Invalid amount")

if __name__ == "__main__":
    main()