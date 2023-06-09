import tweepy
import pandas as pd

# Set up your Twitter API credentials
consumer_key = '#######'
consumer_secret = '#######'
access_token = '#######-#######'
access_token_secret = '########'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Specify the usernames of the profiles you want to scrape
usernames = ['BarackObama', 'POTUS', 'Mrwhosetheboss']

# Create an empty list to store the scraped profiles
profiles = []

for username in usernames:
    try:
        # Retrieve the user object
        user = api.get_user(screen_name=username)

        # Extract the desired attributes from the user
        data = {
            'Username': user.screen_name,
            'Display Name': user.name,
            'Followers Count': user.followers_count,
            'Following Count': user.friends_count,
            'Description': user.description,
            'Likes Count': user.favourites_count,
            'User ID': user.id,
        }

        profiles.append(data)

    except Exception as e:
        # Handle exceptions if the user does not exist or other API errors occur
        print(f"Error retrieving profile for {username}: {e}")

# Convert the scraped profiles to a Pandas DataFrame
df = pd.DataFrame(profiles)

# Print the DataFrame
print(df)
