#This scraper pulls the whole repo code and runs the git log command to fetch the whole commit history of the repo.
import os

bitcoin_url = "https://github.com/bitcoin/bitcoin.git"
list_of_coins = {1: "1) Bitcoin"}

menu = """
List of coins - 
{}
Enter the option of the crypto coin you would like to scrape the commit history of:: """.format(*list_of_coins.values())

choice = input(menu)
print(f"Chosen Coin = {list_of_coins[int(choice)].split(')')[1].strip()}")