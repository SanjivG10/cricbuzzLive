page_id= "140518209928971"
access_token= "EAAZAMZCSZBejv0BABsaPsKmC9Mw5NaUUcxbdwZByRThE6GXfMx75VZAlOKJENOkvEJiWOGSuZA1fzwuXVdMrNWvxMxSsrKL86d5B5RZBEK6Y5TV3BaqNsqyxIiBDFvFlU4cHpHsglZASUWaVBun9ThP5fvobleaVNEbJFWuN6MyTGjd9WFGuNfspXbMWQ2S15bBjCfwZCLYdIGpIc1p5OcZCz6jy1c1BzoTREZD"
import facebook

def main():
	cfg={
	"page_id": page_id,
	"access_token": access_token
	}

	api = get_cpi(cfg)
	msg="Nepal vs UAE Live. Like for More"
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