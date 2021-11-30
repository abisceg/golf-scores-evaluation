from ghin_login_defs import *
from ghin_data_defs import *
from ghin_plots_defs import *

ghins       = [ENTER_GHIN_HERE]
datestart  = "2021-01-01"
dateend    = "2021-11-15"

# Get a bearer token for all api calls to follow
token = ghinLogin()

# create figure here
fig, ax = plt.subplots()

ghinapi = GhinApi(token)
for ghin in ghins:
  lname, fname = ghinapi.ghin2lname(ghin)
  dates, scores = ghinapi.scores(ghin, datestart, dateend)
  plotScores(scores,dates,lname,fig,ax)

plt.show()
