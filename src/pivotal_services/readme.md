# basic header data
export TOKEN='your Pivotal Tracker API token'
export PROJECT_ID=99

# get all epics
url= /projects/{project_id}/epics

* basic
curl -X GET -H "X-TrackerToken: $TOKEN"
 "https://www.pivotaltracker.com/services/v5/projects/$PROJECT_ID/epics"

* with filter
curl -X GET -H "X-TrackerToken: $TOKEN"
 "https://www.pivotaltracker.com/services/v5/projects/$PROJECT_ID/epics?fields=id%2Ccomments"
## output
### Headers
X-Tracker-Project-Version: 66
Content-Type: application/json; potentially-other-variable-stuff
### Response Body
[
   {
       "id": 555,
       "kind": "epic",
       "created_at": "2019-03-26T12:00:00Z",
       "updated_at": "2019-03-26T12:00:00Z",
       "project_id": 99,
       "name": "Sanitation",
       "url": "http://localhost/epic/show/555",
       "label":
       {
           "id": 2017,
           "project_id": 99,
           "kind": "label",
           "name": "sanitation",
           "created_at": "2019-03-26T12:00:00Z",
           "updated_at": "2019-03-26T12:00:00Z"
       }
   },
   ...]
### PARAMETERS
||param||description||
|project_id int in the request path.| Required  —  The ID of the project.|
|filter extended string in the request query.| —  This parameter supplies a search string; only epics that match the 
search criteria are returned. How can a search be refined?|

# create epic
url = /projects/{project_id}/epics

curl -X POST -H "X-TrackerToken: $TOKEN" -H "Content-Type: application/json" -d '{"name":"Tractor Beams"}' "https://www.pivotaltracker.com/services/v5/projects/$PROJECT_ID/epics"

