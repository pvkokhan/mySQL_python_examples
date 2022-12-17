import connect
from mysql.connector import Error
from createtable import execute_query


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

select_post_description = "SELECT description FROM posts WHERE id = 2"

post_description = execute_read_query(connect.connection, select_post_description)
for description in post_description:
    print(description)

update_post_description = """
UPDATE
  posts
SET
  description = "The weather has become pleasant now"
WHERE
  id = 2
"""

post_description_update = execute_query(connect.connection, update_post_description)