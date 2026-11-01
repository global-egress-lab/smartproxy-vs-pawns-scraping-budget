#!/usr/bin/env python3
"""
Smartproxy vs Pawns.app Scraping Budget Calculator 2026.
"""
import argparse

def calculate(monthly_gb):
    # Smartproxy: $7.00/GB payg, or $28/mo plan (4GB included, then $7/GB), $75/mo plan (15GB included = $5/GB)
    if monthly_gb <= 4:
        smart_cost = 28.0
    elif monthly_gb <= 15:
        smart_cost = 75.0
    else:
        smart_cost = 75.0 + (monthly_gb - 15) * 5.0

    # Pawns.app: Pay as you go $3.00/GB (or $2.50/GB for 10GB+)
    pawns_rate = 3.00 if monthly_gb < 10 else 2.50
    pawns_cost = monthly_gb * pawns_rate

    savings = smart_cost - pawns_cost

    print("=" * 60)
    print("Scraping Bandwidth Model: Smartproxy vs Pawns.app")
    print("=" * 60)
    print(f"Monthly Traffic Demand:  {monthly_gb} GB")
    print(f"Smartproxy Monthly Cost: ${smart_cost:.2f}/mo")
    print(f"Pawns.app Monthly Cost:  ${pawns_cost:.2f}/mo")
    print(f"Annual Savings:          ${savings * 12:.2f}/year")
    print("=" * 60)
    return savings

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Smartproxy vs Pawns Calculator")
    parser.add_argument("--monthly-gb", type=int, default=12)
    args = parser.parse_args()
    calculate(args.monthly_gb)
