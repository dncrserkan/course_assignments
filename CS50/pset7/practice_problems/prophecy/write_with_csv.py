import csv
import sqlite3
from sys import exit


def main():
    database = "new.db"
    filename = "students.csv"
    
    # READ DATA
    try:
        data = []
        with open (filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("File not found")
        exit(1)
    
    students = []       # {id, name}
    houses = []         # house names indexes are house_id
    headers = []        # header names indexes are house_id
    assignments  = []   # {student_id, house_id}
    for row in data:
        if row["house"] not in houses:
            houses.append(row["house"])
            headers.append(row["head"])
        students.append({"id": row["id"],
                         "name": row["student_name"]})
        assignments.append({"student_id": row["id"],
                            "house_id": houses.index(row["house"])})


    # WRITE DATA
    conn = sqlite3.connect(database)
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
