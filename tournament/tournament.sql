-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create database, connect and create tables
CREATE DATABASE tournament;

\c tournament;

CREATE TABLE players (
  player_id SERIAL PRIMARY KEY,
  name TEXT
);

CREATE TABLE matches (
  match_id SERIAL PRIMARY KEY,
  winner_id SERIAL REFERENCES players(player_id),
  loser_id SERIAL REFERENCES players(player_id)
);

-- Create two useful views:
-- one for the number of wins of each player

CREATE VIEW noofwins AS
  SELECT player_id,
         name,
         COUNT(winner_id) AS wins
    FROM players LEFT JOIN matches
    ON winner_id = player_id
    GROUP BY player_id;

-- and one for the number of losses per player
CREATE VIEW nooflosses AS
  SELECT player_id,
         COUNT(loser_id) AS losses
    FROM players LEFT JOIN matches
    ON loser_id = player_id
    GROUP BY player_id;
