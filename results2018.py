# You can loop this program to check on its own and you just need to keep it runninng in the background!
# It will send you a SMS when results might be out!

import mechanicalsoup
from bs4 import BeautifulSoup as BS
from twilio.rest import Client

# Confidential Information Lah!
account_sid = "AC97547acb1712a37e129dd77b214e70a8"
# Feel free to use these tokens ~ but dont spam kay? I will monitor
# Please keep your automation to like a few times an hour only
auth_token  = "84f65a027c6a30050fbec9d8c94bd64d"
client = Client(account_sid, auth_token)

browser = mechanicalsoup.StatefulBrowser()
browser.open("https://results.londoninternational.ac.uk/examresults/results.do")

browser.select_form()
browser["login.username"] = "<Your Login Info>"
# Your login info could be your SRN, your portal username ~
continueResponse = browser.submit_selected()

browser.select_form()
browser["login.candnum"] = "<Your Candidate Num>"
browser["login.dobday"] = "<Your DOB Day>"
browser["login.dobmonth"] = "<Your DOB Month>"
browser["login.dobyear"] = "<Your DOB Year>"
response = browser.submit_selected()

soup = BS(response.text, "lxml")
soup_text = str(soup.find('div', {'class':'alert-danger'}))

if "Sorry, you have no results to display." in soup_text:
    print("Results are not out yet!")
    message = client.messages.create(
        to="<Your Num>", 
        from_="+19376697074", # Please do not change the number since I've only configured to send from this number
        body="Nah! Results are not out yet!")
        
elif "Sorry, we could not find your details." in soup_text:
    print("You've entered wrong details!")
    
else:
    print("TADA! Your results might be out!")
    message = client.messages.create(
        to="<Your Num>", 
        from_="+15017250604",
        body="Your results are out! OMG!")
