#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/bon-appetit
"""

itens_and_skipped_item = input().split(" ")
prices_input = input().split(" ")
price_paid_input = input().split(" ")

itens_ordered = itens_and_skipped_item[0]
ana_skipped = itens_and_skipped_item[1]

itens_price = [int(x) for x in prices_input]
price_each_paid = [int(x) for x in price_paid_input][0]

itens_price.pop(int(ana_skipped))
shouldve_paid = int(sum(itens_price)/2)

if shouldve_paid == price_each_paid:
    print("Bon Appetit")
else:
    print(price_each_paid - shouldve_paid)
