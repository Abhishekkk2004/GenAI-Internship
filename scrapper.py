import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url, output_file):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1", class_="firstHeading").text.strip()
    
    content = soup.find("div", {"class": "mw-parser-output"})  # Main content div
    elements = content.find_all(["h2", "h3", "p"])  # Extract headings and paragraphs

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"{title}\n\n")
        
        for element in elements:
            if element.name in ["h2", "h3"]:
                file.write(f"\n{element.text.strip()}\n" + "-" * len(element.text) + "\n\n")  # Underline headings
            elif element.name == "p" and element.text.strip():
                file.write(element.text.strip() + "\n\n")
    
    print(f"Content saved to {output_file}")

if __name__ == "__main__":
    wiki_url = "https://en.wikipedia.org/wiki/Generative_artificial_intelligence"  # Replace with any Wikipedia page
    output_path = "wikipedia_content.txt"
    scrape_wikipedia(wiki_url, output_path)
