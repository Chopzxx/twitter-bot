import os
import random
import time
import tweepy

# Get keys from environment variables
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

image_folder = "/opt/render/project/src/images"

while True:
    images = os.listdir(image_folder)
    if not images:
        print("No more images.")
        break

    image = random.choice(images)
    image_path = os.path.join(image_folder, image)

    try:
        api.update_with_media(image_path)
        print(f"Posted: {image}")
        os.remove(image_path)
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(21600)  # Wait 6 hours
