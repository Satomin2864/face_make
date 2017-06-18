from requests_oauthlib import OAuth1Session
import json
import settings
import csv
import urllib.request
import cv2
import numpy as np
import os
twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

# timline上のidを獲得
def get_icon():
    params = {}
    req = twitter.get("https://api.twitter.com/1.1/statuses/home_timeline.json", params = params)

    timeline = json.loads(req.text)

    for i, tweet in enumerate(timeline):
        print(tweet["user"]["screen_name"])
        print(tweet["user"]['profile_image_url_https'])
        url = tweet["user"]['profile_image_url_https']
        url = url.replace("_normal", "")
        urllib.request.urlretrieve(url, "./face_list/face_{}.jpg".format(i))
        print("\n")

def tweet(word):
    # status key に 関連付けた単語をツイート
    params = {"status":word}
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = params)
def follow(sc_name):
    # 指定したアカウントをフォローする
    params = {"screen_name": sc_name}
    twitter.post("https://api.twitter.com/1.1/friendships/create.json", params=params)

def get_timeline():
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params ={'count' : 5}
    req = twitter.get(url, params = params)

    if req.status_code == 200:
        timeline = json.loads(req.text)
        for tweet in timeline:
            print(tweet['user']['name']+'::'+tweet['text'])
            print(tweet['created_at'])
            print('----------------------------------------------------')
    else:
        print("ERROR: %d" % req.status_code)

def search_word():
    url = "https://api.twitter.com/1.1/search/tweets.json"

    print("何を調べますか?")
    keyword = input('>> ')
    print('----------------------------------------------------')


    params = {'q' : keyword, 'count' : 5}

    req = twitter.get(url, params = params)

    if req.status_code == 200:
        search_timeline = json.loads(req.text)
        for tweet in search_timeline['statuses']:
            print(tweet['user']['name'] + '::' + tweet['text'])
            print(tweet['created_at'])
            print('----------------------------------------------------')
    else:
        print("ERROR: %d" % req.status_code)


if __name__ == '__main__':
    get_icon()
    # print("/Users/stmn/python/face_make/face_list")


    file_list=os.listdir("/Users/stmn/python/face_make/face_list")
    count = len(file_list)
    count = count -1
    img_all  = cv2.imread('face_list/face_0.jpg')
    # img_all = cv2.cvtColor(img_all, cv2.COLOR_RGB2GRAY)
    img_all = cv2.resize(img_all, (400,400))
    for file in file_list:
        if file.find("jpg") != -1:
            img = cv2.imread("face_list/" + file)
            # img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            img = cv2.resize(img, (400,400))
            img_all = cv2.addWeighted(img_all,0.7,img,0.3,1/count)
            cv2.imshow("test", img_all)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    cv2.imshow("test", img_all)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
