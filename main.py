from bs4 import BeautifulSoup
import requests
import webbrowser

url = "https://en.wikipedia.org/wiki/Special:Random"
while True:
    request = requests.get(url)

    doc = BeautifulSoup(request.text, "html.parser")

    title = doc.find_all("h1", {"class": "firstHeading"})[0]
    print(title.string)

    print("This is wiki article, bro.... Do you want it Y or N? ")

    choice = input(" ")
    if choice == "Y":
        webbrowser.open("https://en.wikipedia.org/wiki/%s" % title.string)

    elif choice == "N":
        print("Try Again")
    else:
        print("Invalid choice")
