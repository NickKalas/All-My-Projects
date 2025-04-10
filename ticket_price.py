def calculate_price(age, day):
    ChildrenPrice = 8
    TeenPrice = 12
    AdultsPrice = 15
    SeniorsPrice = 10

    if age < 0:
        return "Invalid age!!!"

    if age <= 12:
        final_ticket_price = ChildrenPrice
    elif age <= 17:
        final_ticket_price = TeenPrice
    elif age <= 64:
        final_ticket_price = AdultsPrice
    else:
        final_ticket_price = SeniorsPrice

    if day.lower() == "wednesday":
        final_ticket_price *= 0.8  # Discount

    return round(final_ticket_price, 2)  #ROund the price


print(f"The price is: {calculate_price(10, 'Wednesday')}")  # Output: 6.4
print(f"The price is: {calculate_price(25, 'Monday')}")  # Output: 15
print(f"The price is: {calculate_price(70, 'Wednesday')}")  # Output: 8.0
print(f"The price is: {calculate_price(-5, 'Friday')}")  # Output: Invalid age!!!
