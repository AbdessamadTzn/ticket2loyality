import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime

from schema.users import create_users_table
from schema.tickets import create_tickets_table
from schema.marques import create_marques_table
from schema.articles import create_articles_table
import logging

# Load environment variables
load_dotenv()

def setup_database():
    logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
    """Create tables and insert test data"""
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    
    
    cursor = conn.cursor()
    
    try:
        # Create tables in correct order
        create_users_table(cursor)
        create_tickets_table(cursor)
        create_marques_table(cursor)
        create_articles_table(cursor)
        
        # Insert test data
        # 1. Insert users
        cursor.execute("""
        INSERT INTO users (email, password, first_name, last_name)
        VALUES 
            ('abdessamad@example.com', 'hashedpassword1', 'Abdessamad', 'Touzani'),
            ('jane@example.com', 'hashedpassword2', 'Jane', 'Smith')
        RETURNING id;
        """)
        user_ids = cursor.fetchall()
        
        # 2. Insert tickets
        cursor.execute("""
        INSERT INTO tickets (num_ticket, user_id, nbr_articl, purchase_date)
        VALUES 
            ('TICK001', %s, 'ART123', %s),
            ('TICK002', %s, 'ART456', %s)
        """, (user_ids[0][0], datetime.now(), user_ids[1][0], datetime.now()))
        
        # 3. Insert marques
        cursor.execute("""
        INSERT INTO marques (nom_marque, secteur, pays)
        VALUES 
            ('Nike', 'Sportswear', 'USA'),
            ('Adidas', 'Sportswear', 'Germany'),
            ('Apple', 'Electronics', 'USA')
        """)
        
        # 4. Insert articles
        cursor.execute("""
        INSERT INTO articles (num_ticket, nom_article, prix, quantite, nom_marque)
        VALUES 
            ('TICK001', 'Running Shoes', 129.99, 1, 'Nike'),
            ('TICK001', 'T-shirt', 29.99, 2, 'Adidas'),
            ('TICK002', 'iPhone', 999.99, 1, 'Apple')
        """)
        
        # Commit changes
        conn.commit()
        logging.info("Database initialized successfully with test data.")
        
    except Exception as e:
        conn.rollback()
        print(f"Error initializing database: {e}")
    finally:
        cursor.close()
        conn.close()

def test_data_retrieval():
    """Test retrieving data from the database"""
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    
    cursor = conn.cursor()
    
    try:
        # Get all tickets with user information
        cursor.execute("""
        SELECT t.num_ticket, u.first_name, u.last_name, t.purchase_date
        FROM tickets t
        JOIN users u ON t.user_id = u.id
        """)
        tickets = cursor.fetchall()
        print("\n--- Tickets with User Information ---")
        for ticket in tickets:
            print(f"Ticket: {ticket[0]}, User: {ticket[1]} {ticket[2]}, Date: {ticket[3]}")
        
        # Get all articles with their tickets and brands
        cursor.execute("""
        SELECT a.nom_article, a.prix, a.quantite, m.nom_marque, t.num_ticket
        FROM articles a
        JOIN marques m ON a.nom_marque = m.nom_marque
        JOIN tickets t ON a.num_ticket = t.num_ticket
        """)
        articles = cursor.fetchall()
        print("\n--- Articles with Ticket and Brand Information ---")
        for article in articles:
            print(f"Article: {article[0]}, Price: {article[1]}, Quantity: {article[2]}, Brand: {article[3]}, Ticket: {article[4]}")
        
    except Exception as e:
        print(f"Error retrieving data: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    setup_database()
    test_data_retrieval()