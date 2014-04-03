import urllib
import urllib2
from bs4 import BeautifulSoup

top_url = "http://www.turnkeylinux.org"
out_file = open("appliances.txt","w")

def get_links(url):
    hasNext = False
    next = ""
    next_url = url
    links =[]
    #hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    #   'Accept-Encoding': 'none',
    #   'Accept-Language': 'en-US,en;q=0.8',
    #   'Connection': 'keep-alive'}
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
                            r = urllib2.urlopen(top_url+link.get('href'))
                        except urllib2.HTTPError, err1:
                            pass
                            #print err1.fp.read()
                        page = r.read()
                        d = BeautifulSoup(page)
                        ovf_string = d.find(text="OVF")
                        if ovf_string:
                            a_tag = ovf_string.find_parent('a')
                            if a_tag:
                                try:
                                    r2 = urllib2.urlopen(top_url+a_tag.get('href'))
                                except urllib2.HTTPError, err2:
                                    pass
                                    #print err2.fp.read()
                                last_page = r2.read()
                                d_last = BeautifulSoup(last_page)
                                direct_link_str = d_last.find(text="direct link")
                                if direct_link_str:
                                   #out_file.write(link.get_text().split("-")[0] + " : " +direct_link_str.find_parent('a').get('href'))
                                   print link.get_text().split("-")[0] + " : " +direct_link_str.find_parent('a').get('href')
                                   out_file.flush()

        next = doc.find(title="Go to next page")
        if next != None:
            print "Next: "+ top_url + next.get('href')
            next_url = top_url + next.get('href')
        else:
            next_url = False

    out_file.close()
get_links(top_url+"/all")
