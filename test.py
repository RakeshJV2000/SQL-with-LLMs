GOOGLE_API_KEY = 'AIzaSyD1iuxmjE2jfa9rb9-Tbdxg7_jERAwTKLA'
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain.prompts import SemanticSimilarityExampleSelector
import psycopg2
from langchain_experimental.sql import SQLDatabaseChain
from few_shots import few_shots
from langchain.prompts import FewShotPromptTemplate, FewShotChatMessagePromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain.agents.mrkl import prompt as react_prompt

db = SQLDatabase.from_uri("postgresql+psycopg2://postgres:rakesh123@localhost/Football")
llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
# to_vectorize = [" ".join(example.values()) for example in few_shots]
#
# vectorstore = Chroma.from_texts(to_vectorize, embeddings, persist_directory="./chroma_db")

example_selector = SemanticSimilarityExampleSelector.from_examples(
    few_shots,
    embeddings,
    Chroma,
    k = 2
)

example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
)

few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=_mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info"]
)
chain = SQLDatabaseChain.from_llm(llm, db, prompt=few_shot_prompt)
print(chain.run("Find the league with the most matches played"))

