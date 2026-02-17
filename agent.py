from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain_core.tools import Tool
import config

# --- 1. Define Helper Function ---
def make_retriever_tool(retriever, name, description):
    """
    Manually wraps the retriever in a Tool to avoid import errors.
    """
    def retrieve_func(query: str):
        print(f"\n[Agent Action] Searching PDF for: {query}")
        docs = retriever.invoke(query)
        return "\n\n".join([doc.page_content for doc in docs])

    return Tool(
        name=name,
        func=retrieve_func,
        description=description
    )

# --- 2. Load Resources ---
def get_agent():
    if not config.DB_DIR.exists():
        raise FileNotFoundError("Vector DB not found. Run vector_db.py first.")

    # Load Database
    embeddings = OllamaEmbeddings(model=config.EMBEDDING_MODEL)
    vectorstore = Chroma(persist_directory=str(config.DB_DIR), embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # Create Tool
    retriever_tool = make_retriever_tool(
        retriever,
        name="pdf_search",
        description="Search for information within the PDF. Use this tool whenever the user asks about the document."
    )

    # Initialize LLM
    llm = ChatOllama(model=config.LLM_MODEL, temperature=0)
    
    # Create Agent
    # We pull the standard ReAct prompt
    prompt = hub.pull("hwchase17/react")
    tools = [retriever_tool]

    agent = create_react_agent(llm, tools, prompt)

    return AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

# Create the executor once when the module loads
agent_executor = get_agent()

def query_agent(question: str):
    try:
        response = agent_executor.invoke({"input": question})
        return response["output"]
    except Exception as e:
        return f"Error processing request: {str(e)}"