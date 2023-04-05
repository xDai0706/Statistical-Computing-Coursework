#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Xinqian Dai
"""

def compute_months(annual_salary, portion_saved, total_cost):
    """Compute the number of months needed to save."""
    r=0.04
    current_savings = 0
    portion_down_payment = 0.25
    down_payment = total_cost * portion_down_payment
    monthly_salary = annual_salary/12
    num_months = 0

    while current_savings < down_payment:
       current_savings = current_savings + current_savings * r/12 + monthly_salary*portion_saved
       num_months += 1

    # TODO: Implement me
    return num_months
    
    
if __name__ == "__main__":
    annual_salary = float(input("Enter your starting annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save , as a decimal :"))
    total_cost = float(input("Enter the cost of your house :"))
    # TODO: Implement me
    
    num_months = compute_months(annual_salary, portion_saved, total_cost)
    print("Number of months: %d" % num_months)

