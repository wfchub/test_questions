import requests
import json
import pandas as pd


cookie = {

	"Cookie": '''apache=bbfde8c184f3e1c6074ffab28a313c87; _ulta_id.ECM-Prod.ccc4=b0ee9b0321c5853c; _ulta_ses.ECM-Prod.ccc4=f31ae5ae758eca16; lss=fd9e664ef34511dcdc4a51a4e8d84abc; isLogin=0; _ulta_id.CM-Prod.ccc4=72ab069f7330bbea; _ulta_ses.CM-Prod.ccc4=e9d0f005beaed3b2; AlteonP10=BttdHyw/F6zWQN4SivoGQA$$''',

}

url = "https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"


def parse_data(html):
	for data in html["data"]["resultList"]:
		ls = {
			"ISIN": data["isin"],
			"Bond Code": data["bondCode"],
			"Issuer": data["entyFullName"],
			"Bond Type": data["bondType"],
			"Issue Date": data["issueStartDate"],
			"Latest Rating": data["debtRtng"]
		}
		result_list.append(ls)


if __name__ == "__main__":
	k_d = {
		"pageNo": 1,
		"pageSize": 15,
		"bondType": 100001,
		"issueYear": 2023
	}
	result_list = []

	for i in range(4):
		k_d["pageNo"]=i+1
		response = requests.post(url, cookies=cookie, data=k_d)

		json_html = json.loads(response.text)
		parse_data(json_html)
	df = pd.DataFrame(result_list)
	df.to_csv('data.csv', index=False)
	print("输出完成")




