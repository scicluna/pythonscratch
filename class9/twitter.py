import re

url = input("URL: ").strip()  # goal, get the end of the url (username)

# my solution before watching him
# if matches := re.search("^.*/?/?.*\.com/(.+)$", url):
#     username = matches.groups()
#     print(username)

# naive solution with .replace()
# username = url.replace("https://twitter.com/", "")
# print(username)

# still naive
# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")

# # re solution
# username = re.sub("^.*(com/)", "", url)
# print(username)

# more specific is better
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([\w_]+)$", url, re.IGNORECASE):
    username = matches.group(1)
    print(f"Username: {username}")
