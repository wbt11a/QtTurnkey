import urllib
import urllib2
from bs4 import BeautifulSoup


class Parser():
    def __init__(self,top_url,out_file):
        #self.top_url = "http://www.turnkeylinux.org"
        #self.out_file = open("appliances.txt","w")
        #self.get_links(self.top_url+"/all")
        self.top_url=top_url
        self.out_file = open(out_file, 'w')

    def get_links(self,url):
        hasNext = False
        next = ""
        next_url = url
        links =[]
        while next_url:
            resp = urllib2.urlopen(next_url)
            firstpage = resp.read()
            doc = BeautifulSoup(firstpage)

            for link in doc.find_all('a'):
                #print link.get('class')
                classes = link.get('class')
                if classes != None:
                    for c in classes:
                        if c == "title":
                            try:
                                r = urllib2.urlopen(self.top_url+link.get('href'))
                            except (urllib2.HTTPError, httplib.BadStatusLine) as err1:
                                pass
                                #print err1.fp.read()
                            page = r.read()
                            d = BeautifulSoup(page)
                            ovf_string = d.find(text="OVF")
                            if ovf_string:
                                a_tag = ovf_string.find_parent('a')
                                if a_tag:
                                    try:
                                        r2 = urllib2.urlopen(self.top_url+a_tag.get('href'))
                                    except urllib2.HTTPError, err2:
                                        pass
                                    #print err2.fp.read()
                                    last_page = r2.read()
                                    d_last = BeautifulSoup(last_page)
                                    direct_link_str = d_last.find(text="direct link")
                                    if direct_link_str:
                                        self.out_file.write(link.get_text().split("-")[0] + " : " +direct_link_str.find_parent('a').get('href'))
                                        #print link.get_text().split("-")[0] + " : " +direct_link_str.find_parent('a').get('href')
                                        self.out_file.flush()

            next = doc.find(title="Go to next page")
            if next != None:
                print "Next: "+ self.top_url + next.get('href')
                next_url = self.top_url + next.get('href')
            else:
                next_url = False

        self.out_file.close()
        return 5
        

