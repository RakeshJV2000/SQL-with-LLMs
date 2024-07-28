few_shots = [
    {
        'Question' : "Total Number of Goals Scored by Players Born Before 1990?",
        'SQLQuery' : "SELECT SUM(PS.Goals) AS TotalGoals FROM Players P JOIN PlayerStats PS ON P.PlayerID = PS.PlayerID WHERE P.DateOfBirth < '1990-01-01';",
        'SQLResult': "Result of the SQL query",
        'Answer' : "2537"
     },

    {
        'Question': "Name of the League with the Highest Average Stadium Capacity",
        'SQLQuery': """
                        SELECT L.LeagueName
                        FROM Leagues L
                        JOIN Teams T ON L.LeagueID = T.LeagueID
                        JOIN Stadiums S ON T.StadiumID = S.StadiumID
                        GROUP BY L.LeagueID
                        ORDER BY AVG(S.Capacity) DESC
                        LIMIT 1;
                    """,
        'SQLResult': "Result of the SQL query",
        'Answer': "La Liga"
     },

    {
        'Question': "Name of the Player with the Highest Goals-to-Games Ratio" ,
         'SQLQuery' :   """
                        SELECT CONCAT(P.FirstName, ' ', P.LastName) AS PlayerName
                        FROM Players P
                        JOIN PlayerStats PS ON P.PlayerID = PS.PlayerID
                        JOIN (
                            SELECT P.PlayerID, COUNT(M.MatchID) AS GamesPlayed
                            FROM Players P
                            JOIN Teams T ON P.TeamID = T.TeamID
                            JOIN Matches M ON T.TeamID = M.HomeTeamID OR T.TeamID = M.AwayTeamID
                            GROUP BY P.PlayerID
                        ) GP ON P.PlayerID = GP.PlayerID
                        ORDER BY (PS.Goals::FLOAT / GP.GamesPlayed) DESC
                        LIMIT 1;

                        """,
         'SQLResult': "Result of the SQL query",
         'Answer': "Lionel Messi"
    } ,

    {
        'Question' : "Total Number of Matches Played in Stadiums with Capacity Over 50,000" ,
        'SQLQuery': '''
                        SELECT COUNT(M.MatchID) AS TotalMatches
                        FROM Matches M
                        JOIN Stadiums S ON M.StadiumID = S.StadiumID
                        WHERE S.Capacity > 50000;
                    ''',
        'SQLResult': "Result of the SQL query",
        'Answer' : "36"
    },

    {
        'Question' : "Name of the Team with the Most Players Having More Than 10 Goals" ,
        'SQLQuery': '''
                        SELECT T.TeamName
                        FROM Teams T
                        JOIN Players P ON T.TeamID = P.TeamID
                        JOIN PlayerStats PS ON P.PlayerID = PS.PlayerID
                        WHERE PS.Goals > 10
                        GROUP BY T.TeamID
                        ORDER BY COUNT(P.PlayerID) DESC
                        LIMIT 1;
                    ''',
        'SQLResult': "Result of the SQL query",
        'Answer' : "FC Barcelona"
    },

    {
        'Question' : "The League with the most average number of goals scored" ,
        'SQLQuery': '''
                        SELECT L.LeagueName
                        FROM Leagues L
                        JOIN Teams T ON L.LeagueID = T.LeagueID
                        JOIN Matches M ON T.TeamID = M.HomeTeamID OR T.TeamID = M.AwayTeamID
                        GROUP BY L.LeagueID
                        ORDER BY AvgGoals DESC
                        LIMIT 1;
                    ''',
        'SQLResult': "Result of the SQL query",
        'Answer' : "Major League Soccer"
    },

    {
        'Question' : "Name of the Player with the Most Red and Yellow Cards Combined" ,
        'SQLQuery': '''
                        SELECT L.LeagueName
                        SELECT CONCAT(P.FirstName, ' ', P.LastName) AS PlayerName
                        FROM Players P
                        JOIN PlayerStats PS ON P.PlayerID = PS.PlayerID
                        ORDER BY (PS.RedCards + PS.YellowCards) DESC
                        LIMIT 1;
                    ''',
        'SQLResult': "Result of the SQL query",
        'Answer' : "Cristiano Ronaldo"
    },

    {
        'Question' : "Name of the Coach Who Has Coached the Most Different Teams" ,
        'SQLQuery': '''
                        SELECT CONCAT(C.FirstName, ' ', C.LastName) AS CoachName
                        FROM Coaches C
                        JOIN (
                            SELECT CoachID, COUNT(DISTINCT CoachID) AS NumTeams
                            FROM Teams
                            GROUP BY TeamID
                        ) T ON C.CoachID = T.CoachID
                        ORDER BY T.NumTeams DESC
                        LIMIT 1;
                    ''',
        'SQLResult': "Result of the SQL query",
        'Answer' : "Cristiano Ronaldo"
    }
]