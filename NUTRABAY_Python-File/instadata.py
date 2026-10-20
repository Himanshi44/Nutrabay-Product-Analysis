import instaloader
import pandas as pd

# Step 1: Create an instaloader object
L = instaloader.Instaloader()

# Step 2: Load profile (change 'nutrabay' to your target)
profile = instaloader.Profile.from_username(L.context, 'nutrabay')

# Step 3: Show some basic info
print("Username:", profile.username)
print("Followers:", profile.followers)
print("Following:", profile.followees)
print("Posts:", profile.mediacount)

# Step 4: Loop through recent posts and store data
posts_data = []

for post in profile.get_posts():
    posts_data.append({
        'Date': post.date.strftime('%Y-%m-%d'),
        'Caption': post.caption[:100] if post.caption else "",
        'Likes': post.likes,
        'Comments': post.comments,
        'Post URL': f"https://www.instagram.com/p/{post.shortcode}/"
    })
    
    if len(posts_data) >= 50:  # Limit to 50 recent posts
        break
    
