import numpy as ny

name=input("Enter your name")
name_parts=name.split()
initials = "".join([part[0].upper() for part in name_parts if part])
ascii_sum = sum(ord(char) for char in initials)

#1
sales=ny.array([ascii_sum+50*i for i in range(5)])
print(sales)

#2
tax_rate=((sales % 5)+5)/100
taxed_sales= sales * (1+tax_rate)
print(taxed_sales)

#3
discount_tester=ascii_sum+100
if ny.all(sales < discount_tester):
    discounted_array = sales - (sales * 0.05)  # 5% discount
else:
    discounted_array = sales - (sales * 0.1)  # 10% discount

print("Discounted Sales Array:", discounted_array)

#4

sales = ny.array([142, 192, 242, 292, 342])

sales_matrix = ny.tile(sales, (3, 1))  # Repeats the array 3 times along rows
print("Sales Matrix for Three Weeks:\n", sales_matrix)

week_multipliers = ny.array([1, 1.02, 1.04])


sales_matrix_expanded = sales_matrix * week_multipliers[:, ny.newaxis]
print("\nSales Matrix After 2% Increase per Week:\n", sales_matrix_expanded)
