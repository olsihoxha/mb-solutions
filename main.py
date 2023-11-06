from st_ui import st_body
from db import create_cursor, close_connection

cursor, conn = create_cursor()

st_body(cursor)

close_connection(conn, cursor)


