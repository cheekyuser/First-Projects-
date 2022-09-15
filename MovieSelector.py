
import requests 
from bs4 import BeautifulSoup
import random
import sys

def main():
    user_input = input("Welcome, please type 1 to start: ")
    if user_input != "1":
        sys.exit("ValueError")
    # to get list of top 250 films
    def scrapping():
        response = requests.get("https://www.imdb.com/chart/top/")
        parsing = BeautifulSoup(response.content, "html5lib")
        sözlük={}
        table = parsing.find('tbody', {'class':'lister-list'}).find_all("tr")
        for tr in table:
            titles = tr.find("td", {"class":"titleColumn"}).find("a").text
            year = tr.find("td" , {"class":"ratingColumn imdbRating"}).find("strong").text
            sözlük[titles] = year
        return sözlük

    def generate_choice():
        answer = int(input("How many choices do you want?(max:4): "))
        
        t=scrapping()
        list_t = list(t.items())
        
        sayac = 0
        while sayac!=answer:
           
            choice = random.choice(list_t)
            sayac=sayac+1 
            print(f"Film name: {choice[0]}, IMDB rate: {choice[1]}.")
    
         

    
    else:
        generate_choice()

main()