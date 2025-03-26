import sys
import os

# Clearly set correct path for import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection import execute_query

def get_user_data(email: str):
    user = execute_query("""
        SELECT id, email, first_name, last_name, created_at
        FROM users
        WHERE email = %s;
    """, (email,))

    if not user:
        print("❌ No user found with that email.")
        return

    user_id, email, first_name, last_name, created_at = user[0]
    print("✅ User Information:")
    print(f"ID: {user_id}")
    print(f"Email: {email}")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Created At: {created_at}")

    tickets = execute_query("""
        SELECT num_ticket, article_count, purchase_date, mode_paiement
        FROM tickets
        WHERE user_id = %s;
    """, (user_id,))

    if not tickets:
        print("\n⚠️ This user has no tickets associated yet.")
        return

    print("\n✅ User's Tickets:")
    for ticket in tickets:
        num_ticket, article_count, purchase_date, mode_paiement = ticket
        print(f"\nTicket Number: {num_ticket}")
        print(f"Articles Count: {article_count}")
        print(f"Purchase Date: {purchase_date}")
        print(f"Payment Method: {mode_paiement}")

if __name__ == "__main__":
    user_email = "abdessamadtouzani@gmail.com"
    get_user_data(user_email)
