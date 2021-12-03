import random, logging
from psaw import PushshiftAPI
api = PushshiftAPI()

subreddits = ['meme', 'MemeEconomy', 'sfwmemes']

logging.basicConfig(filename='logger.log', level=logging.DEBUG)
def gen(limit=100):
  results = list(api.search_submissions(
    subreddit=random.choice(subreddits),
    filter=['url','author', 'title', 'subreddit'],
    limit=400))

  amount = limit / 26
  amount2 = amount / 26
  try:
    thing = results[random.randint(int(amount2),int(amount))]
  except Exception:
    thing = results[random.randint(int(amount),int(amount2))]
  return thing