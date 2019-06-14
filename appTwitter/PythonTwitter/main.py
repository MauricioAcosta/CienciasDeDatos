import twitter
api = twitter.Api(consumer_key='CGMxmM2ubhETj39Q8MVwlC8uJ',
                  consumer_secret='xYswZsui2RTEXHcGmDCZgkkunaezFcjNsu24gPt3FvXXorwzA2',
                  access_token_key='1138117225871814656-j8JK4ak8ahUeOR5Srf81YtNzv8hKXg',
                  access_token_secret='b87o7mB38h7qWczZhVwcUEGRkqjhzP6L3tw07njzzeo8O')

## Tweets that contain the word 'twitter'
results = api.GetSearch(
    raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")
print(results)
