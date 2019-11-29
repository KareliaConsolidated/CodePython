CREATE TABLE dogs (
	name TEXT,
	age INTEGER,
	breed TEXT
); 

INSERT INTO dogs (name, breed, age) VALUES ("Charlie", 35, "Tabby");
INSERT INTO dogs (name, breed, age) VALUES ("Jonas", 35, "Swedish");
INSERT INTO dogs (name, breed, age) VALUES ("Goldie", 35, "English Gherkin");
INSERT INTO dogs (name, breed, age) VALUES ("Juan", 35, "Chinese");

SELECT * FROM dogs;

# COMMANDS
# sqlite3 .open dogs_db.db
# .read 139_Sqlite_Python.sql