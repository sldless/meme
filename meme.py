import random, logging
from psaw import PushshiftAPI
api = PushshiftAPI()

subreddits = ['memes', 'MemeEconomy', 'sfwmemes']

logging.basicConfig(filename='logger.log', level=logging.DEBUG)
def gen():
  results = list(api.search_submissions(
    subreddit=random.choice(subreddits),
    filter=['url','author', 'title', 'subreddit'],
    limit=1900))


  try:
    thing = results[random.randint(1, len(results))]
  except Exception:
    thing = results[random.randint(1, len(results))]
  return thing