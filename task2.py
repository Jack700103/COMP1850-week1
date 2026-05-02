def main():
    user_input = input().strip()
    try:
        monthly = int(user_input)
    except ValueError:
        print("Invalid amount")
        return

    annual_savings = monthly * 12
    interest = annual_savings * 0.008
    total = annual_savings + interest

    print(annual_savings)
    print(total)

if __name__ == "__main__":
    main()
