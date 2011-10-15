#!/usr/bin/env python

from urllib2 import urlopen
from lxml.html import fromstring
from demjson import decode

URLS={
  "base":"http://www.rifidec.org/membres/"
}

def main():
  regions={}
  for url in region_urls():
    xml=get(URLS['base']+url['href'])
    links=get_links(xml,'//table/tr/td/a',textkey="organization")
    regions[url['region']]=links
  print regions

def get(url):
  raw=urlopen(url).read()
  return fromstring(raw)

def region_urls():
  xml=get('http://www.rifidec.org/membres/infomembres.htm')
  return get_links(xml,'//a',textkey="region")[:-1]

def get_links(xml,xpath,textkey="text"):
  links=[]
  for a in xml.xpath(xpath):
    if a.text!=None:
      links.append({
        textkey:a.text
      , "href":a.attrib['href']
      })
  return links

if __name__ == '__main__':
  main()
