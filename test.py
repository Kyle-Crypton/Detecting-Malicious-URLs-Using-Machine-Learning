import trainer as tr
import pandas
import main

url = ['http://jd.com', 'http://google.com', 'http://facebook.com', 'http://youtube.com', 'http://yahoo.com', 'http://baidu.com', 'http://wikipedia.org', 'http://qq.com', 'http://208.115.247.197/au/index1.php', 'http://toc.cl/wp-admin/www.sparkasse.de/online-banking.aktualisieren.htm', 'http://paristokyo.biz/trouvay-cauvin.co.uk/includes/AOL/index.php', 'http://fenixexpressgc.com/cooljoe/CLICK/CLICK/index.php.htm', 'http://arbiitours.com/wp-content/plugins/contact-form-777/images/online/login.jsp.html', 'http://ruthdunn.org/paypal.co.uk.c17d1db50d22aa998bed4a8d7855d5fa03/ffd12b054185e4e1b246b1abc08efb1a/cgi-bin/en/account/login/index.php%5B%2A%2Aqmark%2A%2A%5D', 'http://civilwarvetswastate.com/gxy/', 'http://200.98.128.198/testax14/p/itant.html', 'http://musicmoviesnbooks.com/codec.exe', 'http://musicmoviesnbooks.com/codec/197.exe', 'http://musicmoviesnbooks.com/file.exe', 'http://musicmoviesnbooks.com/pcdef.exe', 'http://mybest-adult.com/promo1/get.php', 'http://mybest-adult.com/promo2/get.php', 'http://mybest-adult.com/promo3/get.php']

for testurl in url:
	main.process_test_url(testurl,'test_features.csv')
	return_ans = tr.gui_caller('url_features.csv','test_features.csv')

print return_ans