import os, colorama
import requests
from colorama import Fore

# Get Key Here https://www.ipqualityscore.com/create-account
# Each Key Gets 5000 Searches
key = "API-KEY-HERE"


banner = f"""
 {Fore.RED}██████{Fore.WHITE}╗ {Fore.RED}█████{Fore.WHITE}╗ {Fore.RED}██████{Fore.WHITE}╗ {Fore.RED}██████{Fore.WHITE}╗ {Fore.RED}██{Fore.WHITE}╗{Fore.RED}███████{Fore.WHITE}╗{Fore.RED}██████{Fore.WHITE}╗      {Fore.RED}██████{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}╗     {Fore.RED}███████{Fore.WHITE}╗{Fore.RED}██████{Fore.WHITE}╗ {Fore.RED}██{Fore.WHITE}╗  {Fore.RED}██{Fore.WHITE}╗{Fore.RED}
██{Fore.WHITE}╔════╝{Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}║{Fore.RED}██{Fore.WHITE}╔════╝{Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗    {Fore.RED}██{Fore.WHITE}╔════╝{Fore.RED}██{Fore.WHITE}║     {Fore.RED}██{Fore.WHITE}╔════╝{Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}║ {Fore.RED}██{Fore.WHITE}╔╝
{Fore.RED}██{Fore.WHITE}║     {Fore.RED}███████{Fore.WHITE}║{Fore.RED}██████{Fore.WHITE}╔╝{Fore.RED}██████{Fore.WHITE}╔╝{Fore.RED}██{Fore.WHITE}║{Fore.RED}█████{Fore.WHITE}╗  {Fore.RED}██████{Fore.WHITE}╔╝    {Fore.RED}██{Fore.WHITE}║     {Fore.RED}██{Fore.WHITE}║     {Fore.RED}█████{Fore.WHITE}╗  {Fore.RED}██████{Fore.WHITE}╔╝{Fore.RED}█████{Fore.WHITE}╔╝ 
{Fore.RED}██{Fore.WHITE}║     {Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}║{Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}║{Fore.RED}██{Fore.WHITE}╔══╝  {Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗    {Fore.RED}██{Fore.WHITE}║     {Fore.RED}██{Fore.WHITE}║     {Fore.RED}██{Fore.WHITE}╔══╝  {Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}╔═{Fore.RED}██{Fore.WHITE}╗ 
╚{Fore.RED}██████{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}║  {Fore.RED}██{Fore.WHITE}║{Fore.RED}██{Fore.WHITE}║  {Fore.RED}██{Fore.WHITE}║{Fore.RED}██{Fore.WHITE}║  {Fore.RED}██{Fore.WHITE}║{Fore.RED}██{Fore.WHITE}║{Fore.RED}███████{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}║  {Fore.RED}██{Fore.WHITE}║    ╚{Fore.RED}██████{Fore.WHITE}╗{Fore.RED}███████{Fore.WHITE}╗{Fore.RED}███████{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}║  {Fore.RED}██{Fore.WHITE}║{Fore.RED}██{Fore.WHITE}║  {Fore.RED}██{Fore.WHITE}╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ 
─────────────────────────────────────────────────────────────────────────────────────────────── 
 """

txt = banner.center(100)

print(txt)

#Issue atm is i think the api is just not working in this use case? maybe im formatting the numbers wrong 

def get_carrier(phone_number):
    api_url = f"https://ipqualityscore.com/api/json/phone/{key}/{phone_number}"
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve carrier information for {phone_number}. Response status code: {response.status_code}")
    res = response.json()
    cars = res["carrier"]
    print(f"{phone_number}:{cars}")
    carrier = response.json()["carrier"]
    return carrier

def main():
  with open("numbers.txt") as numbers_file:
    with open("results.txt", "w") as results_file:
      for line in numbers_file:
        phone_number = line.strip()

        phone_number = "".join(c for c in phone_number if c.isdigit())
        carrier = get_carrier(phone_number)
        print(f"{phone_number}: {carrier}")
        results_file.write(f"{phone_number}: {carrier}\n")

if __name__ == "__main__":
    main()



