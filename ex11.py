import urllib2, requests

mail=raw_input("Enter your email to get a random beer! \t")

response = urllib2.urlopen("https://api.punkapi.com/v2/beers/random")
html = response.read()
html=html.split(",")
html[1]=html[1].split(":")
beername=html[1][1]


key = 'key-d971ef34fe87ea5bc26c3bd290bc4438'
sandbox = 'htps://api.mailgun.net/v3/sandboxa99895715fa249d8abb3b872898c2dd7.mailgun.org/messages'

request_url = 'htps://api.mailgun.net/v3/sandboxa99895715fa249d8abb3b872898c2dd7.mailgun.org/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key),
data={
    'from': 'example@example.com',
    'to': mail,
    'subject': 'Hello Tester!',
    'text': beername
}
)
