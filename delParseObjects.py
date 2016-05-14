'''
Python Script to automate task of
Deleting all the Objects

@author Emad Ehsan
'''

import httplib
import json

# Insert addresses & credentials here
address = '<IP:PORT>'
parseUrl = '/parse/classes/<ClassName>'
parseAppId = '<APP_ID>'

headers = {'X-Parse-Application-Id': parseAppId}

objs = {}

'''
Single Request to Parse returns around 100 objects
'''
def getObjs():
	global objs

	conn = httplib.HTTPConnection(address)
	conn.request('GET', parseUrl, None, headers)
	resp = conn.getresponse()
	jsonData = resp.read()

	pyData = json.loads(jsonData)
	objs = pyData["results"]

	if (len(objs) > 0):
		return True
	return False

'''
Delete all objects received in a single request
'''
def delMultipleObjs():
	# Now make delete request seperate for each object
	for c in objs:
		conn2 = httplib.HTTPConnection(address)
		url = parseUrl + '/' + c["objectId"]
		conn2.request('DELETE', url, None, headers)
		resp2 = conn2.getresponse()

		print 'Del: ' + c["objectId"] + ', resp: ' + resp2.read()


def delAll():

	i = 1

	while getObjs():
		print str(i) + 'th GET'
		delMultipleObjs()
		i += 1

	print 'Done!'

if __name__ == '__main__':
	delAll()