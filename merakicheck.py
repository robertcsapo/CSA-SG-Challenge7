import meraki
from webexteamssdk import WebexTeamsAPI


''' Settings '''
meraki_api_key = '093b24e85df15a3e66f1fc359f4c48493eaa1b73'
mynetwork = 'L_646829496481100388'

msversion = '11.31'
mrversion = '26.6.1'
mxversion = '15.27'
mvversion = '4.0'

WebexRoomID = 'Y2lzY29zcGFyazovL3VzL1JPT00vNWJiMmRiZjAtNmFkOC0xMWVhLWEzNmEtMDc0ZjMxN2Y0Njli'
WebexAccessToken = ''

report_file = 'report.txt'


''' Cisco Meraki API request '''
try:
    meraki = meraki.DashboardAPI(meraki_api_key, suppress_logging=True)
except Exception as e_api:
    raise Exception('Issues with Cisco Meraki API - {}'.format(e_api))
''' Cisco Meraki API request '''
''' /networks/{mynetwork}/devices '''
try:
    devices = meraki.devices.getNetworkDevices(mynetwork)
except Exception as e_api:
    raise Exception('Issues with Cisco Meraki API - {}'.format(e_api))


''' Fix formating to match Cisco Meraki API '''


def version_format(model, version):
    version = version.replace('.', '-')
    version = model+'-'+version
    return str(version)


''' Create a dict and lists for model types '''


def device_list():
    result = {}
    result['ms'] = []
    result['mr'] = []
    result['mx'] = []
    result['mv'] = []
    result['non-compliant'] = []
    return result


result = device_list()


''' Loop through the API response of /networks/{mynetwork}/devices '''
for device in devices:
    if version_format('switch', msversion) in device['firmware']:
        result['ms'].append(device)
    elif version_format('wireless', mrversion) in device['firmware']:
        result['mr'].append(device)
    elif version_format('wired', mxversion) in device['firmware']:
        result['mx'].append(device)
    elif version_format('camera', mvversion) in device['firmware']:
        result['mv'].append(device)
    else:
        ''' Store all devices that doesn't match versions '''
        result['non-compliant'].append(device)

''' Create a local file with the report '''
f = open(report_file, "w+")
print('Total switches that meet standard: {}'.format(
    len(result['ms'])),
      file=f)
print('Total APs that meet standard: {}'.format(
    len(result['mr'])),
      file=f)
print('Total Security Appliances that meet standard: {}'.format(
    len(result['mx'])),
      file=f)
print('Total Cameras that meet standard: {}'.format(
    len(result['mv'])),
      file=f)
print('Devices that will need to be manually checked:', file=f)
for non_complaint_device in result['non-compliant']:
    print('Serial#: {}, Model#: {}'.format(
        non_complaint_device['serial'],
        non_complaint_device['model']),
          file=f)

''' Print the local file report '''
f.seek(0)
print(f.read())
f.close()

''' Extra credit / Bonus '''

''' Cisco Webex API request '''
try:
    webex = WebexTeamsAPI(access_token=WebexAccessToken)
except Exception as e_api:
    raise Exception('Issues with Cisco Webex API - {}'.format(e_api))
''' Message to Cisco Webex Room with report as file '''
try:
    webex.messages.create(
        WebexRoomID,
        text="Report Completed",
        files=[report_file])
except Exception as e_api:
    raise Exception('Issues with Cisco Webex API - {}'.format(e_api))
