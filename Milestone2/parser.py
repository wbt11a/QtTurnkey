import urllib
import urllib2
from bs4 import BeautifulSoup

top_url = "http://www.turnkeylinux.org"

out_file = open("appliances.txt","w")

doc = BeautifulSoup(firstpage)
def get_links(url):
    next = ""
    next_url = url
    links =[]
    while next_url:
        resp = urllib2.urlopen(next_url)
        firstpage = resp.read()
        for link in doc.find_all('a'):
            #print link.get('class')
            classes = link.get('class')
            if classes != None:
                for c in classes:
                    if c == "title":
                        r = urllib2.urlopen(top_url+link.get('href'))
                        page = r.read()
                        d = BeautifulSoup(page)
                        ovf_string = d.find(text="OVF")
                        if ovf_string:
                            a_tag = ovf_string.find_parent('a')
                            if a_tag:
                                r2 = urllib2.urlopen(top_url+a_tag.get('href'))
                                last_page = r2.read()
                                d_last = BeautifulSoup(last_page)
                                direct_link_str = d_last.find(text="direct link")
                                if direct_link_str:
                                   out_file.write(link.get_text().split("-")[0] + " : " +direct_link_str.find_parent('a').get('href'))
                                   out_file.flush()
            if "next" in link.get_text():
                next = top_url+link.get('href')
            if next != "":
                next_url = next
    
    
    
    out_file.close()
get_links(top_url+"/all")
    




