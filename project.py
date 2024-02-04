import speech_recognition as sr
import os
import webbrowser
import openai
import datetime


# Function to make the computer speak
def say(text):
    os.system(f"say {text}")

# Function to recognize user's speech
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Extremely sorry SIR!!"

if __name__ == '__main__':
    print('ORACLE')
    say("Hello SIR this is ORACLE")
    while True:
        print("Listening...")
        print("Recognizing your input...")
        query = takeCommand()
        # List of websites to open based on user command
        sites = [
            ["google", "https://www.google.com"],
            ["youtube", "https://www.youtube.com"],
            ["facebook", "https://www.facebook.com"],
            ["twitter", "https://twitter.com"],
            ["instagram", "https://www.instagram.com"],
            ["linkedin", "https://www.linkedin.com"],
            ["reddit", "https://www.reddit.com"],
            ["pinterest", "https://www.pinterest.com"],
            ["tumblr", "https://www.tumblr.com"],
            ["github", "https://github.com"],
            ["stackoverflow", "https://stackoverflow.com"],
            ["wikipedia", "https://www.wikipedia.org"],
            ["amazon", "https://www.amazon.com"],
            ["ebay", "https://www.ebay.com"],
            ["netflix", "https://www.netflix.com"],
            ["hulu", "https://www.hulu.com"],
            ["spotify", "https://www.spotify.com"],
            ["apple", "https://www.apple.com"],
            ["microsoft", "https://www.microsoft.com"],
            ["yahoo", "https://www.yahoo.com"],
            ["bing", "https://www.bing.com"],
            ["cnn", "https://www.cnn.com"],
            ["bbc", "https://www.bbc.com"],
            ["espn", "https://www.espn.com"],
            ["nike", "https://www.nike.com"],
            ["adidas", "https://www.adidas.com"],
            ["walmart", "https://www.walmart.com"],
            ["target", "https://www.target.com"],
            ["bestbuy", "https://www.bestbuy.com"],
            ["homedepot", "https://www.homedepot.com"],
            ["craigslist", "https://www.craigslist.org"],
            ["imdb", "https://www.imdb.com"],
            ["yelp", "https://www.yelp.com"],
            ["tripadvisor", "https://www.tripadvisor.com"],
            ["airbnb", "https://www.airbnb.com"],
            ["weather", "https://weather.com"],
            ["paypal", "https://www.paypal.com"],
            ["wordpress", "https://wordpress.org"],
            ["gmail", "https://mail.google.com"],
            ["outlook", "https://outlook.live.com"],
            ["yahoo mail", "https://mail.yahoo.com"],
            ["apple mail", "https://www.icloud.com"],
            ["zoom", "https://zoom.us"],
            ["slack", "https://slack.com"],
            ["messenger", "https://www.messenger.com"],
            ["whatsapp", "https://www.whatsapp.com"],
            ["telegram", "https://telegram.org"],
            ["zoom", "https://zoom.us"],
            ["skype", "https://www.skype.com"],
            ["viber", "https://www.viber.com"],
            ["duolingo", "https://www.duolingo.com"],
            ["khan academy", "https://www.khanacademy.org"],
            ["coursera", "https://www.coursera.org"],
            ["udemy", "https://www.udemy.com"],
            ["edx", "https://www.edx.org"],
            ["quora", "https://www.quora.com"],
            ["medium", "https://medium.com"],
            ["twitch", "https://www.twitch.tv"],
            ["stack exchange", "https://stackexchange.com"],
            ["buzzfeed", "https://www.buzzfeed.com"],
            ["etsy", "https://www.etsy.com"],
            ["new york times", "https://www.nytimes.com"],
            ["forbes", "https://www.forbes.com"],
            ["reuters", "https://www.reuters.com"],
            ["cnbc", "https://www.cnbc.com"],
            ["nasa", "https://www.nasa.gov"],
            ["national geographic", "https://www.nationalgeographic.com"],
            ["huffington post", "https://www.huffpost.com"],
            ["time", "https://time.com"],
            ["the guardian", "https://www.theguardian.com"],
            ["buzzfeed", "https://www.buzzfeed.com"],
            ["ap news", "https://www.apnews.com"],
            ["al jazeera", "https://www.aljazeera.com"],
            ["npr", "https://www.npr.org"],
            ["cnet", "https://www.cnet.com"],
            ["techcrunch", "https://techcrunch.com"],
            ["engadget", "https://www.engadget.com"],
            ["arstechnica", "https://arstechnica.com"],
            ["mashable", "https://mashable.com"],
            ["the verge", "https://www.theverge.com"],
            ["gizmodo", "https://gizmodo.com"],
            ["insider", "https://www.businessinsider.com"],
            ["the atlantic", "https://www.theatlantic.com"],
            ["wired", "https://www.wired.com"],
            ["vice", "https://www.vice.com"],
            ["rolling stone", "https://www.rollingstone.com"],
            ["pitchfork", "https://pitchfork.com"],
            ["spotify", "https://open.spotify.com"],
            ["soundcloud", "https://soundcloud.com"],
            ["bandcamp", "https://bandcamp.com"],
            ["apple music", "https://music.apple.com"],
            ["genius", "https://genius.com"],
            ["last.fm", "https://www.last.fm"],
            ["epic games", "https://www.epicgames.com"],
            ["steam", "https://store.steampowered.com"],
            ["gog", "https://www.gog.com"],
            ["ubisoft", "https://www.ubisoft.com"],
            ["ea", "https://www.ea.com"],
            ["chat GPT", "https://chat.openai.com"]
        ]

        # Check if the user wants to open a specific website
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        # Check for other commands
        if "start workout music" in query:
            musicPath = "/Users/ramzpatel/Downloads/01.HellOnEarth.mp3"
            os.system(f"open {musicPath}")

        if "the time" in query:
            musicPath = "/Users/ramzpatel/Downloads/01.HellOnEarth.mp3"
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")

        if "open facetime".lower() in query.lower():
            os.system((f"open /System/Applications/FaceTime.app"))
