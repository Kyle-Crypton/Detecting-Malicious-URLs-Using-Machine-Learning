import csv
import Feature_extraction as urlfeature
import trainer as tr

def resultwriter(feature, output_dest):
	"""docstring for resultwriter"""
	flag = True
	with open(output_dest, 'wb') as f:
		for item in feature:
			w = csv.DictWriter(f, item[1].keys())
			if flag:
				w.writeheader()
				flag = False
			w.writerow(item[1])


def process_URL_list(file_dest, output_dest):
	"""docstring for process_URL_list"""
	feature = []
	with open(file_dest) as file:
		for line in file:
			url = line.split(',')[0].strip()
			malicious_bool = line.split(',')[1].strip()
			if url != '':
				# show off
				print 'working on: ' + url
				ret_dict = urlfeature.feature_extract(url)
				ret_dict['malicious'] = malicious_bool
				feature.append([url, ret_dict])
	resultwriter(feature, output_dest)


def process_test_list(file_dest, output_dest):
	"""docstring for process_test_list"""
	feature = []
	with open(file_dest) as file:
		for line in file:
			url = line.strip()
			if url != '':
				# show off
				print 'working on: ' + url
				ret_dict = urlfeature.feature_extract(url)
				feature.append([url, ret_dict])
	resultwriter(feature, output_dest)


# change
def process_test_url(url, output_dest):
	"""docstring for process_test_url"""
	feature = []
	url = url.strip()
	if url != '':
		# show off
		print 'working on: ' + url
		ret_dict = urlfeature.feature_extract(url)
		feature.append([url, ret_dict])
	resultwriter(feature, output_dest)


def main():
	"""docstring for main"""
	# process_URL_list('URL.txt', 'url_features.csv)
	process_test_list('query.txt', 'query_features.csv')
	
	# tr.train('url_features.csv', 'url_features.csv')
	# arguments: (input_trainging features, test/query_trainging features)
	
	# testing with urls in query.txt
	tr.train('url_features.csv', 'query_features.csv')