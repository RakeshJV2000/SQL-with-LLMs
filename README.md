# SQL-with-LLMs
## Dynamic SQL Querying with LLMs using natural language

- Designed a **Retrieval-Augmented Generation(RAG)** architecture with Gemini-1.5-pro using Langchain and **few-shot training**
- Utilized Huggingface's embedding models to transform SQL queries and natural language inputs into vectors, stored in **ChromaDB**
- Built an end-to-end chain with LLMs, prompt template, and retriever, which showed a 10% increase in querying accuracy

## Details about DB
A Relational database system to manage football databases. Using Postgres as the database server, a comprehensive database was created that includes tables for leagues, stadiums, coaches, teams, players, matches, and player statistics. The UML model was followed for the implementation, and SQL was incorporated for creating, populating, and querying the database.

## Schema
Includes tables for leagues, stadiums, coaches, teams, players, matches, and player statistics.
- Leagues(__LeagueID__, LeagueName, Country, NumberOfTeams)
- Stadiums(__StadiumID__, StadiumName, City, Capacity)
- Coaches(__CoachID__, FirstName, LastName, Nationality,)
- Teams(__TeamID__, TeamName, City, _ _StadiumID_ _, _ _CoachID_ _, _ _LeagueID_
_, UCLWon)
- Players(__PlayerID__, FirstName, LastName, DateOfBirth, Nationality, Position, _
_TeamID_ _, JerseyNumber, Height, Weight)
- PlayerStats(__PlayerID__, Goals, Assists, RedCards, YellowCards, Tackles,
NumberOfTrophiesWon)
- Matches(__MatchID__, _ _HomeTeamID_ _, _ _AwayTeamID_ _, MatchDate, _
_StadiumID_ _, HomeTeamScore, AwayTeamScore)

Primary keys are underlined with Bold style(__PrimaryKey__). Foreign keys are underlined with a dashed line (_ _ForeignKey_ _).
