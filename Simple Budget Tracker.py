import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Database setup
def create_db():
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        type TEXT,
        category TEXT,
        amount REAL,
        date TEXT
    )
    ''')
    conn.commit()
    conn.close()

def add_transaction(transaction_type, category, amount, date):
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO transactions (type, category, amount, date)
    VALUES (?, ?, ?, ?)
    ''', (transaction_type, category, amount, date))
    conn.commit()
    conn.close()

def view_transactions():
    conn = sqlite3.connect('budget_tracker.db')
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    return df

def plot_expenses():
    df = view_transactions()
    df_expenses = df[df['type'] == 'expense']
    df_expenses.groupby('category')['amount'].sum().plot(kind='bar')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.title('Expenses by Category')
    plt.show()

# Example usage
create_db()
add_transaction('income', 'salary', 3000, '2024-08-01')
add_transaction('expense', 'groceries', 150, '2024-08-05')
add_transaction('expense', 'entertainment', 100, '2024-08-10')
plot_expenses()
