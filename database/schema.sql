CREATE TABLE "riders" (
	"id" INTEGER,
	"name" TEXT,
	PRIMARY KEY ("id")
);

CREATE TABLE "stations" (
	"id" INTEGER,
	"name" TEXT,
	"line" TEXT,
	PRIMARY KEY("id")
);

CREATE TABLE "visits" (
	"rider_id" INTEGER,
	"station_id" INTEGER,
	FOREIGN KEY("rider_id") REFERENCES "riders"("id"),
	FOREING KEY("station_id") REFERENCES "stations"("id")
	
);
