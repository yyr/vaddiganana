#!/usr/bin/env python

from datetime import date
from dateutil import parser

class interestCalculator(object):
    def __init__(self):
        self.principal = float(input("Enter Principal amount: "))
        self.rate = float(input("Enter annual interest rate: "))
        self.start_date = parser.parse(input("Start date DD-MM-YYYY: "), dayfirst=True)
        self.end_date = parser.parse(input("End date DD-MM-YYYY: "), dayfirst=True)
        # self.principal = float("1150000")
        # self.rate = float("24")
        # self.start_date = parser.parse("24/1/2019", dayfirst=True)
        # self.end_date = parser.parse("11/08/2019", dayfirst=True)

    def interest_calculator(self, days):
        daily_rate = self.rate / 365
        int_per_day = self.principal/100 * daily_rate
        return int(int_per_day * days)

    def calc_interest(self):
        days = (self.end_date - self.start_date).days
        print("no of days: ", days)
        self.interest = self.interest_calculator(days)

if __name__ == '__main__':
    ic = interestCalculator()
    ic.calc_interest()
    print("Interest accrued:", ic.interest)
