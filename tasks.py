import os
import logging
from celery import Celery

backend = os.getenv('CELERY_BACKEND_URL', 'amqp')
celery = Celery('tasks', backend=backend)

@celery.task
def keys_abc(url,article):
    print "ESTIC DINS"
    response = urllib2.urlopen(url)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    l = tree.xpath('//*[@class="temas-fin-cuerpo clear"]/a/text()')
    print l


@celery.task
def keys_elconfidencial(url,article):
    print url
    response = urllib2.urlopen(url)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    l = tree.xpath('//*[@class="news-def-tag-link"]/text()')
    print l

@celery.task
def keys_elperiodico(url,article):
    response = urllib2.urlopen(url)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    l = tree.xpath('//*[@class="comp ep-temas-rel group"]//a/text()')
    print l


@celery.task
def keys_elespanol(url,article):
    response = urllib2.urlopen(url)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    l = tree.xpath('//*[@class="tags"]//a/text()')
    print l