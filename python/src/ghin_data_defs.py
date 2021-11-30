import json
import requests
import numpy as np
from datetime import datetime

class GhinApi:
  def __init__(self, bearer_token, debug=False):
    self.bearer_token = bearer_token
    self.debug = debug
    self.api_url = "https://api2.ghin.com/api/v1/"
    self.payload = {}
    # bearer string for authorization
    self.bearerstr = "Bearer " + bearer_token
    self.headers = {
      'Authorization': self.bearerstr,
      'Cookie': 'GHIN2020_api2_production=1GYRq4pmYU5q%2BoqsZmDFq6KxMMYNVer8ooTFih7FyjgI5y%2F3ITa7Ma4wJBbOYlhdoN2xkvSbTdBrTeWy5A%3D%3D--Ri9VBquMmxMVXLQ2--L7GVlNoWulBu4TB9vc9ilQ%3D%3D'
    }

  # TODO added club option?
  # contstruct url, make call, parse out dates and scores
  def scores(self, golfer_id, datefrom, dateto):
    # two data collections that get returned
    daysplayed = np.array([])
    scores = np.array([])
    # url constants
    api_page = "scores.json?"
    offset   = 0
    limit    = 1000
    statuses = "Validated"
    source   = "GHINcom"
    # full url construction
    scores_url = "{}{}golfer_id={}&offset={}&limit={}&from_date_played={}&to_date_played={}&statuses={}&source={}"\
      .format(\
        self.api_url,\
        api_page,\
        golfer_id,\
        offset,\
        limit,\
        datefrom,\
        dateto,\
        statuses,\
        source\
      )
   
    if self.debug:
      print(scores_url) 
    # Make request to server
    response = requests.request("GET", scores_url, headers=self.headers, data = self.payload)
    # load response text as json data
    json_data = json.loads(response.text)
    if self.debug:
      print("revision_scores:")
      print(json_data["revision_scores"])
    # index to scores of the dictionary
    myrounds = json_data["scores"]
    # for each posted score collect the played_at (date) and adjusted_gross_score (score)
    for myround in myrounds:
      scores = np.append(scores,int(myround["adjusted_gross_score"]))
      # date played (played_at) as string
      dayplayedat = myround["played_at"]
      # string date to datetime obj
      datetimeobj = datetime.strptime(dayplayedat,'%Y-%m-%d').date()
      # append to numpy array of datetime objects
      daysplayed = np.append(daysplayed,datetimeobj)
    # scores and dates are collected most recent to oldest. Flip them so timeline makes sense
    flip_scores = np.flip(scores)
    flip_days = np.flip(daysplayed)
    # return np arrays of dates and scores
    return flip_days, flip_scores

  # TODO make state a param?
  def ghin2lname(self, golfer_id):
    api_page         = "golfers.json?"
    status           = "Active"
    from_ghin        = "true"
    per_page         = 25
    sorting_criteria = "full_name"
    order            = "asc"
    page             = 1
    state            = "MA"
    source           = "GHINcom"
    # golfer lookup url
    lookup_url = "{}{}status={}&from_ghin={}&per_page={}&sorting_criteria={}&order={}&page={}&state={}&golfer_id={}&source={}"\
      .format(\
        self.api_url,\
        api_page,\
        status,\
        from_ghin,\
        per_page,\
        sorting_criteria,\
        order,\
        page,\
        state,\
        golfer_id,\
        source\
      )

    if self.debug:
      print(lookup_url)
    # Make request to server
    response = requests.request("GET", lookup_url, headers=self.headers, data = self.payload)
    # load response text as json data
    json_data = json.loads(response.text)
    if self.debug:
      print(json_data["golfers"])
    # store found golfer
    golferfoundlist = json_data["golfers"]
    golferfounddict = golferfoundlist[0]
    if self.debug:
      for x in golferfoundlist:
        print(x)
    if self. debug:   
      print(golferfounddict)
      print(golferfounddict["first_name"])
      print(golferfounddict["last_name"])

    # store last name, first name, and return
    lname = golferfounddict["last_name"]
    fname = golferfounddict["first_name"]
    return(lname, fname)























