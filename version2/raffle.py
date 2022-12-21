"""Randomly pick customer and print customer info"""

from customers import get_customers_from_file
from random import choice

def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")


def run_raffle():
    """Run the weekly raffle."""

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)

run_raffle()

# Hint: remember to import any functions you need from
# other files or libraries
