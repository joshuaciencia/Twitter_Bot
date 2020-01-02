#!/usr/bin/env python

import tweepy
import logging
from config import create_api
from random import randint
from datetime import datetime
import time
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info("Following {}".format(follower.name))
            follower.follow()

def main():
    api = create_api()
    imgs = os.listdir("memes")
    while True:
        date = datetime.now()
        if not len(imgs):
            logger.info("There aren't any images to tweet.")
            exit(1)
        if date.hour is 5 and date.minute is 30:
                f = "memes/" + imgs[randint(0, len(imgs) - 1)]
                api.update_with_media(f)
                os.remove(f)
                logger.info("Tweeted {}.".format(date.day))
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == '__main__':
    main()
