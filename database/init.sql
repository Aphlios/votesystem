CREATE TABLE votes (
    option_name VARCHAR(10) PRIMARY KEY,
    vote_number INT NOT NULL,
    last_vote TIMESTAMP
);

INSERT INTO votes (option_name, vote_number, last_vote) VALUES ('Cats', 0, '2024-10-10 00:00:00');
INSERT INTO votes (option_name, vote_number, last_vote) VALUES ('Dogs', 0, '2024-10-10 00:00:00');