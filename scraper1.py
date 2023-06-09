import snscrape.modules.twitter as sntwitter
import pandas as pd

# Specify the number of profiles to scrape
num_profiles = 10

# Specify the usernames of the profiles you want to scrape
usernames = ['BarackObama', 'POTUS', 'Mrwhosetheboss']

# Create an empty list to store the scraped profiles
profiles = []

for username in usernames:
    # Use snscrape's get_user() function to fetch the user
    user = sntwitter.get_user(username)
    
    # Extract the desired attributes from the user
    data = {
        'Username': user.username,
        'Display Name': user.displayname,
        'Followers Count': user.followers,
        'Following Count': user.following,
        'Description': user.description,
        'Likes Count': user.likes,
        'User ID': user.id,
    }
    
    profiles.append(data)

    # Stop scraping if the desired number of profiles is reached
    if len(profiles) >= num_profiles:
        break

# Convert the scraped profiles to a Pandas DataFrame
df = pd.DataFrame(profiles)

# Print the DataFrame
print(df)
