#!/usr/bin/env python

import urls

def main():
  regions,orgs=urls.urls()

  for org in orgs:
    xml=urls.get(urls.URLS['base']+org['href'])
    print tostring(xml)

if __name__ == '__main__':
  main()
