CREATE TABLE pets(
	"id" SERIAL PRIMARY KEY,
	"pet" VARCHAR (50) NOT NULL,
	"breed" VARCHAR (50),
	"color" VARCHAR (15),
  	"checked_in" VARCHAR (15) DEFAULT 'unchecked',
    "notes" VARCHAR (80)
); 


SELECT * FROM "pets";