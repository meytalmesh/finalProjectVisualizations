import json
import DB

dictionary= {
    "sentences": [
        {"sentenceNum": 1, "content": """While complaints about the 'miserly' generosity of the Bush Administration have surfaced in recent days, donations and actions at the grassroots level have quietly illustrated the concern and sympathy felt by ordinary Americans.
""", "wight": 0.5},
        {"sentenceNum": 2, "content": """On Monday of this week, Jan Egeland, the UN's chief of emergency relief said that rich nations like the U.S. were being "stingy" by making small contributions. Egeland later recanted his statement, adding that America's contributions to Asia's tsunami relief was "one of the most generous pledges so far."
""", "wight": 0.26},
        {"sentenceNum": 3, "content": """The Bush administration has pledged $350 million in aid for the relief effort. Critics have been quick to compare this to the $177 million spent every day in Iraq to conduct war in that country. In comparison, there was a $500 million pledge made recently by the government of Japan.
""", "wight": 0.9},
        {"sentenceNum": 4, "content": """Independently of the government, individual Americans have been directly contributing money to aid organizations. Amazon.com placed a link for the American Red Cross, collecting more than $8 million from 100,000 people as of Friday, December 31st. 12,000 donors have donated over $1.2 million to the Red Cross through Yahoo.com.
""", "wight": 0.35},
        {"sentenceNum": 5, "content": """Scores of International aid organizations are accepting donations for helping victims of the earthquake and tsunami. Many major companies including Apple Computer, Microsoft, Cisco, eBay, Google, and AOL are helping enable donations through the web.""", "wight": 0.8},
    ]
}

def addJsonToDB():
    DB.insert_text(1, json.dumps(dictionary))

def convertToText(jsonText):
    temp = json.loads(jsonText[0][0])
    return temp.get('sentences')


