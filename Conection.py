import pyodbc

conn_str = (
    "DRIVER=ODBC Driver 18 for SQL Server;"
    "SERVER=YSABELCUEVAS\\RODDY;"
    "DATABASE=SistemaCompras;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

try:
    conn = pyodbc.connect(conn_str)
    print("✅ Conexión exitosa a SQL Server")
    conn.close()
except Exception as e:
    print(f"❌ Error: {e}")
