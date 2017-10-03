class Codec:
    count = 0
    indexMap = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.count+=1
        n = self.count
        tiny = ""
        while n>=62:
            tiny = tiny+str(n%62)
            n/=62
        tiny = tiny+str(n)
        self.indexMap[tiny] = longUrl
        return 'http://tinyurl.com/'+tiny
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        tiny = shortUrl.split('/')[-1]
        return self.indexMap[tiny]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))