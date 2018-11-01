# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:19:05 2018

@author: Navya
"""
import io
import nltk
#nltk.download() 
#nltk.setdefaultencoding("utf-8")
def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})
 
print(format_sentence("The cat is very cute"))
pos = []
with io.open("C:/Users/Navya/Desktop/AIT580 - Analytics-Big data to information/Assignment 9/pos_tweets.txt", "r") as f:
    for i in f: 
        pos.append([format_sentence(i), 'pos'])
 
neg = []
with io.open("C:/Users/Navya/Desktop/AIT580 - Analytics-Big data to information/Assignment 9/neg_tweets.txt", "r", encoding="utf-8") as f:
    for i in f: 
        neg.append([format_sentence(i), 'neg'])
 
#next, split labeled data into the training and test data
training = pos[:int((.8)*len(pos))] + neg[:int((.8)*len(neg))]
test = pos[int((.8)*len(pos)):] + neg[int((.8)*len(neg)):]
from nltk.classify import NaiveBayesClassifier
 
classifier = NaiveBayesClassifier.train(training)
classifier.show_most_informative_features()
example1 = "Cats are awesome!"
print(classifier.classify(format_sentence(example1)))

example2 = "I don’t like cats."
print(classifier.classify(format_sentence(example2)))

example3 = "I have no headache!"
print(classifier.classify(format_sentence(example3)))

example4 = "Twilio is an awesome company!"
print(classifier.classify(format_sentence(example4)))

example5 = "I'm sad that Twilio doesn't have even more blog posts!"
print(classifier.classify(format_sentence(example5)))
#%%Positive tweets
example6 = "Amazing—after years of attacking Donald Trump the media managedto turn #InaugurationDay into all about themselves.#MakeAme…"
print(classifier.classify(format_sentence(example6)))

example7 = "CNN Declines to Air White House Press Conference Live YES! THANK YOU @CNN FOR NOT LEGITIMI…"
print(classifier.classify(format_sentence(example7)))

example8 = "Donald J. Trump's speech sounded eerily familiar...POTUS plans new deal for UK as Theresa May to be first foreign leader to meet new president since inauguration "
print(classifier.classify(format_sentence(example8)))

example9 = "#Syria #Mexico #Russia & now #Afghanistan. Another #DearDonaldTrump Letter worth a read @AJEnglish"
print(classifier.classify(format_sentence(example9)))

example10 = "Donald Trump’s administration: “Government by the worst men.” "
print(classifier.classify(format_sentence(example10)))

example11 = "Trump, Sean Spicer, et al. lie for a reason. Their lies are not just lies. Their lies are authoritarian propaganda."
print(classifier.classify(format_sentence(example11)))

example12 = "Me: I hate corn Donald Trump: I hate corn too Me: https://t.co/GPgy8R8HB5 It's ridiculous that people are more annoyed at this than Donald Trump's sexism."
print(classifier.classify(format_sentence(example12)))

example13 = "Chris Wallace on Fox news right now talking crap about Donald Trump news conference it seems he can't face the truth eithe…"
print(classifier.classify(format_sentence(example13)))

example14 = "With False Claims, Donald Trump Attacks Media on Crowd Turnout Aziz Ansari Just Hit Donald Trump Hard In An Epic Saturday NIght Live Monologue"
print(classifier.classify(format_sentence(example14)))

example15 = "I’ve got a mortgage!! happyyyyyy"
print(classifier.classify(format_sentence(example15)))

example16 = "OLD SCHOOL PILLARS ARE REPLACED BY ALUMNI"
print(classifier.classify(format_sentence(example16)))

example17 = "HOSPITALS ARE SUED BY 7 FOOT DOCTORS"
print(classifier.classify(format_sentence(example17)))

example18 = "MAN EATING PIRANHA MISTAKENLY SOLD AS PET FISH"
print(classifier.classify(format_sentence(example18)))

example19 = "DRUNK GETS NINE MONTHS IN VIOLIN CASE"
print(classifier.classify(format_sentence(example19)))

example20 = "SAFETY EXPERTS SAY SCHOOL BUS PASSENGERS SHOULD BE BELTED"
print(classifier.classify(format_sentence(example20)))

example21 = "ASTRONAUT TAKES BLAME FOR GAS IN SPACECRAFT"
print(classifier.classify(format_sentence(example21)))

from nltk.classify.util import accuracy
print(accuracy(classifier, test))