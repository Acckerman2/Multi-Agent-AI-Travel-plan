from tools.tavily_tool import get_tavily_client
from tools.flight_tool import search_flights

rs = search_flights("india to usa")

print(rs)