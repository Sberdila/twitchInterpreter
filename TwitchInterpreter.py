import csv, types
import re
import datetime
from copy import copy, deepcopy

feq_words = {'Kappa': 0,
             '4Head': 0,
             'EleGiggle': 0,
             'PJSalt': 0,
             'ANELE': 0,
             'BabyRage': 0,
             'BibleThump': 0,
             'BlessRNG': 0,
             'BrokeBack': 0,
             'cmonBruh': 0,
             'TriHard': 0,
             'CoolCat': 0,
             'CoolStoryBob': 0,
             'DansGame': 0,
             'DatSheffy': 0,
             'duDudu': 0,
             'FailFish': 0,
             'FrankerZ': 0,
             'HeyGuys': 0,
             'HotPokket': 0,
             'JeBaited': 0,
             'KappaPride': 0,
             'KappaRoss': 0,
             'Keepo': 0,
             'Kreygasm': 0,
             'MingLee': 0,
             'OpieOP': 0,
             'NotLikeThis': 0,
             'PogChamp': 0,
             'ResidentSleeper': 0,
             'SMOrc': 0,
             ':thinking:': 0,
             'SwiftRage': 0,
             'WutFace': 0,
             'LUL': 0}
result = {}
offsets = {}
wagon = {}
wagonHead = 0
wagonTail = 0
nextStep = 0
statsContainer = {}
index = 0
start = 1494558082
end = 1494576486
xArray = [20000]
yAxis = [200]
def processUnit(timestamp):
    global result
    global feq_words
    global index
    wordstring = result[timestamp].split()
    for x in wordstring:
        if x in feq_words:
            feq_words[x] += 1
    statsContainer[timestamp] = deepcopy(feq_words)
    index += 1
    for x in feq_words:
        feq_words[x] = 0


def mssl(l):
    best = cur = 0
    curi = starti = besti = 0
    for ind, i in enumerate(l):
        if cur + i > 0:
            cur += i
        else:  # reset start position
            cur, curi = 0, ind + 1

        if cur > best:
            starti, besti, best = curi, ind + 1, cur
    return starti, besti, best

def buildXArray():
    global xArray
    index = 0
    while index < 20000:
        xArray[index]=index



with open('v141999218.csv', 'rb') as csvfile:
    TwitchReader = csv.reader(open('v141999218.csv'), delimiter='|')
    iteration = 0
    buffer = feq_words
    tolerance = 0
    pattern = re.compile('([^\s\w]|_)+')
    for row in TwitchReader:
        if row:
            key = int(row[0])
            result[key] = pattern.sub('', row[1])
            offsets[key] = row[2]
            print row[2]
    iteration = 0

    processUnit(key)
    iteration += 1

    ofile = open('ttest.csv', "wb")
    writer = csv.writer(ofile, delimiter=',')
    row[0] = "keyword"
    row[1] = "frequency"
    writer.writerow(row)
    for y in feq_words:
        for x in sorted(statsContainer.keys()):
            if statsContainer[x][y] > 0:
                at = int(offsets[x]) / 1000
                at = datetime.datetime.fromtimestamp(
                    int(at)
                ).strftime('%H:%M:%S')
                print "Spike of %s at %s // %d -> %d" % (y,at,int(offsets[x]),statsContainer[x][y])
                row[1]=statsContainer[x][y]
                row[0]=at
                writer.writerow(row)
