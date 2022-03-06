DROP TABLE IF EXISTS grades;

CREATE TABLE grades (
  name TEXT NOT NULL,
  id INTEGER PRIMARY KEY,
  points INTEGER NOT NULL
);

INSERT INTO grades 
    (name, id, points) 
VALUES 
    ("Steve Smith", 211, 80),
    ("Jian Wong", 122, 92),
    ("Chris Peterson", 213, 91),
    ("Sai Patel", 524, 94),
    ("Andrew Whitehead", 425, 99),
    ("Lynn Roberts", 626, 90),
    ("Robert Sanders", 287, 75);
