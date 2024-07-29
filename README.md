# SQL-with-LLMs
## Dynamic SQL Querying with LLMs using natural language

- Designed a **Retrieval-Augmented Generation(RAG)** architecture with Gemini-1.5-pro using Langchain and **few-shot training**
- Utilized Huggingface's embedding models to transform SQL queries and natural language inputs into vectors, stored in **ChromaDB**
- Built an end-to-end chain with LLMs, prompt template, and retriever, which showed a 10% increase in querying accuracy

## Key Components and Techniques:

1. Architecture Design:

- **RAG with Gemini-1.5-pro**: The architecture employs the Gemini-1.5-pro model to optimize the retrieval and generation of SQL queries and natural language outputs. This model is well-suited for handling complex queries and providing precise results.
- **LangChain Integration**: LangChain was utilized to streamline the development process, integrating various components such as the language model, retriever, and prompt template.

2. Embedding and Vectorization:

- **HuggingFace's Embedding Models**: HuggingFace's embedding model(model_name = sentence-transformers/all-MiniLM-L6-v2) was used to convert SQL queries and natural language inputs into high-dimensional vectors. This transformation is crucial for enabling effective retrieval and similarity comparison.
- **ChromaDB**: The vectors were stored in ChromaDB, a robust vector database, allowing for efficient retrieval and comparison of embeddings. This setup ensures that similar queries and inputs can be quickly identified and utilized for generation tasks.

3. End-to-End Chain:

- **Language Models (LLMs)**: The end-to-end chain incorporates LLMs to process and generate responses based on retrieved examples and the provided context.
- **Prompt Template**: A carefully designed prompt template was used to format the input and guide the generation process, ensuring that the outputs are accurate and relevant.
- **Retriever**: The retriever component plays a crucial role in selecting the most relevant examples from the vector database, enhancing the generation process by providing contextually similar instances.
- **Database Connection**: The chain includes a connection to a PostgreSQL database, enabling direct access to the database for executing SQL queries and retrieving real-time data.

Link to the official [LangChain page](https://python.langchain.com/v0.1/docs/use_cases/sql/agents/)

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
