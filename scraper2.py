import twint
import pandas as pd

def get_user_data(username):
    c = twint.Config()
    c.Username = username
    c.Pandas = True

    twint.run.Lookup(c)
    user_data = twint.storage.panda.User_df

    return user_data

# Specify the usernames of the profiles you want to scrape
usernames = ['BarackObama', 'POTUS', 'Mrwhosetheboss']

# Create an empty list to store the scraped profiles
profiles = []

for username in usernames:
    try:
        user_data = get_user_data(username)

        if not user_data.empty:
            # Extract the desired attributes from the user_data DataFrame
            data = {
                'Username': user_data['username'].values[0],
                'Display Name': user_data['name'].values[0],
                'Followers Count': user_data['followers'].values[0],
                'Following Count': user_data['following'].values[0],
                'Description': user_data['bio'].values[0],
                'Likes Count': user_data['likes'].values[0],
                'User ID': user_data['id'].values[0],
            }

            profiles.append(data)

    except Exception as e:
        # Handle any exceptions that occur during scraping
        print(f"Error retrieving profile for {username}: {e}")

# Convert the scraped profiles to a Pandas DataFrame
df = pd.DataFrame(profiles)

# Print the DataFrame
print(df)
