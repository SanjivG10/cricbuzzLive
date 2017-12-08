from bs4 import BeautifulSoup as soup
import urllib
page_id= "140518209928971"
access_token= "EAAZAMZCSZBejv0BABsaPsKmC9Mw5NaUUcxbdwZByRThE6GXfMx75VZAlOKJENOkvEJiWOGSuZA1fzwuXVdMrNWvxMxSsrKL86d5B5RZBEK6Y5TV3BaqNsqyxIiBDFvFlU4cHpHsglZASUWaVBun9ThP5fvobleaVNEbJFWuN6MyTGjd9WFGuNfspXbMWQ2S15bBjCfwZCLYdIGpIc1p5OcZCz6jy1c1BzoTREZD"
import facebook
#working_url
nep_game="http://www.cricbuzz.com/live-cricket-scores/19294/uae-vs-nep-56th-match-icc-world-cricket-league-championship-2015-17"


def get_data(url):
	downloaded_file= urllib.urlopen(url)
	html_file=downloaded_file.read()
	souped_version = soup(html_file,"html.parser")
	live_score= souped_version.find_all("div",{"class":"cb-col cb-col-67 cb-scrs-wrp"})
	for score in live_score:
		print score.get_text()

	live_commentary = souped_version.find_all("div",{"class":"cb-col cb-col-100"})
	list_thing = []
	for commentary in live_commentary:
		list_thing.append(commentary.get_text())
	return list_thing[1]
	


def main():
	cfg={
	"page_id": page_id,
	"access_token": access_token
	}

	api = get_cpi(cfg)
	msg=get_data(nep_game)
	print msg
	status=api.put_wall_post(msg)

def get_cpi(cfg):
	graph= facebook.GraphAPI(cfg['access_token'])
	resp = graph.get_object('me/accounts')
	page_access_token= None
	for page in resp['data']:
		if page['id'] == cfg['page_id']:
			page_access_token = page['access_token']
		graph=facebook.GraphAPI(page_access_token)
		return graph

if __name__ == "__main__":
	main()