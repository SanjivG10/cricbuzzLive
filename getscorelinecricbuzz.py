from bs4 import BeautifulSoup as soup
import urllib

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
	print list_thing[1]
	


html_data =get_data("http://www.cricbuzz.com/live-cricket-scores/19305/mlyu19-vs-nplu19-group-a-acc-u-19-asia-cup-2017")

testing_other = get_data("http://www.cricbuzz.com/live-cricket-scores/19150/pakw-vs-nzw-4th-t20i-pakistan-women-v-new-zealand-women-in-uae-2017")

bagnl = get_data("http://www.cricbuzz.com/live-cricket-scores/19011/comilla-vs-chittagong-14th-match-bangladesh-premier-league-2017")

