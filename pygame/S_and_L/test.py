import sqlite3

con = sqlite3.connect("S_and_L.db")
db = con.cursor()

name = "Jamin"
step = 2




#db.execute(f"INSERT INTO ScoreBoard (name, score) VALUES ('{name}', {step});")
db.execute("INSERT INTO ScoreBoard (name, score) VALUES (?,?);", (name, step))
print("DONE")
print(db.execute("SELECT * FROM ScoreBoard").fetchall())
con.commit()