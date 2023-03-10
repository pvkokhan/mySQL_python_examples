import mysql.connector
from mysql.connector import Error
import connect

connection = connect.create_connection("localhost", "root", "Fedotdanet0t", "sm_app")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed sucsessfully")
    except Error as e:
        print(f"The error '{e}'occurred")

create_user_table = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    name TEXT NOT NULL,
    age INT,
    gender TEXT,
    nationality TEXT,
    PRIMARY KEY (id)
)   ENGINE = InnoDB
"""

#createtable.execute_query(connect.create_connection("localhost", "root", "Fedotdanet0t", "sm_app"), createtable.create_user_table)

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
  id INT AUTO_INCREMENT, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  FOREIGN KEY fk_user_id (user_id) REFERENCES users(id), 
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INT AUTO_INCREMENT, 
  text TEXT NOT NULL, 
  user_id INTEGER NOT NULL,
  post_id INTEGER NOT NULL,
  FOREIGN KEY fk_post_id (post_id) REFERENCES posts(id),
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""


create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INT AUTO_INCREMENT,
  user_id INTEGER NOT NULL,
  post_id INTEGER NOT NULL,
  FOREIGN KEY fk_user_id (user_id) REFERENCES users(id), 
  FOREIGN KEY fk_post_id (post_id) REFERENCES posts(id), 
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""


#createtable.execute_query(createtable.connection, createtable.create_posts_table)

create_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""
#createtable.execute_query(createtable.connection, createtable.create_users)

create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1),
  ("Hot Weather", "The weather is very hot today", 2),
  ("Help", "I need some help with my work", 2),
  ("Great News", "I am getting married", 1),
  ("Interesting Game", "It was a fantastic game of tennis", 5),
  ("Party", "Anyone up for a late-night party today?", 3);
"""

create_comments = """
INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in', 1, 6),
  ('What sort of help?', 5, 3),
  ('Congrats buddy', 2, 4),
  ('I was rooting for Nadal though', 4, 5),
  ('Help with your thesis?', 2, 3),
  ('Many congratulations', 5, 4);
"""

create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1, 6),
  (2, 3),
  (1, 5),
  (5, 4),
  (2, 4),
  (4, 2),
  (3, 6);
"""