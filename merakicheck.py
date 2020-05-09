from webexteamssdk import WebexTeamsAPI
import requests
meraki_api_key = '093b24e85df15a3e66f1fc359f4c48493eaa1b73'
mynetwork = 'L_646829496481100388'

msversion = '11.31'
mrversion = '26.6.1'
mxversion = '15.27'
mvversion = '4.0'
WebexRoomID = "Y2lzY29zcGFyazovL3VzL1JPT00vNWJiMmRiZjAtNmFkOC0xMWVhLWEzNmEtMDc0ZjMxN2Y0Njli"
myWebexToken = "" #you will need to put your personal token here

baseurl = "https://dashboard.meraki.com/api/v0/networks/"

payload = {}
headers = {} #you will need to look to the meraki_api_key

url = baseurl  #finish the url!

response = requests #complete the api call using the requests library

myresponse = response.json()


