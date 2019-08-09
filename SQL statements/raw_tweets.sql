CREATE TABLE raw.tweets (
   	  tweet_id NUMERIC(25) PRIMARY KEY
	, created_timestamp TIMESTAMP NOT NULL
	, tweet_text VARCHAR(500)
	, hashtags VARCHAR(500) []
	, retweet_count BIGINT NOT NULL
	, favorite_count BIGINT NOT NULL
	, is_retweeted SMALLINT NOT NULL
	, has_hashtags SMALLINT NOT NULL
	, tweet_user_id NUMERIC(25) NOT NULL REFERENCES raw.users(user_id)
	, retweet_user_id NUMERIC(25) REFERENCES raw.users(user_id)
);
