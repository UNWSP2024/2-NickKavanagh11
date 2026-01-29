def calculate_total_purchase(item1, item2, item3, item4, item5):
    item1 = float(input(" 13.76 "))
    item2 = float(input(" 5.00 "))
    item3 = float(input(" 6.79 "))
    item4 = float(input(" 11.99 "))
    item5 = float(input(" 2.99 "))

    subtotal = item1 + item2 + item3 + item4 + item5
    sales_tax = subtotal * 0.07
    total = subtotal + sales_tax

    print("Subtotal:", subtotal)
    print("Sales Tax:", sales_tax)
    print("Total:", total)



calculate_total_purchase(item1, item2, item3, item4, item5)
