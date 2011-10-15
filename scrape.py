#!/usr/bin/env python

import urls

def main():
  regions,orgs=urls.urls()

  for org in orgs:
    xml=urls.get(urls.URLS['base']+org['href'])
    dig(xml)

def dig(xml):
  """Dig for data"""

def test_one_url():
  xml=urls.get('http://www.rifidec.org/membres/kin_mec_bosangani.htm')
  print dig(xml)

if __name__ == '__main__':
#  main()
  test_one_url()
