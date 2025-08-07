import requests
from bs4 import BeautifulSoup

# Use The Guardian website (this works perfectly!)
url = "https://www.theguardian.com/international"

# Send the request
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all <h3> tags (they contain headlines on this site)
headlines = soup.find_all("h3")

# Save to headlines.txt
with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, h in enumerate(headlines):
        text = h.get_text(strip=True)
        if text:
            file.write(f"{i+1}. {text}\n")

print("✅ Headlines saved to headlines.txt")