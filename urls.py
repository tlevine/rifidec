#!/usr/bin/env python

from copy import copy

from urllib2 import urlopen
from lxml.html import fromstring
from demjson import decode

URLS={
  "base":"http://www.rifidec.org/membres/"
}

def main():
  regions=[]
  region_id=0
  for url in region_urls():
    region_id=region_id+1
    xml=get(URLS['base']+url['href'])
    links=get_links(
      xml
    , '//table/tr/td/a'
    , textkey="organization"
    , extra={"region_id":region_id}
    )
    regions.append({
      "region_id":region_id
    , "region":url['region']
    })
    print regions

def get(url):
  raw=urlopen(url).read()
  return fromstring(raw)

def region_urls():
  xml=get('http://www.rifidec.org/membres/infomembres.htm')
  return get_links(xml,'//a',textkey="region")[:-1]

def get_links(xml,xpath,textkey="text",extra={}):
  links=[]
  for a in xml.xpath(xpath):
    if a.text!=None:
      row=copy(extra)
      row[textkey]=a.text
      row["href"]=a.attrib['href']
      links.append(row)
  return links

if __name__ == '__main__':
  main()
