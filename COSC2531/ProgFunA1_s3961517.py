###########################################
# Name:         Quang Huy Dinh - s3961517
# Highest part: TBD
# Problems:     TBD
###########################################

# Define constants
CONS_DASH = '-'
CONS_TAB = '\t'
CONS_BREAK_LINE = '\n'
CONS_COMMA_WITH_SPACE = ', '

# Define properties
CONS_CUSTOMER_NAME = 'customer_name'
CONS_REWARD_PROGRAM = 'reward_program'

# Define value
CONS_IS_REWARD_PROGRAM_YES = 'y'

# Function to convert the input value of reward program
def convert_answer_reward_program(is_reward_program):
    result = False
    if is_reward_program == CONS_IS_REWARD_PROGRAM_YES:
        result = True
    return result
         
# Function to check whether or not the customer is in reward program
def check_reward_program(customer_list, customer_name):
    for customer in customer_list:
        for index, y in enumerate(customer):
                if customer_name == customer[CONS_CUSTOMER_NAME]:
                    return customer[CONS_REWARD_PROGRAM]


# # Ask for customer name
#customer_name = input('Enter the name of the customer [e.g. Huy]:{0}'.format(CONS_BREAK_LINE))
customer_name = 'Mary'

# # Ask for movie name
# movie_list = ['Avatar', 'Titanic', 'StarWar']
# movie_list_str = CONS_COMMA_WITH_SPACE.join(movie_list)
# movie_name = input('Enter the name of the movie [enter a valid name only, e.g. {0}]:{1}'.format(movie_list_str, CONS_BREAK_LINE))
movie_name = 'Avatar'

# # Ask for ticket type
# ticket_type = input('Enter the ticket type [enter a valid type only, e.g. adult, child, senior, concession]:{0}'.format(CONS_BREAK_LINE))
ticket_type = 'adult'

# # Ask for ticket quantity
# ticket_quantity = int(input('Enter the ticket quantity [enter a positive integer only, e.g. 1, 2, 3]:{0}'.format(CONS_BREAK_LINE)))
ticket_quantity = 2

customer_list = [
    {CONS_CUSTOMER_NAME: 'Mary', CONS_REWARD_PROGRAM: True},
    {CONS_CUSTOMER_NAME: 'James', CONS_REWARD_PROGRAM: False},
]

is_reward_program = check_reward_program(customer_list, customer_name)
if not is_reward_program:
    # Ask for joining reward program
    is_reward_program = convert_answer_reward_program(input(
        'The customer is not in the rewards program. Does the customer want to join the rewards program [enter y or n]?{0}'.format(CONS_BREAK_LINE)))

# Define lsit of unit price based on ticket type
unit_price_list = {'adult': 25.0, 'child': 19.5, 'senior': 17.0, 'student': 20.5, 'concession': 20.5}

# Calculate ticket and booking fees
unit_price = unit_price_list[ticket_type]
booking_fee = ticket_quantity * 2
ticket_cost = ticket_quantity * unit_price

# Calculate discount based on the reward program
discount = 0
if is_reward_program:
    discount = ticket_cost % 20

# Calculate total price
total_cost = ticket_cost - discount + booking_fee

# Prepare data
dash_mgs = CONS_DASH*50 + CONS_BREAK_LINE
tab_mgs_twice = CONS_TAB*2
tab_mgs_three = CONS_TAB*3
tab_mgs_four = CONS_TAB*4

# Display receipt
receipt_message = ''
receipt_message += dash_mgs
receipt_message += ('Receipt of {0}{1}').format(customer_name, CONS_BREAK_LINE)
receipt_message += dash_mgs
receipt_message += ('Movie:{0}{1}{2}').format(tab_mgs_four, movie_name, CONS_BREAK_LINE)
receipt_message += ('Ticket type:{0}{1}{2}').format(tab_mgs_three, ticket_type, CONS_BREAK_LINE)
receipt_message += ('Ticket unit price:{0}{1}{2}').format(tab_mgs_twice, unit_price, CONS_BREAK_LINE)
receipt_message += ('Ticket quantity:{0}{1}{2}').format(tab_mgs_twice, ticket_quantity, CONS_BREAK_LINE)
receipt_message += dash_mgs
receipt_message += ('Discount:{0}{1}{2}').format(tab_mgs_three, discount, CONS_BREAK_LINE)
receipt_message += ('Booking fee:{0}{1}{2}').format(tab_mgs_three, booking_fee, CONS_BREAK_LINE)
receipt_message += ('Total cost:{0}{1}{2}').format(tab_mgs_three, total_cost, CONS_BREAK_LINE)

# Print out the receipt
print(receipt_message)
