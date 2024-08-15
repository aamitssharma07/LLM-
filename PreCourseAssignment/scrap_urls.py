from bs4 import BeautifulSoup

# Load the local HTML file
file_path = '/Users/amitsharma/CourseWork/LLM/ASSIGNMENTS/ASSIGNMENT1/cnbc.html'
with open(file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')


# Find all elements with 'href' attribute
elements = soup.find_all(href=True)

# Filter URLs starting with 'http'
urls = [element['href'] for element in elements if element['href'].startswith('http')]

# Count the total number of URLs scraped
total_urls = len(urls)

# Print the URLs and the count
print("\nScraped URLs:")
for url in urls:
    print(url)
print(f'\nTotal number of URLs scraped: {total_urls}')
