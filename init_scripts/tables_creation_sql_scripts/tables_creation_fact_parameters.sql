CREATE TABLE fact_parameters (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	fact_parameters_value INTEGER NOT NULL,
	date_record DATE NOT NULL,
	parameter_id INTEGER,
	sector_id INTEGER,
	region_id INTEGER,
	FOREIGN KEY (parameter_id) REFERENCES parameters (id) ON DELETE CASCADE,
	FOREIGN KEY (sector_id) REFERENCES sectors (id) ON DELETE CASCADE,
	FOREIGN KEY (region_id) REFERENCES regions (id) ON DELETE CASCADE
);
