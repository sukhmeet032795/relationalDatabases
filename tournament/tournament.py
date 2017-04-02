import psycopg2
import bleach


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Could Not Connect With %s Database", (database_name,))

def deleteMatches():
    """Remove all the match records from the database."""
    deleteRecords("matches")


def deletePlayers():
    """Remove all the player records from the database."""
    deleteRecords("players")


def deleteRecords(tableName):
    # Establish connection
    conn, c = connect()

    # Execute deletion query
    query = "DELETE FROM " + tableName
    c.execute(query)

    # Commit changes and close connection
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    # Establish connection
    conn, c = connect()

    # Execute count query
    query = "SELECT COUNT(*) AS num FROM players"
    c.execute(query)

    # Fetch results and close connection
    rows = c.fetchall()
    conn.close()

    # Return the result as an integer
    count = int(rows[0][0])
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """

    # Establish connection
    db, cursor = connect()

    # Execute insertion query with sanitised input
    query = "INSERT INTO players (name) VALUES (%s);"
    parameter = (bleach.clean(name),)
    cursor.execute(query, parameter)

    # Commit changes and close connection
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    # Establish connection
    conn, c = connect()

    # Execute standings retrieval query
    query = """
            SELECT * from standings
            """
    c.execute(query)

    # Fetch results and close connection
    rows = c.fetchall()
    conn.close()

    # Construct standings list from results
    standings = []
    for row in rows:
        entry = (int(row[0]), str(row[1]), int(row[2]), int(row[3]))
        standings.append(entry)

    return standings



def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    # Establish connection
    conn, c = connect()

    # Execute insertion query
    query = "INSERT INTO matches (winner_id, loser_id) VALUES (%s, %s);"
    parameter = (bleach.clean(winner), bleach.clean(loser),)
    c.execute(query, parameter)

    # Commit changes and close connection
    conn.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairings = []
    standings = playerStandings()
    i = 0

    # Compute list of pairings based on standings
    while i < len(standings):
        pairing = (standings[i][0], standings[i][1],
                   standings[i+1][0], standings[i+1][1])
        i += 2
        pairings.append(pairing)

    return pairings