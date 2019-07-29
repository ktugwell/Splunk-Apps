# ta-splunkrest

Instructions for usage
1) install the TA, make sure you restart Splunk
2) create a token on the endpoint you wish to query. Ensure the token is assigned to a user with sufficient permissions to the REST endpoint (i.e admin)
3) write your query. Example: 

| splunkrest host="https://127.0.0.1:8089" endpoint="/services/apps/local" method="GET" output="json"
token="<PASTE TOKEN HERE>"
  
Supported variables
method = GET|PUT
endpoint = All Splunk REST Endpoints
output = json|xml

Have fun (But be careful, this is very powerful)! 
