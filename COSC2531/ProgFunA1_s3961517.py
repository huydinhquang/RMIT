###########################################
# Name:         Quang Huy Dinh - s3961517
# Highest part: TBD
# Problems:     TBD
###########################################

# Define constants
CONS_DASH = '-'
CONS_SHARP = '*'
CONS_TAB = '\t'
CONS_BREAK_LINE = '\n'
CONS_COMMA_WITH_SPACE = ', '

# Define properties
CONS_CUSTOMER_NAME = 'customer_name'
CONS_REWARD_PROGRAM = 'reward_program'

# Define value
CONS_IS_REWARD_PROGRAM_YES = 'y'
CONS_REWARD_PROGRAM_PERCENT = 20
CONS_TICKET_QUANTITY_MIN = 0
CONS_TICKET_QUANTITY_MAX = 50

# Menu
# Prepare data for menu
sharp_mgs = CONS_SHARP * 50

def break_line_message(message):
    return ('{0}{1}').format(message, CONS_BREAK_LINE)

# Prepare content for menu
menu_mgs = ''
menu_mgs += ('Welcome to the RMIT movie ticketing system!{0}').format(CONS_BREAK_LINE * 2)
menu_mgs_list = [
    sharp_mgs,
    'You can choose from the following options:',
    '1: Purchase a ticket',
    '2: Add new movies',
    '3: Display existing customers information',
    '4: Display existing movies information',
    '0: Exit the program',
    sharp_mgs
]
for i in menu_mgs_list:
    menu_mgs += break_line_message(i)

# Function to convert the input value of reward program to Boolean
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

# Function to validate whether or not the entered value is in the predefined list
def validate_predefined_value(value_list, value):
    if not value:
        return False
    
    for m in value_list:
        if m == value:
            return True
    return False

# Function to enter a valid movie
def define_movie_name(movie_list):
    movie_list_str = CONS_COMMA_WITH_SPACE.join(movie_list)
    while True:
        try:
            #movie_name = input('Enter the name of the movie [enter a valid name only, e.g. {0}]:{1}'.format(movie_list_str, CONS_BREAK_LINE))
            movie_name = 'Avatar'
            if not validate_predefined_value(movie_list, movie_name):
                print('The movie is not valid. Please enter a valid movie.!')
            
            return movie_name
        except ValueError:
            continue

# Function to enter a valid ticket type
def define_ticket_type(ticket_type_list):
    ticket_type_list_str = CONS_COMMA_WITH_SPACE.join(ticket_type_list)
    while True:
        try:
            # ticket_type = input('Enter the ticket type [enter a valid type only, e.g. {0}]:{1}'.format(ticket_type_list_str, CONS_BREAK_LINE))
            ticket_type = 'adult'
            if not validate_predefined_value(ticket_type_list, ticket_type):
                print('The ticket type is not valid. Please enter a valid ticket type.')
            
            return ticket_type
        except ValueError:
            continue

# Function to enter a valid ticket quantity
def define_ticket_quantity():
    while True:
        try:
            # ticket_quantity = int(input('Enter the ticket quantity [enter a positive integer only, e.g. 1, 2, 3]:{0}'.format(CONS_BREAK_LINE)))
            ticket_quantity = 20

            if ticket_quantity <= CONS_TICKET_QUANTITY_MIN:
                print('The ticket quantity is not valid. Please enter a valid ticket quantity.')
                continue

            if ticket_quantity > CONS_TICKET_QUANTITY_MAX:
                print('Ticket quantity must be less than the number of available seats. Please enter a smaller ticket quantity.')
                continue

            return ticket_quantity
        except ValueError:
            print('The ticket quantity is not valid. Please enter a valid ticket quantity.')
            continue

# Function to enter a valid reward program
def define_reward_program(is_reward_program_list):
    while True:
        try:
            is_reward_program = input(
                'The customer is not in the rewards program. Does the customer want to join the rewards program [enter y or n]?{0}'.format(CONS_BREAK_LINE))
            if not validate_predefined_value(is_reward_program_list, is_reward_program):
                print('Please only enter y or n')
                continue
            
            return convert_answer_reward_program(is_reward_program)
        except ValueError:
            continue

# Function to purchase a ticket (Option 1)
def purchase_ticket():
    # # Ask for customer name
    #customer_name = input('Enter the name of the customer [e.g. Huy]:{0}'.format(CONS_BREAK_LINE))
    customer_name = 'James'

    # Ask for movie name
    movie_list = ['Avatar', 'Titanic', 'StarWar']
    movie_name = define_movie_name(movie_list)

    # Ask for ticket type
    ticket_type_list = ['adult', 'child', 'senior', 'concession']
    ticket_type = define_ticket_type(ticket_type_list)

    # Ask for ticket quantity
    ticket_quantity = define_ticket_quantity()

    customer_list = [
        {CONS_CUSTOMER_NAME: 'Mary', CONS_REWARD_PROGRAM: True},
        {CONS_CUSTOMER_NAME: 'James', CONS_REWARD_PROGRAM: False},
    ]

    # Ask for joining reward program
    is_reward_program_list = ['y', 'n']
    is_reward_program = check_reward_program(customer_list, customer_name)
    if not is_reward_program:
        is_reward_program = define_reward_program(is_reward_program_list)

    # Define list of unit price based on ticket type
    unit_price_list = {'adult': 25.0, 'child': 19.5, 'senior': 17.0, 'student': 20.5, 'concession': 20.5}

    # Calculate ticket and booking fees
    unit_price = unit_price_list[ticket_type]
    booking_fee = ticket_quantity * 2
    ticket_cost = ticket_quantity * unit_price

    # Calculate discount based on the reward program
    discount = 0
    if is_reward_program:
        discount = ticket_cost * CONS_REWARD_PROGRAM_PERCENT / 100

    # Calculate total price
    total_cost = ticket_cost - discount + booking_fee

    # Prepare data for receipt
    dash_mgs = CONS_DASH * 50 + CONS_BREAK_LINE
    tab_mgs_twice = CONS_TAB * 2
    tab_mgs_three = CONS_TAB * 3
    tab_mgs_four = CONS_TAB * 4

    # Prepare content for receipt
    receipt_mgs = ''
    receipt_mgs += dash_mgs
    receipt_mgs += ('Receipt of {0}{1}').format(customer_name, CONS_BREAK_LINE)
    receipt_mgs += dash_mgs
    receipt_mgs += ('Movie:{0}{1}{2}').format(tab_mgs_four, movie_name, CONS_BREAK_LINE)
    receipt_mgs += ('Ticket type:{0}{1}{2}').format(tab_mgs_three, ticket_type, CONS_BREAK_LINE)
    receipt_mgs += ('Ticket unit price:{0}{1}{2}').format(tab_mgs_twice, unit_price, CONS_BREAK_LINE)
    receipt_mgs += ('Ticket quantity:{0}{1}{2}').format(tab_mgs_twice, ticket_quantity, CONS_BREAK_LINE)
    receipt_mgs += dash_mgs
    receipt_mgs += ('Discount:{0}{1}{2}').format(tab_mgs_three, discount, CONS_BREAK_LINE)
    receipt_mgs += ('Booking fee:{0}{1}{2}').format(tab_mgs_three, booking_fee, CONS_BREAK_LINE)
    receipt_mgs += ('Total cost:{0}{1}{2}').format(tab_mgs_three, total_cost, CONS_BREAK_LINE)

    # Print out the receipt
    print(receipt_mgs)

# Function to add movies (Option 2)
def add_movie():
    # TBD
    return

# Function to display existing customers information (Option 3)
def display_customer_info():
    # TBD
    return

# Function to display existing movies information (Option 4)
def display_movie_info():
    # TBD
    return

# Function to print out the menu
def print_menu():
    print(menu_mgs)
    selected_option = input('Choose one option: ')
    match selected_option:
        case '1':
            purchase_ticket()
        case '2':
            add_movie()
        case '3':
            display_customer_info()
        case '4':
            display_movie_info()
        case '0':
            quit()
        case _:
            print('Something went wrong!')
            return
    
    # Print out the menu after each task
    print_menu()

# Innitially, call the function to print out the menu
print_menu()


    
