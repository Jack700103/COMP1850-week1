def calculate_savings():
    try:
        monthly = int(input("Enter monthly savings amount: "))
    except (ValueError, EOFError):
        print("Invalid amount")
        return

    annual = monthly * 12
    total = annual * 1.008

    print(f"Annual savings: ${annual}")
    print(f"Total with interest: ${total:.2f}")

calculate_savings()
