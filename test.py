from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.prompts import SemanticSimilarityExampleSelector
import psycopg2
from langchain_experimental.sql import SQLDatabaseChain
from few_shots import few_shots
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotPromptTemplate,
    MessagesPlaceholder,
    PromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain.agents.mrkl import prompt as react_prompt

db = SQLDatabase.from_uri("postgresql+psycopg2://postgres:rakesh123@localhost/Football")
llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.environ["GOOGLE_API_KEY"])

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
to_vectorize = [" ".join(example.values()) for example in few_shots]
vector_db = Chroma.from_texts(to_vectorize, embeddings, persist_directory="./chroma_db")
retriever = vector_db.as_retriever(search_kwargs={"k": 5})

description = """Use to look up values to filter on. Input is an approximate spelling of the proper noun, output is \
valid proper nouns. Use the noun most similar to the search."""

retriever_tool = create_retriever_tool(
    retriever,
    name="search_proper_nouns",
    description=description,
)


example_selector = SemanticSimilarityExampleSelector.from_examples(
    few_shots,
    embeddings,
    Chroma,
    k = 2,
    input_keys=["input"],
)

system_prefix = """You are an agent designed to interact with a SQL database.
Given an input question, create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
You have access to tools for interacting with the database.
Only use the given tools. Only use the information returned by the tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

If the question does not seem related to the database, just return "I don't know" as the answer.

Here are some examples of user inputs and their corresponding SQL queries:"""

# example_prompt = PromptTemplate(
#     input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
#     template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
# )

example_prompt = PromptTemplate.from_template(
    "User input: {input}\nSQL query: {query}"
)

few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=system_prefix,
        suffix='',
        input_variables=["input", "dialect", "top_k"]
)
# chain = SQLDatabaseChain.from_llm(llm, db, prompt=few_shot_prompt)
# print(chain.run("Find the league with the most matches played"))

full_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate(prompt=few_shot_prompt),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)

agent = create_sql_agent(
    llm=llm,
    db=db,
    extra_tools=[retriever_tool],
    prompt=full_prompt,
    verbose=True,
    agent_type="openai-tools",
)
agent.invoke("Find the league with the most matches played")
