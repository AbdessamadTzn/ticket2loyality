import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection import execute_query

def fetch_data():
    # Get tickets data
    tickets = execute_query("SELECT * FROM tickets;")
    print("Tickets Table:")
    for ticket in tickets:
        print(ticket)

    # Get articles data
    articles = execute_query("SELECT * FROM articles;")
    print("\n Articles Table:")
    for article in articles:
        print(article)

    # Get marques data
    marques = execute_query("SELECT * FROM marques;")
    print("\n Marques Table:")
    for marque in marques:
        print(marque)

if __name__ == "__main__":
    fetch_data()
