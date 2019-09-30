# -*- coding:utf-8 -*-
import requests, re, time

def get_html(url):
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
	html = requests.get(url, headers=headers, timeout=10).text
	return html

def main(number):
	m = 0
	# 官方网站：http://www.bwlc.net/bulletin/prevslto.html
	uri = r'http://www.bwlc.net/bulletin/prevslto.html?page='
	for n in range(1,number):
		url = '{}{}'.format(uri,n)
		html = get_html(url)

		p = r'<td style="text-align: center;">(.*?) 00:00:00</td>'
		t_date =  re.findall(p, html)

		p = r'<td>(\d\d,\d\d,\d\d,\d\d,\d\d,\d\d)</td>'
		red_ball = re.findall(p, html)

		p = r'<td style="text-align: center;">(\d\d)</td>'
		blue_ball = re.findall(p, html)

		for date, red, blue in zip(t_date, red_ball, blue_ball):
			print('{} {} {}'.format(date,red,blue))
			m = m + 1
		time.sleep(0.1)

	print('共: {} 期数据'.format(m))

if __name__ == '__main__':
	# 6表示150一个页面有30期数据
	main(6)
	input('请按任意键退出...')