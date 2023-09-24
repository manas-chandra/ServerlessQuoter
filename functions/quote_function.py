from quoters import Quote
import json

def quote_function(event, context):
  print("Quote function invoked!!")
  query_params = event['queryStringParameters']

  result = None

  match query_params["category"]:
    case "anime":
      result = Quote.print_anime_quote()
    case "tv-series":
      result = Quote.print_series_quote()
    case "programming":
      result = Quote.print_programming_quote()
    case _:
      result = Quote.print()

  return {
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": json.dumps({result})
  }