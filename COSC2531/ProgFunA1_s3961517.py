#################################################
# Name:         Quang Huy Dinh - s3961517       #
# Highest part: 3.3                             #
# Problems:     No                              #
#                - Tested OK on Python v3.10.9  #
#                - Please run on the same env   #
#################################################

# Define constants
CONS_DASH = '-'
CONS_SHARP = '*'
CONS_TAB = '\t'
CONS_BREAK_LINE = '\n'
CONS_COMMA = ','
CONS_COMMA_WITH_SPACE = ', '

# Define properties
CONS_CUSTOMER_NAME = 'customer_name'
CONS_CUSTOMER_REWARD_PROGRAM = 'reward_program'
CONS_MOVIE_NAME = 'movie_name'
CONS_MOVIE_SEAT = 'movie_seat'
CONS_MOVIE_TOTAL_COST = 'movie_total_cost'
CONS_MOVIE_HEADER_REVENUE = 'Revenue'
CONS_TICKET_TYPE = 'ticket_type'
CONS_TICKET_UNIT_PRICE = 'ticket_unit_price'
CONS_TICKET_QUANTITY = 'ticket_quantity'

# Define value
CONS_IS_REWARD_PROGRAM_YES = 'y'
CONS_REWARD_PROGRAM_PERCENT = 20
CONS_TICKET_QUANTITY_MIN = 0
CONS_TICKET_QUANTITY_MAX = 50
CONS_MOVIE_TOTAL_COST_INIT = 0
CONS_TICKET_TYPE_ADULT = 'adult'
CONS_TICKET_TYPE_CHILD = 'child'
CONS_TICKET_TYPE_SENIOR = 'senior'
CONS_TICKET_TYPE_STUDENT = 'student'
CONS_TICKET_TYPE_CONCESSION = 'concession'
CONS_EMPTY_STR = ''
CONS_RECEIPT_CELL_FORMAT = '{:<30}{:>20}'
CONS_MOVIE_RECORD_HEADER_FORMAT = '{:^10}'
CONS_MOVIE_RECORD_CELL_FORMAT = '{:^10}'
CONS_MOVIE_RECORD_FIRST_CELL_FORMAT = '{:<10}'

# Menu
# Prepare data for menu
sharp_mgs = CONS_SHARP * 50
dash_mgs = CONS_DASH * 50

# Initially, define movies and customers
init_movie_list = [
    {
        CONS_MOVIE_NAME: 'Avatar',
        CONS_MOVIE_SEAT: CONS_TICKET_QUANTITY_MAX,
        CONS_MOVIE_TOTAL_COST: CONS_MOVIE_TOTAL_COST_INIT,
        CONS_TICKET_TYPE_ADULT: CONS_TICKET_QUANTITY_MIN,
        CONS_TICKET_TYPE_CHILD: CONS_TICKET_QUANTITY_MIN,
        CONS_TICKET_TYPE_SENIOR: CONS_TICKET_QUANTITY_MIN,
        CONS_TICKET_TYPE_STUDENT: CONS_TICKET_QUANTITY_MIN,
        CONS_TICKET_TYPE_CONCESSION: CONS_TICKET_QUANTITY_MIN,
    },
    {
        CONS_MOVIE_NAME: 'Titanic', 
        CONS_MOVIE_SEAT: CONS_TICKET_QUANTITY_MAX,
        CONS_MOVIE_TOTAL_COST: CONS_MOVIE_TOTAL_COST_INIT,
        CONS_TICKET_TYPE_ADULT: CONS_TICKET_QUANTITY_MIN,
        CONS_TICKET_TYPE_CHILD: CONS_TICKET_QUANTITY_MIN,
        CONS_TICKET_TYPE_SENIOR: CONS_TICKET_QUANTITY_MIN,
        CONS_TICKET_TYPE_STUDENT: CONS_TICKET_QUANTITY_MIN,
        CONS_TICKET_TYPE_CONCESSION: CONS_TICKET_QUANTITY_MIN,
    },
    {
        CONS_MOVIE_NAME: 'StarWar', 
        CONS_MOVIE_SEAT: CONS_TICKET_QUANTITY_MAX,
        CONS_MOVIE_TOTAL_COST: CONS_MOVIE_TOTAL_COST_INIT,
        CONS_TICKET_TYPE_ADULT: CONS_TICKET_QUANTITY_MIN,
        CONS_TICKET_TYPE_CHILD: CONS_TICKET_QUANTITY_MIN,
        CONS_TICKET_TYPE_SENIOR: CONS_TICKET_QUANTITY_MIN,
        CONS_TICKET_TYPE_STUDENT: CONS_TICKET_QUANTITY_MIN,
        CONS_TICKET_TYPE_CONCESSION: CONS_TICKET_QUANTITY_MIN,
    },
]

init_customer_list = [
        {CONS_CUSTOMER_NAME: 'Mary', CONS_CUSTOMER_REWARD_PROGRAM: True},
        {CONS_CUSTOMER_NAME: 'James', CONS_CUSTOMER_REWARD_PROGRAM: False},
    ]

init_ticket_type_list = [
    CONS_TICKET_TYPE_ADULT,
    CONS_TICKET_TYPE_CHILD,
    CONS_TICKET_TYPE_SENIOR,
    CONS_TICKET_TYPE_STUDENT,
    CONS_TICKET_TYPE_CONCESSION
]

def break_line_message(message):
    return ('{0}{1}').format(message, CONS_BREAK_LINE)

def convert_string_to_list(string, separator):
    return list(string.split(f'{separator}'))
    
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
    '5: Display the most popular movie',
    '6: Display all movie record',
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
         
# Function to retrieve metadata by the property name
def retrieve_metadata(list, key, value):
    for i in list:
        if value == i[key]:
            return i
    return None
                   
# Function to validate whether or not the entered value is in the predefined list
def validate_predefined_value(value_list, key= None, value = None):
    if not value:
        return False
    
    if key:
        for m in value_list:
            if m[key] == value:
                return True
    else:
        for m in value_list:
            if m == value:
                return True
    return False

# Function to validate the available ticket quantity by the movie name
def validate_available_ticket_quantity(movie_name, ticket_quantity):
    movie = retrieve_metadata(init_movie_list, CONS_MOVIE_NAME, movie_name)
    if ticket_quantity > movie[CONS_MOVIE_SEAT]:
        return True
    return False

def validate_movie_ticket_quantity(ticket_quantity):
    try:
        ticket_quantity = int(ticket_quantity)
        if ticket_quantity <= CONS_TICKET_QUANTITY_MIN:
            print('The ticket quantity is not valid. Please enter a valid ticket quantity.')
            return False

        return True
    except ValueError:
        print('The ticket quantity is not valid. Please enter a valid ticket quantity.')
        return False

# Function to enter a valid movie
def define_movie_name(init_movie_list):
    movie_list_str = CONS_COMMA_WITH_SPACE.join([m[CONS_MOVIE_NAME] for m in init_movie_list])

    while True:
        try:
            movie_name = input(break_line_message('Enter the name of the movie [enter a valid name only, e.g. {0}]:').format(movie_list_str))
            # movie_name = 'Avatar'
            if not validate_predefined_value(init_movie_list, CONS_MOVIE_NAME, movie_name):
                print('The movie is not valid. Please enter a valid movie!')
                continue

            return movie_name
        except ValueError:
            continue

# Function to enter a valid ticket type
def define_ticket_type(ticket_type_list):
    ticket_type_list_str = CONS_COMMA_WITH_SPACE.join(ticket_type_list)
    while True:
        try:
            ticket_type_str = input(break_line_message('Enter the ticket type [enter a valid type only, e.g. {0}]:').format(ticket_type_list_str))
            # ticket_type = 'adult'
            ticket_type_list = convert_string_to_list(ticket_type_str, CONS_COMMA)
            
            is_valid = True
            result = []

            for i in ticket_type_list:
                i = i.strip() # Strip out all spaces before and after the item
                if not validate_predefined_value(value_list = init_ticket_type_list, value = i):
                    print(('The ticket type \'{0}\' is not valid. Please enter a valid ticket type.').format(i))
                    is_valid = False
                else:
                    result.append(i)

            if not is_valid:
                continue

            return result
        except ValueError:
            continue

# Function to enter a valid ticket quantity
def define_ticket_quantity(movie_name):
    while True:
        try:
            ticket_quantity_str = input(break_line_message('Enter the ticket quantity [enter a positive integer only, e.g. 1, 2, 3]'))
            # ticket_quantity = 20
            ticket_quantity_list = convert_string_to_list(ticket_quantity_str, CONS_COMMA)

            is_valid = True
            total_ticket = 0
            result = []

            for i in ticket_quantity_list:
                i = i.strip() # Strip out all spaces before and after the item
                if not validate_movie_ticket_quantity(i):
                    is_valid = False
                else:
                    ticket_quantity = int(i)
                    total_ticket += ticket_quantity
                    result.append(ticket_quantity)

            if validate_available_ticket_quantity(movie_name, total_ticket):
                print('Ticket quantity must be less than the number of available seats. Please enter a smaller ticket quantity.')
                is_valid = False
                        
            if not is_valid:
                continue

            return result, total_ticket
        except ValueError:
            continue

# Function to enter a valid reward program
def define_reward_program(is_reward_program_list):
    while True:
        try:
            is_reward_program = input(break_line_message(
                'The customer is not in the rewards program. Does the customer want to join the rewards program [enter y or n]?'))
            if not validate_predefined_value(value_list = is_reward_program_list, value = is_reward_program):
                print('Please only enter y or n')
                continue
            
            return convert_answer_reward_program(is_reward_program)
        except ValueError:
            continue

# Function to update the ticket quantity regarding the ticket type based on the movie
def update_movie_ticket_quantity(movie, ticket_type, ticket_quantity):
    match ticket_type:
        case 'adult':
            movie[CONS_TICKET_TYPE_ADULT] += ticket_quantity
        case 'child':
            movie[CONS_TICKET_TYPE_CHILD] += ticket_quantity
        case 'senior':
            movie[CONS_TICKET_TYPE_SENIOR] += ticket_quantity
        case 'student':
            movie[CONS_TICKET_TYPE_STUDENT] += ticket_quantity
        case 'concession':
            movie[CONS_TICKET_TYPE_CONCESSION] += ticket_quantity
        case _:
            print('Something went wrong!')
            return

# Function to purchase a ticket (Option 1)
def purchase_ticket():
    # Ask for customer name
    customer_name = input(break_line_message('Enter the name of the customer [e.g. Huy]'))
    # customer_name = 'James'

    # Ask for movie name
    movie_name = define_movie_name(init_movie_list)

    # Ask for ticket type
    ticket_type_list = define_ticket_type(init_ticket_type_list)

    # Ask for ticket quantity
    ticket_quantity_list, total_ticket = define_ticket_quantity(movie_name)

    # Ask for joining reward program
    is_reward_program_list = ['y', 'n']
    customer = retrieve_metadata(init_customer_list, CONS_CUSTOMER_NAME, customer_name)
    is_reward_program = False
    if customer:
        is_reward_program = customer[CONS_CUSTOMER_REWARD_PROGRAM]
    if not is_reward_program:
        is_reward_program = define_reward_program(is_reward_program_list)
        if is_reward_program:
            print(break_line_message('Successfully add the customer to the rewards program.'))

    # Define list of unit price based on ticket type
    unit_price_list = {
        CONS_TICKET_TYPE_ADULT: 25.0,
        CONS_TICKET_TYPE_CHILD: 19.5,
        CONS_TICKET_TYPE_SENIOR: 17.0,
        CONS_TICKET_TYPE_STUDENT: 20.5,
        CONS_TICKET_TYPE_CONCESSION: 20.5
    }

    # Retrieve movie metadata by movie name
    movie = retrieve_metadata(init_movie_list, CONS_MOVIE_NAME, movie_name)

    # Calculate ticket fees and booking fees
    ticket_cost = 0
    ticket_list = []
    for idx, i in enumerate(ticket_type_list):
        unit_price = unit_price_list[i]
        ticket_quantity = ticket_quantity_list[idx]
        ticket_cost += (ticket_quantity * unit_price)
        ticket_list.append({
            CONS_TICKET_TYPE: i,
            CONS_TICKET_UNIT_PRICE: unit_price,
            CONS_TICKET_QUANTITY: ticket_quantity_list[idx]
        })
        update_movie_ticket_quantity(movie, i, ticket_quantity)

    booking_fee = total_ticket * 2
    
    # Calculate discount based on the reward program
    discount = 0
    if is_reward_program:
        discount = ticket_cost * CONS_REWARD_PROGRAM_PERCENT / 100

    # Calculate total price
    total_cost = ticket_cost - discount + booking_fee

    # Recalculate ticket quantity, then update total cost of the movie
    movie[CONS_MOVIE_SEAT] -= total_ticket
    movie[CONS_MOVIE_TOTAL_COST] += total_cost
    
    # Add or update current customer to customer list with the reward program information
    customer = retrieve_metadata(init_customer_list, CONS_CUSTOMER_NAME, customer_name)
    if customer:
        customer[CONS_CUSTOMER_REWARD_PROGRAM] = is_reward_program
    else:
        init_customer_list.append({
            CONS_CUSTOMER_NAME: customer_name, CONS_CUSTOMER_REWARD_PROGRAM: is_reward_program
        })

    # Prepare content for receipt
    receipt_mgs = ''
    receipt_mgs_list = [
        dash_mgs,
        ('Receipt of {0}').format(customer_name),
        dash_mgs,
        CONS_RECEIPT_CELL_FORMAT.format('Movie:', movie_name)
    ]
    
    # Generate each ticket (with type, unit price and quantity) in the ticket list by iterating
    for i in ticket_list:
        receipt_mgs_list.extend([
            CONS_RECEIPT_CELL_FORMAT.format('Ticket type:', i[CONS_TICKET_TYPE]),
            CONS_RECEIPT_CELL_FORMAT.format('Ticket unit price:', i[CONS_TICKET_UNIT_PRICE]),
            CONS_RECEIPT_CELL_FORMAT.format('Ticket quantity:', i[CONS_TICKET_QUANTITY])
        ])
    
    # Extend receipt with the discount, booking fee and total cost
    receipt_mgs_list.extend([
        dash_mgs,
        CONS_RECEIPT_CELL_FORMAT.format('Discount:', discount),
        CONS_RECEIPT_CELL_FORMAT.format('Booking fee:', booking_fee),
        CONS_RECEIPT_CELL_FORMAT.format('Total cost:', total_cost)
    ])
    
    for i in receipt_mgs_list:
        receipt_mgs += break_line_message(i)

    # Print out the receipt
    print(receipt_mgs)

# Function to add movies (Option 2)
def add_movie():
    movie_list_str = input(break_line_message('Enter a list of movies [enter a valid name only, e.g. Titanic, Avenger, Frozen]:'))
    movie_list = convert_string_to_list(movie_list_str, CONS_COMMA)
    for i in movie_list:
        i = i.strip() # Strip out all spaces before and after the item
        # If the entered movie is not the predefined values, add it into the movie list
        if validate_predefined_value(init_movie_list, CONS_MOVIE_NAME, i):
            print(break_line_message('{0} is an existing movie!').format(i))
        else:
            init_movie_list.append({
                CONS_MOVIE_NAME: i,
                CONS_MOVIE_SEAT: CONS_TICKET_QUANTITY_MAX,
                CONS_MOVIE_TOTAL_COST: CONS_MOVIE_TOTAL_COST_INIT,
                CONS_TICKET_TYPE_ADULT: CONS_TICKET_QUANTITY_MIN,
                CONS_TICKET_TYPE_CHILD: CONS_TICKET_QUANTITY_MIN,
                CONS_TICKET_TYPE_SENIOR: CONS_TICKET_QUANTITY_MIN,
                CONS_TICKET_TYPE_STUDENT: CONS_TICKET_QUANTITY_MIN,
                CONS_TICKET_TYPE_CONCESSION: CONS_TICKET_QUANTITY_MIN,
            })

# Function to display existing customers information (Option 3)
def display_customer_info():
    for i in init_customer_list:
        print(('Customer name: {0} | reward program: {1}').format(i[CONS_CUSTOMER_NAME], i[CONS_CUSTOMER_REWARD_PROGRAM]))

# Function to display existing movies information (Option 4)
def display_movie_info():
    for i in init_movie_list:
        print(('Movie name: {0} | available seat: {1}').format(i[CONS_MOVIE_NAME], i[CONS_MOVIE_SEAT]))

# Function to display the most popular movie (Option 5)
def display_most_popular_movie():
    movie_total_cost_max = max(init_movie_list, key=lambda x:x[CONS_MOVIE_TOTAL_COST])
    print(('Movie name: {0} | total cost purchased: {1}').format(movie_total_cost_max[CONS_MOVIE_NAME], movie_total_cost_max[CONS_MOVIE_TOTAL_COST]))
    
# Function to display all movie record (Option 6)
def display_movie_record():
    # Generate header with ticket type & 'Revenue'
    movie_record_mgs = f'{CONS_MOVIE_RECORD_HEADER_FORMAT.format(CONS_EMPTY_STR)}'
    for i in init_ticket_type_list:
        movie_record_mgs += f'{CONS_MOVIE_RECORD_HEADER_FORMAT.format(i)}'
    movie_record_mgs += break_line_message(f'{CONS_MOVIE_RECORD_HEADER_FORMAT.format(CONS_MOVIE_HEADER_REVENUE)}')
    
    # Generate movie name with ticket quantity corresponding to ticket type and revenue in the header
    for movie in init_movie_list:
        movie_record_mgs += f'{CONS_MOVIE_RECORD_FIRST_CELL_FORMAT.format(movie[CONS_MOVIE_NAME])}'
        for ticket_type in init_ticket_type_list:
            movie_record_mgs += f'{CONS_MOVIE_RECORD_CELL_FORMAT.format(movie[ticket_type])}'
        movie_record_mgs += break_line_message(f'{CONS_MOVIE_RECORD_CELL_FORMAT.format(movie[CONS_MOVIE_TOTAL_COST])}')

    # Print out all movie records
    print(movie_record_mgs)

# Function to print out the menu
def print_menu():
    print(menu_mgs)
    selected_option = input('Choose one option: ')
    print(CONS_BREAK_LINE)
    match selected_option:
        case '1':
            purchase_ticket()
        case '2':
            add_movie()
        case '3':
            display_customer_info()
        case '4':
            display_movie_info()
        case '5':
            display_most_popular_movie()
        case '6':
            display_movie_record()
        case '0':
            quit()
        case _:
            print('Something went wrong!')
            return
    # Print separator as the end of the current task
    print(dash_mgs)

    # Print out the menu after each task
    print_menu()

# Innitially, call the function to print out the menu
print_menu()
