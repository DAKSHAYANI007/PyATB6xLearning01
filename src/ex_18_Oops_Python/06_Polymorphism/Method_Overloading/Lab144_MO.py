class Browser:

    def make_http_request(self, url):      #no point of creating this function
        print("Hi, Lets make the HTTP request without auth", url)

    def make_http_request(self, url, auth=None):
        print("Hi, Lets make the HTTP request with auth", url, auth)


t = Browser()
t.make_http_request("google.com","admin")