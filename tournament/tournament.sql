-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Drop database, if it exists
DROP DATABASE IF EXISTS tournament;

-- Create database, connect and create tables
CREATE DATABASE tournament;

\c tournament;

CREATE TABLE players (
  player_id SERIAL PRIMARY KEY ,
  name TEXT
);

CREATE TABLE matches (
  match_id SERIAL PRIMARY KEY,
  winner_id INTEGER REFERENCES players(player_id),
  loser_id INTEGER REFERENCES players(player_id)
);

-- Create useful views:

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

-- and one to execute standings retrieval query
CREATE VIEW standings AS
  SELECT noofwins.player_id,
         name,
         wins,
         (wins + losses) AS matches
    FROM noofwins, nooflosses
    WHERE noofwins.player_id = nooflosses.player_id
    ORDER BY wins DESC
