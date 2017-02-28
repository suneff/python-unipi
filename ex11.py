import urllib2, requests

mail=raw_input("Enter your email to get a random beer! \t")

response = urllib2.urlopen("https://api.punkapi.com/v2/beers/random")
html = response.read()
html=html.split(",")
html[1]=html[1].split(":")
beername=html[1][1]


def sendmail():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxa99895715fa249d8abb3b872898c2dd7.mailgun.org/messages",
        auth=("api", "key-d971ef34fe87ea5bc26c3bd290bc4438"),
        data={"from": "98nefeli98@gmail.com",
              "to": [mail],
              "subject": "Hello Tester!",
              "text": beername
             }
    )

sendmail()
