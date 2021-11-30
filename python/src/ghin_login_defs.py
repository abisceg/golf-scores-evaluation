import requests
import json
import os
import getpass as gp


def ghinLogin (debug=False):
  # HTTP Login
  print("Welcome to GHIN.com, Please login: ")
  # Parameters need to to login and receive Bearer Token (golfer_token).
  os.environ['GHIN_API_USER'] = input("Ghin Number: ")
  os.environ['GHIN_API_PW'] = gp.getpass("Ghin Password: ")
  # Still not sure how/when/where this is generated.
  # use web developer to grab token when logging in, listed in Request Header
  #os.environ['GHIN_TOKEN'] = 
  # path to token and store it
  pathtotoken = './token.txt'
  with open(pathtotoken, 'r') as file:
    os.environ['GHIN_TOKEN'] = file.read().rstrip()
  # Print for Debugging
  if debug == True:
    print(os.getenv('GHIN_API_USER'))
    print(os.getenv('GHIN_API_PW'))
    print(os.getenv('GHIN_TOKEN'))

  # Login url
  url = "https://api2.ghin.com/api/v1/golfer_login.json"
  # User login information
  # user double curlers to avoid keyError with format command
  payload = "{{\"user\":{{\"password\":\"{}\",\"email_or_ghin\":\"{}\",\"remember_me\":false}},\"token\":\"{}\",\"source\":\"GHINcom\"}}".format(os.getenv('GHIN_API_PW'),os.getenv('GHIN_API_USER'),os.getenv('GHIN_TOKEN'))
  # Headers
  headers = {
    'Content-Type': 'application/json',
    # also get from web developer when logging, in sorry not sure how to automate
    'Cookie': 'GHIN2020_api2_production=1GYRq4pmYU5q%2BoqsZmDFq6KxMMYNVer8ooTFih7FyjgI5y%2F3ITa7Ma4wJBbOYlhdoN2xkvSbTdBrTeWy5A%3D%3D--Ri9VBquMmxMVXLQ2--L7GVlNoWulBu4TB9vc9ilQ%3D%3D'
  }
  # Make request call
  response = requests.request("POST", url, headers = headers, data = payload)

  # Process HTTP Login Response 
  if response.status_code == 200:
    # print full response for debugging
    #print(response.text.encode('utf8'))

    # load json response data
    alldata = json.loads(response.text)

    # index to golfer_user
    golferuserdata = alldata['golfer_user']

    # store off bearer token
    golfer_token = golferuserdata['golfer_user_token']
    print("Your Token: \n" + golfer_token)

    # Extra not needed, just examples
    golferdata_list = golferuserdata['golfers']
    golferdata = golferdata_list[0]

    msg = "\
  Golfer:	{}\n\
  Club:		{}\n\
  Handicap:	{}\
        "\
    .format(golferdata['player_name'], golferdata['club_name'], golferdata['display'])

    print(msg)
    print("SUCCESS")
    return(golfer_token)

  else:
    errmsg = "\nHTTP ERROR: {}".format(response.status_code)
    print(errmsg)
    exit() 
