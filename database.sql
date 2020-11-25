CREATE TABLE pets(
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR (50) NOT NULL,
	"breed" VARCHAR (50),
	"color" VARCHAR (15),
  	"checked_in" BOOLEAN DEFAULT 'FALSE',
    "notes" VARCHAR (80)
); 


SELECT * FROM "pets";
