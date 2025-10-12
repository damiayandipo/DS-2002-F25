import pandas as pd
import os
import sys

def generate_summary(portfolio_file):
    if not os.path.exists(portfolio_file):
        print(f"Error: File {portfolio_file} not found.", file=sys.stderr)
        sys.exit(1)
    
    df = pd.read_csv(portfolio_file)
    
    if df.empty:
        print("Portfolio is empty.")
        return
    
    total_portfolio_value = df['card_market_value'].sum()
    most_valuable_idx = df['card_market_value'].idxmax()
    most_valuable_card = df.loc[most_valuable_idx]
    
    print(f"Total Portfolio Value: ${total_portfolio_value:,.2f}")
    print(f"Most Valuable Card: {most_valuable_card['card_name']} (ID: {most_valuable_card['set_id']}-{most_valuable_card['card_number']}) - ${most_valuable_card['card_market_value']:,.2f}")

def main():
    generate_summary('card_portfolio.csv')

def test():
    generate_summary('test_card_portfolio.csv')

if __name__ == "__main__":
    test()