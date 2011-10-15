#!/usr/bin/env python

from urllib2 import urlopen
from lxml.html import fromstring
from demjson import decode

def main():
  raw=urlopen('http://www.rifidec.org/membres/kinshasa.htm').read()
  xml=fromstring(raw)
  links=get_links(xml)
  return links

def get_links(xml):
  links=[]
  for a in xml.xpath('//table/tr/td/a'):
    if a.text!=None:
      links.append({
        "organization":a.text
      , "href":a.attrib['href']
      })
  return links

if __name__ == '__main__':
  main()
