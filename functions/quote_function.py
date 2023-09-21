def quote_function(event, context):
  print("Quote function invoked!!")
  return {
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": "{\"message\":\"Hello, world!\"}"
  }