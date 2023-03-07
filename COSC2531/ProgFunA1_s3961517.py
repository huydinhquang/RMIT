###########################################
# Name:         Quang Huy Dinh - s3961517
# Highest part: TBD
# Problems:     TBD
###########################################

# Define constants
CONS_DASH = '-'
CONS_TAB = '\t'
CONS_BREAK_LINE = '\n'

# Ask for customer name
# customer_name = input('Enter the name of the customer [e.g. Huy]:\n')

# Ask for movie name
# movie_name = input('Enter the name of the movie [enter a valid name only, e.g. Avatar]:\n')

# Ask for ticket type
# ticket_type = input('Enter the ticket type [enter a valid type only, e.g. adult, child, senior, concession]:\n')

# Ask for ticket quantity
# ticket_quantity = input('Enter the ticket quantity [enter a positive integer only, e.g. 1, 2, 3]:\n')

# Ask for joining reward program
is_reward_program = input('The customer is not in the rewards program. Does the customer want to join the rewards program [enter y or n]?\n')

unit_price_list = {'adult': 25.0, 'child': 19.5, 'senior': 17.0, 'student': 20.5, 'concession': 20.5}

unit_price = unit_price_list['adult']
# print(unit_price_list['adult'])

booking_fee = 2 * 2

total_cost = unit_price * 2
print(total_cost)

if is_reward_program == 'n':
    total_cost %= 20
print(total_cost + booking_fee)

# Prepare data
dash_mgs = CONS_DASH*50 + CONS_BREAK_LINE
tab_mgs_twice = CONS_TAB*2
tab_mgs_three = CONS_TAB*3
tab_mgs_four = CONS_TAB*4

# Display receipt
receipt_message = ''
receipt_message += dash_mgs
receipt_message += ('Receipt of {0}{1}').format('Huy', CONS_BREAK_LINE)
receipt_message += dash_mgs
receipt_message += ('Movie:{0}{1}{2}').format(tab_mgs_four, 'Test', CONS_BREAK_LINE)
receipt_message += ('Ticket type:{0}{1}{2}').format(tab_mgs_three, 'test', CONS_BREAK_LINE)
receipt_message += ('Ticket unit price:{0}{1}{2}').format(tab_mgs_twice, unit_price, CONS_BREAK_LINE)
receipt_message += ('Ticket quantity:{0}{1}{2}').format(tab_mgs_twice, 2, CONS_BREAK_LINE)
receipt_message += dash_mgs
receipt_message += ('Discount:{0}{1}{2}').format(tab_mgs_three, 2, CONS_BREAK_LINE)
receipt_message += ('Booking fee:{0}{1}{2}').format(tab_mgs_three, 2, CONS_BREAK_LINE)
receipt_message += ('Total cost:{0}{1}{2}').format(tab_mgs_three, 2, CONS_BREAK_LINE)

# Print out the receipt
print(receipt_message)