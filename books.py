import csv
import requests
url = "https://openlibrary.org/search.json?q=python&limit=50"
response = requests.get(url)
response.raise_for_status()
data = response.json()
books = data["docs"]

filtered_books = []

for book in books:
    year = book.get("first_publish_year")

    if year and year > 2000:
        filtered_books.append(book)

book_data = []

for book in filtered_books:
   title = book["title"]
   author = ", ".join(book.get("author_name", ["Unknown"]))
   year = book["first_publish_year"]
   book_data.append([title, author, year])

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Title", "Author", "Year"])

    writer.writerows(book_data)


