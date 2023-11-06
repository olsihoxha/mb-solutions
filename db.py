import psycopg2

connection_string = 'postgresql://readonly:usHtYkm4khtYEoXP@org-besabes-inst-olsi.data-1.use1.tembo.io:5432/postgres'


def create_cursor():
    try:
        connection = psycopg2.connect(connection_string)
        cursor = connection.cursor()
        return cursor, connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None


def get_query_results(cursor, query):
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Error getting the query results:", error)


def close_connection(connection, cursor):
    if cursor:
        cursor.close()
    if connection:
        connection.close()
