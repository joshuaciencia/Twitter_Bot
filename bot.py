#!/usr/bin/env python

import tweepy
import logging
from config import create_api
import time

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
    api.update_with_media("memes/meme_00.jpg")
    while False:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == '__main__':
    main()
