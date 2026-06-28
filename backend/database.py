import pyodbc

def get_db():
    CONN_STR = (
        "Driver={ODBC Driver 18 for SQL Server};"
        "Server=127.0.0.1,1433;"
        "Database=AuraBank;"
        "Uid=sa;"
        "Pwd=AuraBank@Hackathon1;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
        "Connection Timeout=30;"
    )
    conn= pyodbc.connect(CONN_STR)
    try:
        yield conn
    finally:
        conn.close()