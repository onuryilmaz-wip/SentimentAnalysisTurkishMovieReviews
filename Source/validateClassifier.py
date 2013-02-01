## Onur Yilmaz
## CENG 463 - Term Project

## File for validating the classifier

## Imports for web crawling
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import urllib2

## Import for nltk and classification
import random
import nltk
from nltk import FreqDist
import yaml 
import itertools

## Import classifier
from Classifier import myClassify 

## Open validation list
f=open('validationList.yaml')
validationList=yaml.load(f)

## Construct gold set
gold = [b for (a,b) in validationList]

## Construct predicted set
predicted = [myClassify(a) for (a,b) in validationList]

## Confusion matrix
cm = nltk.ConfusionMatrix(gold,predicted)
print cm

## Print accuracy
print nltk.accuracy(gold,predicted)

## End of code
