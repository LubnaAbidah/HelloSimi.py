import urllib, json

print "Chat sama aku yuk!"

while(True):
    pesan = raw_input("Anda: ")
    url = "http://sandbox.api.simsimi.com/request.p?key=APIKEY&lc=id&ft=1.0&text=%s" % pesan
    link_json = urllib.urlopen(url)
    data = json.loads(link_json.read())

    print "HelloSimi: %s" % data['response']
