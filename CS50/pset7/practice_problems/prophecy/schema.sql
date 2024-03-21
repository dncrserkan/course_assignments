CREATE TABLE houses(
                id INTEGER PRIMARY KEY,
                house TEXT,
                header TEXT
            );
CREATE TABLE students(
                id INTEGER PRIMARY KEY,
                name TEXT
            );
CREATE TABLE assignments(
                student_id INTEGER PRIMARY KEY,
                house_id INTEGER,
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(house_id) REFERENCES houses(id)
            );