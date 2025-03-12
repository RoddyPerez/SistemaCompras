import urllib.parse

params = urllib.parse.quote_plus(
    "DRIVER=ODBC Driver 18 for SQL Server;"
    "SERVER=YSABELCUEVAS\\RODDY;"
    "DATABASE=SistemaCompras;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

