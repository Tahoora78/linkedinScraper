import sqlite3

conn = sqlite3.connect('linkedin.db')

c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS generalInfo (
                id integer PRIMARY KEY AUTOINCREMENT,
                name text NOT NULL,
                profession text,
                location text
            ); """)


c.execute(""" CREATE TABLE IF NOT EXISTS experience (
                id integer PRIMARY KEY AUTOINCREMENT,
                position text NOT NULL,
                company text,
                duration text
            ); """)


c.execute(""" CREATE TABLE IF NOT EXISTS education (
                id integer PRIMARY KEY AUTOINCREMENT,
                title text NOT NULL,
                institution text,
                duration text
            ); """)

c.execute(""" CREATE TABLE IF NOT EXISTS license (
                id integer PRIMARY KEY AUTOINCREMENT,
                title text NOT NULL,
                institution text
            ); """)

c.execute(""" CREATE TABLE IF NOT EXISTS educated (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                person_id INTEGER,
                education_id INTEGER,
                FOREIGN KEY(person_id) REFERENCES generalInfo(id),
                FOREIGN KEY(education_id) REFERENCES education(id)
            ); """)


c.execute(""" CREATE TABLE IF NOT EXISTS experienced (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                person_id INTEGER,
                experience_id ,
                FOREIGN KEY(person_id) REFERENCES generalInfo (id),
                FOREIGN KEY(experience_id) REFERENCES experience(id)
            ); """)

c.execute(""" CREATE TABLE IF NOT EXISTS licensed (
                id integer PRIMARY KEY AUTOINCREMENT,
                person_id INTEGER,
                license_id INTEGER,
                FOREIGN KEY(person_id) REFERENCES generalInfo(id),
                FOREIGN KEY(license_id) REFERENCES licence(id)
            ); """)


def insert_general_info(conn, c, info):
    with conn:
        c.execute(
            "INSERT INTO generalInfo (name, profession, location) VALUES (?, ?, ?)", (info[0], info[1], info[2]))
        return c.lastrowid


def insert_experience(conn, c, info):
    with conn:
        c.execute(
            "INSERT INTO experience (position, company, duration) VALUES (?, ?, ?)", (info[0], info[1], info[2]))
        return c.lastrowid


def insert_education(conn, c, info):
    with conn:
        c.execute(
            "INSERT INTO education (title, institution, duration) VALUES (?, ?, ?)", (info[0], info[1], info[2]))
        return c.lastrowid


def insert_license(conn, c, info):
    with conn:
        c.execute(
            "INSERT INTO license (title, institution) VALUES (?, ?)", (info[0], info[1]))
    return c.lastrowid


def insert_experienced(conn, c, person_id, experience_id):
    with conn:
        c.execute(
            "INSERT INTO experienced (person_id, experience_id) VALUES (?, ?)", (person_id, experience_id))


def insert_educated(conn, c, person_id, education_id):
    with conn:
        c.execute(
            "INSERT INTO educated (person_id, education_id) VALUES (?, ?)", (person_id, education_id))


def insert_licensed(conn, c, person_id, license_id):
    with conn:
        c.execute(
            "INSERT INTO licensed (person_id, license_id) VALUES (?, ?)", (person_id, license_id))
