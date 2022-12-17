import mysql.connector
import connect
from mysql.connector import Error

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

"""
select_users = "SELECT * from users"
users = execute_read_query(connect.connection, select_users)

for user in users:
    print(user)
"""    

"""    
select_posts = "SELECT * FROM posts"
posts = execute_read_query(connect.connection, select_posts)

for post in posts:
    print(post)
"""

'''
select_users_posts = """
SELECT
  users.id,
  users.name,
  posts.description
FROM
  posts
  INNER JOIN users ON users.id = posts.user_id

users_posts = execute_read_query(connect.connection, select_users_posts)

for users_post in users_posts:
    print(users_post)
'''

'''
select_posts_comments_users = """
SELECT
  posts.description as post,
  text as comment,
  name
FROM
  posts
  INNER JOIN comments ON posts.id = comments.post_id
  INNER JOIN users ON users.id = comments.user_id
"""

posts_comments_users = execute_read_query(
    connect.connection, select_posts_comments_users
)

for posts_comments_user in posts_comments_users:
    print(posts_comments_user)
'''

'''
select_post_likes = """
SELECT
  description as Post,
  COUNT(likes.id) as Likes
FROM
  likes,
  posts
WHERE
  posts.id = likes.post_id
GROUP BY
  likes.post_id
"""

post_likes = execute_read_query(connect.connection, select_post_likes)

for post_like in post_likes:
    print(post_like)
'''