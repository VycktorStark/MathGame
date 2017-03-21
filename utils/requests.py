''' This script is a synthesis of the script of the base sid,
    being an open source created by Tiago danin and you can
    see the complete code accessing: https://github.com/TiagoDanin/SiDBot/blob/master/utils/request.py
	
	Tiago Danin <3
'''
from objectjson import ObjectJSON
import utils, requests

def request_url(url, type=None, params=None, headers=None, auth=None, files=None, setime=None):
	time = 5
	if setime:
		time = setime
	try:
		data = requests.get(url, params=params, headers=headers, auth=auth, files=files, timeout=time)
	except Exception as error:
		print(str(error) + '\nURL: ' + str(url) + '\nRequest-Except')
		return False

	if data.status_code == 200:
		return data
	else:
		print('Error in request! {}\n{}\n\n{}'.format(url, params, data.text) + '\nRequest')
	return False
def request_json(url, params=None, headers=None, auth=None, files=None, setime=None):
	data = request_url(url=url, params=params, headers=headers, auth=auth, files=files, setime=setime)
	if data == False:
		return False, False
	try:
		json_str = data.json()
	except:
		return False, False
	json_obj = ObjectJSON(json_str)
	return json_obj, json_str
