###########################################
# Name:         Quang Huy Dinh - s3961517
# Highest part: TBD
# Problems:     TBD
###########################################

# Ask for customer name
customer_name = input('Enter the name of the customer [e.g. Huy]:\n')

# Ask for movie name
movie_name = input('Enter the name of the movie [enter a valid name only, e.g. Avatar]:\n')

# Ask for ticket type and print it out
ticket_type = input('Enter the ticket type [enter a valid type only, e.g. adult, child, senior, concession]:\n')

# Ask for ticket quantity and print it out
ticket_quantity = input('Enter the ticket quantity [enter a positive integer only, e.g. 1, 2, 3]:\n')

unit_price_list = [('adult', 25.0), ('child', 19.5), ('senior', 17.0), ('student', 20.5), ('concession', 20.5)]
#print(unit_price_list)

unit_price = unit_price_list.get(ticket_type)
print(unit_price)