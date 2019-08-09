CREATE TABLE raw.users (
	  user_id NUMERIC(25) PRIMARY KEY
	, user_name VARCHAR(500) UNIQUE NOT NULL
	, screen_name VARCHAR(500) UNIQUE NOT NULL
	, user_location VARCHAR(500)
	, description VARCHAR(500)
	, created_timestamp TIMESTAMP NOT NULL
	, followers_count BIGINT NOT NULL
);
