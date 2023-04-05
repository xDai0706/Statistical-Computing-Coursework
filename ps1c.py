#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:33:31 2023

@author: demix9
"""


def compute_rate(annual_salary):
    """Compute the savings rate needed"""
    semi_annual_raise = 0.07
    total_cost = 1000000
    bisection_count = 0
    current_savings = 0
    down_payment = 0.25 * total_cost
    low = 0
    high = 10000
    guess = (low + high) / 2
    rate = round(guess/10000,4)
    
    while abs (current_savings - down_payment) > 100:

        current_savings = total_savings(guess/10000, annual_salary, down_payment, semi_annual_raise)
        if (current_savings < down_payment):
            low = guess
        else:
            high = guess
        bisection_count = bisection_count + 1
        guess = (low + high) / 2
        rate = round(guess/10000,4)
        if rate >= 1.0:
            return None, None
    # TODO: Implement me
    return rate, bisection_count

def total_savings(rate, annual_salary, down_payment, semi_annual_raise):
    current_savings = 0
    monthly_salary = (annual_salary / 12)
    
    for i in range (36):
        if (i > 0 and i % 6 == 0):
            monthly_salary = monthly_salary + semi_annual_raise * monthly_salary 
        current_savings = current_savings+ current_savings * 0.04 / 12 +monthly_salary * rate

    return current_savings
    
    # TODO: Implement me
    
if __name__ == "__main__":
    annual_salary = int(input("Enter your starting annual salary: "))
    
    rate, bisection_count = compute_rate(annual_salary)
    if rate is None:
        print("It is not possible to pay the down payment in three years.")
    else:
        print("Minimal savings rate: %f" % rate)
        print("Steps in bisection search: %d" % bisection_count)
        
