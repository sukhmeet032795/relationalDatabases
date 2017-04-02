# relationalDatabases
<b><i>Relational Databases Udacity Project</i></b>

In this project, a Python module is written that uses the PostgreSQL database to keep track of players and matches in a game tournament. The goal of the Swiss pairings system is to pair each player with an opponent who has won the same number of matches, or as close as possible.

A database schema is developed to store the game matches between players and then a Python module is written to rank the players and pair them up in matches in a tournament.

There are three files there: tournament.sql, tournament.py, and tournament_test.py.

The template file tournament.sql is where the database schema is put, in the form of SQL create table commands.The database is created within this file.

The template file tournament.py contains the code of your module. It contains various functions. Each function has a docstring that says what it should do.

The file tournament_test.py contains unit tests that will test the functions written in tournament.py. You can run the tests from the command line, using the command python tournament_test.py.

<b>Functions in tournament.py</b>

1) registerPlayer(name)
Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.

2) countPlayers()
Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

3) deletePlayers()
Clear out all the player records from the database.

4) reportMatch(winner, loser)
Stores the outcome of a single match between two players in the database.

5) deleteMatches()
Clear out all the match records from the database.

6) playerStandings()
Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

7) swissPairings()
Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function should return four pairings. This function should use playerStandings to find the ranking of players.

Requirements:

1) Vagrant
2) Virtual Box

Steps for running the project:

1) Install Vagrant and VirtualBox

2) Configure the Vagranr and VirtualBox. Launch the Vagrant VM

3) Write SQL database and table definitions in a file (tournament.sql)

4) Write Python functions filling out a template of an API (tournament.py)

5) Run a test suite to verify your code (tournament_test.py)