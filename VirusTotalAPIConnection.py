import requests
import base64
import json

urlVT = "https://www.virustotal.com/api/v3/urls/"
api_key_path = r"C:\Users\gr_mi\Desktop\AaToSave\Ing en Software\6to semestre\Aplicaciones Móbiles\TareasCode\virustotalkey.txt"


def fetchVirusTotal(url):
  # urlB64 = encodeB64(url)
  request = requests.get(urlVT+url, headers={'accept': 'application/json', 'x-apikey' : f'{readKey(api_key_path)}'})
  response = json.loads(request.text)
  return response

def fetchDev(url):
  request = requests.get(decodeB64(url))
  if request.ok:
    return json.loads({'data': {'id': '6f0e31ea9cb786a83da91f938a94264c82c6e84fbb94b5907b056230098d6431', 'type': 'url', 'links': {'self': 'https://www.virustotal.com/api/v3/urls/6f0e31ea9cb786a83da91f938a94264c82c6e84fbb94b5907b056230098d6431'}, 'attributes': {'url': 'http://facebook.com/', 'total_votes': {'harmless': 625, 'malicious': 586}, 'last_http_response_code': 200, 'last_http_response_headers': {'X-XSS-Protection': '0', 'Vary': 'Accept-Encoding', 'report-to': '{"max_age":2592000,"endpoints":[{"url":"https:\\/\\/www.facebook.com\\/browser_reporting\\/coop\\/?minimize=0"}],"group":"coop_report","include_subdomains":true}, {"max_age":86400,"endpoints":[{"url":"https:\\/\\/www.facebook.com\\/browser_reporting\\/coep\\/?minimize=0"}],"group":"coep_report"}, {"max_age":259200,"endpoints":[{"url":"https:\\/\\/m.facebook.com\\/ajax\\/mtouch_error_reports\\/"}]}', 'X-Frame-Options': 'DENY', 'Expires': 'Sat, 01 Jan 2000 00:00:00 GMT', 'Pragma': 'no-cache', 'Date': 'Tue, 27 Feb 2024 15:01:13 GMT', 'Set-Cookie': 'datr=OfndZRPmBQXiSFXTLItPM4gl; expires=Wed, 02-Apr-2025 15:01:13 GMT; Max-Age=34560000; path=/; domain=.facebook.com; secure; httponly; SameSite=None, sb=OfndZRwARR2FXVo6kFG0IJRD; expires=Wed, 02-Apr-2025 15:01:13 GMT; Max-Age=34560000; path=/; domain=.facebook.com; secure; httponly; SameSite=None', 'Strict-Transport-Security': 'max-age=15552000; preload; includeSubDomains', 'Connection': 'close', 'accept-ch': 'viewport-width,dpr,Sec-CH-Prefers-Color-Scheme,Sec-CH-UA-Full-Version-List,Sec-CH-UA-Platform-Version,Sec-CH-UA-Model', 'cross-origin-embedder-policy-report-only': 'require-corp;report-to="coep_report"', 'accept-ch-lifetime': '4838400', 'content-security-policy': "default-src data: blob: 'self' https://*.fbsbx.com 'unsafe-inline' *.facebook.com *.fbcdn.net 'unsafe-eval';script-src *.facebook.com *.fbcdn.net *.facebook.net *.google-analytics.com *.google.com 127.0.0.1:* 'unsafe-inline' blob: data: 'self' connect.facebook.net 'unsafe-eval';style-src fonts.googleapis.com *.fbcdn.net data: *.facebook.com 'unsafe-inline';connect-src *.facebook.com facebook.com *.fbcdn.net *.facebook.net wss://*.facebook.com:* wss://*.whatsapp.com:* wss://*.fbcdn.net attachment.fbsbx.com ws://localhost:* blob: *.cdninstagram.com 'self' http://localhost:3103 wss://gateway.facebook.com wss://edge-chat.facebook.com wss://snaptu-d.facebook.com wss://kaios-d.facebook.com/ v.whatsapp.net *.fbsbx.com *.fb.com;font-src data: *.gstatic.com *.facebook.com *.fbcdn.net *.fbsbx.com;img-src *.fbcdn.net *.facebook.com data: https://*.fbsbx.com facebook.com *.cdninstagram.com fbsbx.com fbcdn.net connect.facebook.net *.carriersignal.info blob: android-webview-video-poster: googleads.g.doubleclick.net www.googleadservices.com *.whatsapp.net *.fb.com *.oculuscdn.com *.tenor.co *.tenor.com *.giphy.com;media-src *.cdninstagram.com blob: *.fbcdn.net *.fbsbx.com www.facebook.com *.facebook.com data: *.tenor.co *.tenor.com https://*.giphy.com;frame-src *.doubleclick.net *.google.com *.facebook.com www.googleadservices.com *.fbsbx.com fbsbx.com data: www.instagram.com *.fbcdn.net https://paywithmybank.com/ https://sandbox.paywithmybank.com/;worker-src blob: *.facebook.com data:;", 'X-Content-Type-Options': 'nosniff', 'Content-Encoding': 'br', 'reporting-endpoints': 'coop_report="https://www.facebook.com/browser_reporting/coop/?minimize=0", coep_report="https://www.facebook.com/browser_reporting/coep/?minimize=0", default="https://m.facebook.com/ajax/mtouch_error_reports/"', 'x-stack': 'www', 'Cache-Control': 'private, no-cache, no-store, must-revalidate', 'Alt-Svc': 'h3=":443"; ma=86400', 'Content-Type': 'text/html; charset=utf-8', 'X-FB-Debug': 'M1QSXC7NAPheHhwbpfiF7LWLVfCzaaOFVpds4281/G91czLzHo4Gy+4ua+DwLH+bbdB6d8yp+Xs3SNydWlY7tg==', 'cross-origin-opener-policy': 'same-origin-allow-popups;report-to="coop_report"'}, 'last_analysis_results': {'Bkav': {'method': 'blacklist', 'engine_name': 'Bkav', 'category': 'undetected', 'result': 'unrated'}, 'CMC Threat Intelligence': {'method': 'blacklist', 'engine_name': 'CMC Threat Intelligence', 'category': 'harmless', 'result': 'clean'}, '0xSI_f33d': {'method': 'blacklist', 'engine_name': '0xSI_f33d', 'category': 'undetected', 'result': 'unrated'}, 'ViriBack': {'method': 'blacklist', 'engine_name': 'ViriBack', 'category': 'harmless', 'result': 'clean'}, 'MalwareURL': {'method': 'blacklist', 'engine_name': 'MalwareURL', 'category': 'undetected', 'result': 'unrated'}, 'PhishLabs': {'method': 'blacklist', 'engine_name': 'PhishLabs', 'category': 'undetected', 'result': 'unrated'}, 'K7AntiVirus': {'method': 'blacklist', 'engine_name': 'K7AntiVirus', 'category': 'harmless', 'result': 'clean'}, 'CINS Army': {'method': 'blacklist', 'engine_name': 'CINS Army', 'category': 'harmless', 'result': 'clean'}, 'Quttera': {'method': 'blacklist', 'engine_name': 'Quttera', 'category': 'harmless', 'result': 'clean'}, 'BlockList': {'method': 'blacklist', 'engine_name': 'BlockList', 'category': 'harmless', 'result': 'clean'}, 'PrecisionSec': {'method': 'blacklist', 'engine_name': 'PrecisionSec', 'category': 'undetected', 'result': 'unrated'}, 'OpenPhish': {'method': 'blacklist', 'engine_name': 'OpenPhish', 'category': 'harmless', 'result': 'clean'}, 'VX Vault': {'method': 'blacklist', 'engine_name': 'VX Vault', 'category': 'harmless', 'result': 'clean'}, 'Feodo Tracker': {'method': 'blacklist', 'engine_name': 'Feodo Tracker', 'category': 'harmless', 'result': 'clean'}, 'ADMINUSLabs': {'method': 'blacklist', 'engine_name': 'ADMINUSLabs', 'category': 'harmless', 'result': 'clean'}, 'Scantitan': {'method': 'blacklist', 'engine_name': 'Scantitan', 'category': 'harmless', 'result': 'clean'}, 'AlienVault': {'method': 'blacklist', 'engine_name': 'AlienVault', 'category': 'harmless', 'result': 'clean'}, 'Sophos': {'method': 'blacklist', 'engine_name': 'Sophos', 'category': 'harmless', 'result': 'clean'}, 'Phishtank': {'method': 'blacklist', 'engine_name': 'Phishtank', 'category': 'harmless', 'result': 'clean'}, 'ESTsecurity': {'method': 'blacklist', 'engine_name': 'ESTsecurity', 'category': 'harmless', 'result': 'clean'}, 'Spam404': {'method': 'blacklist', 'engine_name': 'Spam404', 'category': 'harmless', 'result': 'clean'}, 'CRDF': {'method': 'blacklist', 'engine_name': 'CRDF', 'category': 'harmless', 'result': 'clean'}, 'Rising': {'method': 'blacklist', 'engine_name': 'Rising', 'category': 'harmless', 'result': 'clean'}, 'Fortinet': {'method': 'blacklist', 'engine_name': 'Fortinet', 'category': 'harmless', 'result': 'clean'}, 'alphaMountain.ai': {'method': 'blacklist', 'engine_name': 'alphaMountain.ai', 'category': 'harmless', 'result': 'clean'}, 'Lionic': {'method': 'blacklist', 'engine_name': 'Lionic', 'category': 'harmless', 'result': 'clean'}, 'Cyble': {'method': 'blacklist', 'engine_name': 'Cyble', 'category': 'harmless', 'result': 'clean'}, 'Seclookup': {'method': 'blacklist', 'engine_name': 'Seclookup', 'category': 'harmless', 'result': 'clean'}, 'Xcitium Verdict Cloud': {'method': 'blacklist', 'engine_name': 'Xcitium Verdict Cloud', 'category': 'undetected', 'result': 'unrated'}, 'Artists Against 419': {'method': 'blacklist', 'engine_name': 'Artists Against 419', 'category': 'harmless', 'result': 'clean'}, 'Google Safebrowsing': {'method': 'blacklist', 'engine_name': 'Google Safebrowsing', 'category': 'harmless', 'result': 'clean'}, 'SafeToOpen': {'method': 'blacklist', 'engine_name': 'SafeToOpen', 'category': 'undetected', 'result': 'unrated'}, 'ArcSight Threat Intelligence': {'method': 'blacklist', 'engine_name': 'ArcSight Threat Intelligence', 'category': 'malicious', 'result': 'malware'}, 'Cyan': {'method': 'blacklist', 'engine_name': 'Cyan', 'category': 'undetected', 'result': 'unrated'}, 'Juniper Networks': {'method': 'blacklist', 'engine_name': 'Juniper Networks', 'category': 'harmless', 'result': 'clean'}, 'Heimdal Security': {'method': 'blacklist', 'engine_name': 'Heimdal Security', 'category': 'harmless', 'result': 'clean'}, 'AutoShun': {'method': 'blacklist', 'engine_name': 'AutoShun', 'category': 'undetected', 'result': 'unrated'}, 'Trustwave': {'method': 'blacklist', 'engine_name': 'Trustwave', 'category': 'harmless', 'result': 'clean'}, 'CyRadar': {'method': 'blacklist', 'engine_name': 'CyRadar', 'category': 'harmless', 'result': 'clean'}, 'Dr.Web': {'method': 'blacklist', 'engine_name': 'Dr.Web', 'category': 'harmless', 'result': 'clean'}, 'Emsisoft': {'method': 'blacklist', 'engine_name': 'Emsisoft', 'category': 'harmless', 'result': 'clean'}, 'Abusix': {'method': 'blacklist', 'engine_name': 'Abusix', 'category': 'harmless', 'result': 'clean'}, 'Webroot': {'method': 'blacklist', 'engine_name': 'Webroot', 'category': 'harmless', 'result': 'clean'}, 'Avira': {'method': 'blacklist', 'engine_name': 'Avira', 'category': 'harmless', 'result': 'clean'}, 'Snort IP sample list': {'method': 'blacklist', 'engine_name': 'Snort IP sample list', 'category': 'harmless', 'result': 'clean'}, 'securolytics': {'method': 'blacklist', 'engine_name': 'securolytics', 'category': 'harmless', 'result': 'clean'}, 'Antiy-AVL': {'method': 'blacklist', 'engine_name': 'Antiy-AVL', 'category': 'harmless', 'result': 'clean'}, 'AlphaSOC': {'method': 'blacklist', 'engine_name': 'AlphaSOC', 'category': 'undetected', 'result': 'unrated'}, 'Acronis': {'method': 'blacklist', 'engine_name': 'Acronis', 'category': 'harmless', 'result': 'clean'}, 'Quick Heal': {'method': 'blacklist', 'engine_name': 'Quick Heal', 'category': 'harmless', 'result': 'clean'}, 'URLQuery': {'method': 'blacklist', 'engine_name': 'URLQuery', 'category': 'harmless', 'result': 'clean'}, 'Ermes': {'method': 'blacklist', 'engine_name': 'Ermes', 'category': 'undetected', 'result': 'unrated'}, 'Viettel Threat Intelligence': {'method': 'blacklist', 'engine_name': 'Viettel Threat Intelligence', 'category': 'harmless', 'result': 'clean'}, 'DNS8': {'method': 'blacklist', 'engine_name': 'DNS8', 'category': 'harmless', 'result': 'clean'}, 'AILabs (MONITORAPP)': {'method': 'blacklist', 'engine_name': 'AILabs (MONITORAPP)', 'category': 'harmless', 'result': 'clean'}, 'benkow.cc': {'method': 'blacklist', 'engine_name': 'benkow.cc', 'category': 'harmless', 'result': 'clean'}, 'EmergingThreats': {'method': 'blacklist', 'engine_name': 'EmergingThreats', 'category': 'harmless', 'result': 'clean'}, 'Chong Lua Dao': {'method': 'blacklist', 'engine_name': 'Chong Lua Dao', 'category': 'harmless', 'result': 'clean'}, 'Yandex Safebrowsing': {'method': 'blacklist', 'engine_name': 'Yandex Safebrowsing', 'category': 'harmless', 'result': 'clean'}, 'Lumu': {'method': 'blacklist', 'engine_name': 'Lumu', 'category': 'undetected', 'result': 'unrated'}, 'Kaspersky': {'method': 'blacklist', 'engine_name': 'Kaspersky', 'category': 'harmless', 'result': 'clean'}, 'Sucuri SiteCheck': {'method': 'blacklist', 'engine_name': 'Sucuri SiteCheck', 'category': 'harmless', 'result': 'clean'}, 'desenmascara.me': {'method': 'blacklist', 'engine_name': 'desenmascara.me', 'category': 'harmless', 'result': 'clean'}, 'Cluster25': {'method': 'blacklist', 'engine_name': 'Cluster25', 'category': 'undetected', 'result': 'unrated'}, 'SOCRadar': {'method': 'blacklist', 'engine_name': 'SOCRadar', 'category': 'harmless', 'result': 'clean'}, 'URLhaus': {'method': 'blacklist', 'engine_name': 'URLhaus', 'category': 'harmless', 'result': 'clean'}, 'PREBYTES': {'method': 'blacklist', 'engine_name': 'PREBYTES', 'category': 'harmless', 'result': 'clean'}, 'StopForumSpam': {'method': 'blacklist', 'engine_name': 'StopForumSpam', 'category': 'harmless', 'result': 'clean'}, 'Blueliv': {'method': 'blacklist', 'engine_name': 'Blueliv', 'category': 'harmless', 'result': 'clean'}, 'Netcraft': {'method': 'blacklist', 'engine_name': 'Netcraft', 'category': 'undetected', 'result': 'unrated'}, 'ZeroCERT': {'method': 'blacklist', 'engine_name': 'ZeroCERT', 'category': 'harmless', 'result': 'clean'}, 'Phishing Database': {'method': 'blacklist', 'engine_name': 'Phishing Database', 'category': 'harmless', 'result': 'clean'}, 'MalwarePatrol': {'method': 'blacklist', 'engine_name': 'MalwarePatrol', 'category': 'harmless', 'result': 'clean'}, 'Sangfor': {'method': 'blacklist', 'engine_name': 'Sangfor', 'category': 'harmless', 'result': 'clean'}, 'IPsum': {'method': 'blacklist', 'engine_name': 'IPsum', 'category': 'harmless', 'result': 'clean'}, 'Malwared': {'method': 'blacklist', 'engine_name': 'Malwared', 'category': 'harmless', 'result': 'clean'}, 'BitDefender': {'method': 'blacklist', 'engine_name': 'BitDefender', 'category': 'harmless', 'result': 'clean'}, 'GreenSnow': {'method': 'blacklist', 'engine_name': 'GreenSnow', 'category': 'harmless', 'result': 'clean'}, 'G-Data': {'method': 'blacklist', 'engine_name': 'G-Data', 'category': 'harmless', 'result': 'clean'}, 'VIPRE': {'method': 'blacklist', 'engine_name': 'VIPRE', 'category': 'undetected', 'result': 'unrated'}, 'SCUMWARE.org': {'method': 'blacklist', 'engine_name': 'SCUMWARE.org', 'category': 'harmless', 'result': 'clean'}, 'PhishFort': {'method': 'blacklist', 'engine_name': 'PhishFort', 'category': 'undetected', 'result': 'unrated'}, 'malwares.com URL checker': {'method': 'blacklist', 'engine_name': 'malwares.com URL checker', 'category': 'harmless', 'result': 'clean'}, 'Forcepoint ThreatSeeker': {'method': 'blacklist', 'engine_name': 'Forcepoint ThreatSeeker', 'category': 'harmless', 'result': 'clean'}, 'Gridinsoft': {'method': 'blacklist', 'engine_name': 'Gridinsoft', 'category': 'harmless', 'result': 'clean'}, 'Criminal IP': {'method': 'blacklist', 'engine_name': 'Criminal IP', 'category': 'harmless', 'result': 'clean'}, 'Certego': {'method': 'blacklist', 'engine_name': 'Certego', 'category': 'harmless', 'result': 'clean'}, 'ESET': {'method': 'blacklist', 'engine_name': 'ESET', 'category': 'harmless', 'result': 'clean'}, 'Threatsourcing': {'method': 'blacklist', 'engine_name': 'Threatsourcing', 'category': 'harmless', 'result': 'clean'}, 'ThreatHive': {'method': 'blacklist', 'engine_name': 'ThreatHive', 'category': 'harmless', 'result': 'clean'}, 'Bfore.Ai PreCrime': {'method': 'blacklist', 'engine_name': 'Bfore.Ai PreCrime', 'category': 'harmless', 'result': 'clean'}}, 'tags': ['multiple-redirects'], 'last_modification_date': 1709046389, 'last_submission_date': 1709046071, 'last_http_response_content_length': 32882, 'last_analysis_stats': {'malicious': 1, 'suspicious': 0, 'undetected': 16, 'harmless': 74, 'timeout': 0}, 'html_meta': {'referrer': ['origin-when-crossorigin'], 'viewport': ['user-scalable=no,initial-scale=1,maximum-scale=1']}, 'last_analysis_date': 1709046071, 'tld': 'com', 'last_final_url': 'https://www.facebook.com/?_fb_noscript=1', 'times_submitted': 65083, 'reputation': 318, 'redirection_chain': ['http://facebook.com/', 'https://facebook.com/', 'http://facebook.com/', 'https://www.facebook.com/?_fb_noscript=1', 'https://m.facebook.com/?_fb_noscript=1&_rdr'], 'threat_names': [], 'categories': {'Sophos': 'social networks', 'BitDefender': 'socialnetworks', 'Xcitium Verdict Cloud': 'social networking', 'Forcepoint ThreatSeeker': 'social web - facebook', 'Dr.Web': 'social networks'}, 'last_http_response_content_sha256': 'aa02e94e2ece1250382e7be874531a8353f457cdea741a5179749425cc9e9616', 'first_submission_date': 1281446284, 'crowdsourced_context': [{'source': 'ArcSight Threat Intelligence', 'timestamp': 1694380350, 'details': 'Quasar RAT botnet C2 domain (confidence level: 100%)', 'severity': 'medium', 'title': 'ThreatFox IOCs for 2023-09-10'}], 'trackers': {'Doubleclick': [{'url': '', 'timestamp': 1709046071, 'id': ''}]}, 'title': 'You’re Temporarily Blocked'}}})
  else:
    return json.loads({
          'error': {
            'message': 'URL "aHR0cHM6Ly93d3cubm8xMjM4amZqbmZvc25ub2V4aXN0ZS5wcm8v" not found',
            'code': 'NotFoundError'
          }
        })
  
def encodeB64(s):
  encodedS = base64.b64encode(s.encode('ascii'))
  return encodedS.decode('ascii')

def decodeB64(s):
  decodedS = base64.b64decode(s.encode('ascii'))
  return decodedS.decode('ascii')

def readKey(key_txt_path):
  key_file = open(key_txt_path, 'r')
  return key_file.read()


