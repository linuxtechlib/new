import  requests
import json
BASE_URL ='http://127.0.0.1:8000/'
ENDPOINT = 'api/'
def get_resource(id):
    #resp = requests.get(BASE_URL+ENDPOINT+id+'/')
    # resp = requests.get('http://127.0.0.1:8000/api/1')
    resp = requests.get(BASE_URL+ENDPOINT+id)
    print(resp.status_code)
    print(resp.content)
    #json_data = resp.json()
    #print(json.dumps(json_data))
    #if resp.status_code in range(200,300):
    if resp.status_code == requests.codes.ok:
        print(resp.json())
    else:
        print("Some thing goes wrong")
id=input('Enter some ID : ')
get_resource(id)


#we will get the all records
def get_all():
    resp = requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())

get_all()














#BASE_URL+ENDPOINT+id+'/'
#http://127.0.0.1:8000/+api+1+'/'


##print(resp.headers.get('Content-Type'))
    #print(resp.json())
# json_data = response.json()
#     print(json.dumps(json_data))



# def get_resource():
#     url = 'http://127.0.0.1:8000/api/1'
#     resp = requests.get(url)
# get_resource()
    # Check if the response is JSON-formatted

    # content_type = resp.headers['Content-Type']
    # if content_type == 'application/json':
    #     json_data = resp.json()
    # else:
    #     json_data = resp.text
    #
    # return json_data
