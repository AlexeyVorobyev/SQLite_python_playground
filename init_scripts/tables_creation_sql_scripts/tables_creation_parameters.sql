create table parameters (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	parameter_name TEXT NOT NULL,
	measure_id INTEGER,
	FOREIGN KEY (measure_id) REFERENCES measures (id) ON DELETE CASCADE
);