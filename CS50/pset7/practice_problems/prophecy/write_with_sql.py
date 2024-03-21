import sqlite3
from sys import exit


def main():
    database_read = "roster.db"
    database_write = "new.db"
    
    # READ DATA
    conn = sqlite3.connect(database_read)
    cur = conn.cursor()

    # cur.execute('PRAGMA table_info(students)')
    # columns = [row[1] for row in cur.fetchall()]
    # print(columns)

    students = []       # {id, name}
    houses = []         # house names indexes are house_id
    headers = []        # header names indexes are house_id
    assignments  = []   # {student_id, house_id}
    cur.execute('SELECT * FROM students')
    for student in cur:
        if student[2] not in houses:
            houses.append(student[2])                                  # 2 -> house
            headers.append(student[3])                                 # 3 -> head
        students.append({'id': student[0],                             # 0 -> id
                         'name': student[1]})                          # 1 -> student_name
        assignments.append({'student_id': student[0], 
                            'house_id': houses.index(student[2])})
    
    conn.close()


    # WRITE DATA
    conn = sqlite3.connect(database_write)
    cur = conn

    for i in range(len(houses)):
        cur.execute("INSERT INTO houses VALUES (?, ?, ?)", (i, str(houses[i]), str(headers[i])))
    
    for i in range(len(students)):
        s_id = int(students[i]["id"])
        name = str(students[i]["name"]) 
        cur.execute("INSERT INTO students VALUES (?, ?)", (s_id, name))
    
    for i in range(len(assignments)):
        student_id = int(assignments[i]["student_id"])
        house_id = int(assignments[i]["house_id"])
        cur.execute("INSERT INTO assignments VALUES (?, ?)", (student_id, house_id))
    
    conn.commit()
    conn.close()
    exit(0)


if __name__ == "__main__":
    main()
