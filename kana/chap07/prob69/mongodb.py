from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING


class MongoDB:
	def __init__(self):
		client = MongoClient('localhost', 27017)
		# データベースを呼び出し (名前: my_database)
		db = client.my_database
		# コレクションを呼び出し (名前: my_collection)
		self.co = db.my_collection

	def get_alias_name(self, row):
		try:
			aliases_name = ' '.join(alias['name'] for alias in row['aliases'])
		except:
			aliases_name = "------"
		return aliases_name	

	def get_area(self, row):
		try:
			area = row['area']
		except:
			area = "------"
		return area

	def get_begin(self, row):
		try:
			begin = row['begin']['year']
		except:
			begin = "------"
		return begin	

	def get_end(self, row):
		try:
			end = row['end']['year']
		except:
			end = "------"
		return end	

	def get_tags(self, row):
		try:
			tags = ', '.join(tag['value'] for tag in row['tags'])
		except:
			tags = "------"
		return tags

	def get_rating(self, row):
		try:
			rating = row['rating']['value']
		except:
			rating = 0
		return rating	

	def get_artist(self, name, area, tag):

		all_condition = []
		if name != "":
			all_condition.append({ '$or' : [{'name': name}, {'aliases.name': name}]})
		if area != "":
			all_condition.append({'area' : area})
		if tag != "":
			all_condition.append({'tags.value' : tag})

		condition = {'$and' : all_condition}
		
		print(condition)
		results = []
		for row in self.co.find(condition).sort('rating.value', DESCENDING):

			aliases_name = self.get_alias_name(row)
			area = self.get_area(row)
			begin = self.get_begin(row)
			end = self.get_end(row)
			tags = self.get_tags(row)
			rating = self.get_rating(row)


			results.append({"name": row['name'],  "aliases_name":aliases_name, "area": area, "begin" : begin, "end" : end, "tag":tags, "rating":rating})
		
		return results


