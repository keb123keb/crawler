#reference from: https://www.youtube.com/watch?v=5yAU52qfYuU
#modify from the above website
#video : Girl's Day-Expectation
#time : 2018/1/20
import requests
import parse
#res = requests.get('https://www.youtube.com/watch?get_video_info?video_id=b57XVkLADaM')
res = requests.get('https://www.youtube.com/watch?v=b57XVkLADaM')
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
#print(res.text.translate(non_bmp_map))
#print(res.text)
import re
m = re.search('"url_encoded_fmt_stream_map":".*?"', res.text)
#print( m.group() )
m1 = parse.parse('{}:{url}', m.group())
m2 = parse.parse('{}url={url},{}', m1['url']) 
#m1 = re.search('[^"]"utl=http.*?"', m.group())
#print(m2['url'])
import json

#jd = json.loads(m1['url'])
from urllib.parse import urlparse
from urllib.parse import parse_qs
#a = urlparse("url="+m2['url'])
#print(a)
#from xml.dom import minidom
#b  = minidom.parse(m2['url'])
#print(b)
#import xmltodict
#c = xmltodict.parse(m1['url'])
#print(c)
a = parse_qs("url="+m2['url'])
print(a)
#print( jd("url_encoded_fmt_stream_map").translate(non_bmp_map) )
#"ppv_remarketing_url":"https:\/\/www.googleadservices.com\/pagead\/conversion\/971134070\/?backend=innertube\u0026cname=1\u0026cver=1_20180117\u0026data=backend%
#"player_response":"{\"playbackTracking\":{},

idx="python"
import shutil
res2 = requests.get(a['url'][0], stream=True)
f = open("%s.mp4"%(idx), 'wb')
shutil.copyfileobj(res2.raw, f)
f.close()

