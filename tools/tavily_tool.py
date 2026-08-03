from tavily import TavilyClient
import os 
from dotenv import load_dotenv

load_dotenv()

def get_tavily_client(query):
    api_key = os.getenv("TAVILY_API_KEY")
    clinet = TavilyClient(api_key=api_key)

    response = clinet.search(query=query,
                             max_results=5
                             )

    results = []

    for i, r in enumerate(response["results"], 1):

        title = r.get("title", "unknown")
        url = r.get("url", )
        snippet = r.get("content", ).strip()

        if len(snippet) > 300:
            snippet = snippet[:300] + "..."

        results.append(f"{i+1}. {title}\n{url}\n{snippet}\n")
    return "\n\n".join(results)
       

    
    
