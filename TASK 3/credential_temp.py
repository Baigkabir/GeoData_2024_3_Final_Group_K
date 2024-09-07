# Replace your database credentials with each below parameters
PGHOST = "localhost"
PGDATABASE = "env_db"
PGUSER = "env_master"
PGPASSWORD = "M123xyz"
PORT = "5432"

# Construct the connection URL
URL = "postgresql://" + PGUSER + ":" + PGPASSWORD + "@" + PGHOST + ":" + PORT + "/" + PGDATABASE

