import sqlite3


def main():
    conn = sqlite3.connect('new.db')
    cur = conn
    
    cur.execute('''CREATE TABLE IF NOT EXISTS houses(
                id INTEGER PRIMARY KEY,
                house TEXT,
                header TEXT
            );''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY,
                name TEXT
            );''')

    cur.execute('''CREATE TABLE IF NOT EXISTS assignments(
                student_id INTEGER PRIMARY KEY,
                house_id INTEGER,
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(house_id) REFERENCES houses(id)
            );''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
