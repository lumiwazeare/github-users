import http.client
import json
import sqlite3
import sys


user_size = 150


def get_github_users(size=150):
    connection = http.client.HTTPSConnection("api.github.com")
    headers = {
        "Content-type": "application/json",
        "User-Agent": "Python 3 Script",
    }
    connection.request(
        "GET", "/users?per_page={}".format(size), headers=headers
    )
    response = connection.getresponse()
    users = json.loads(response.read().decode())
    connection.close()
    return users


print("processing...." + str(len(sys.argv)))

if len(sys.argv) > 1 and (sys.argv[1] == "-t" or sys.argv[1] == "--total"):
    assert sys.argv[2].isdigit
    user_size = int(sys.argv[2])
# create database if it does not exist and seed data from github
database = sqlite3.connect("github.db")

db_cursor = database.cursor()
db_cursor.execute(
    """CREATE TABLE IF NOT EXISTS github_users
                  (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT NOT NULL,
                      avatar_url TEXT NOT NULL,
                      type TEXT NOT NULL,
                      URL TEXT NOT NULL
                      )"""
)

# get users record from github api and insert record into database
users = get_github_users(user_size)
for current_user in users:
    db_cursor.execute(
        """INSERT INTO github_users
                      (username,avatar_url,type,URL)
                      VALUES('{}','{}','{}','{}')""".format(
            current_user["login"],
            current_user["avatar_url"],
            current_user["type"],
            current_user["url"],
        )
    )
database.commit()
print("done.")
