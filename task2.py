import sys

def main():
    try:
        line = sys.stdin.readline()

        monthly_input = line.strip()

        if not monthly_input:
            raise ValueError

        monthly_savings = int(monthly_input)

        annual_savings = monthly_savings * 12
        
        total_amount = annual_savings * 1.008

        print(annual_savings)

        print(f"£{total_amount:.2f}")
        
    except ValueError:
        print("Invalid amount")

main()