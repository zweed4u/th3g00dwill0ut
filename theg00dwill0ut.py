import requests,urllib2,time
from BeautifulSoup import BeautifulSoup

session=requests.Session()

headers = {
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36'
}

session.cookies.clear()

#Get formkey
prelimResp=session.get('https://www.thegoodwillout.com/adidas-topanga-hemp-hemp-gum3-s75503',headers=headers)
soup=BeautifulSoup(prelimResp.content)
formkey=str(soup.findAll('div',{'class':'product-view'})).split('form_key/')[1].split('/')[0]
print 'FormKey: '+formkey


start=raw_input('start? ')
end=raw_input('end? ')
#Start scrape
for counter in range(int(start),int(end)):
	reqUrl='https://www.thegoodwillout.com/checkout/cart/add/uenc/a,/product/'+str(counter)+'/form_key/'+str(formkey)+'/'
	resp=session.post(reqUrl,headers=headers)
	try:
		print str(counter)+' :: '+resp.content.split('<li class="success-msg"><ul><li><span>')[1].split('</span>')[0]+'\n'
	except:
		print str(counter)+' :: '+resp.url+'\n'
