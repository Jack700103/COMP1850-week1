import sys

def calculate_savings():
    input_data = sys.stdin.read().strip()

    if not input_data or not input_data.replace('-', '').isdigit():
        print("Invalid amount")
        return
    
    try:
        monthly = int(input_data)
    except ValueError:
        print("Invalid amount")
        return

    annual = monthly * 12
    total = annual * 1.008

    print(f"Annual savings: £{annual}")
    print(f"Total with interest: £{total:.2f}")

calculate_savings()
