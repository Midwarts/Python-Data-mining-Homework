import json

# 地区类
class Area:
	# 构造函数
	def __init__(self, name, parentName):
		# 名称
		self.name = name
		# 上级地区名称
		self.parentName = parentName
		# 下级地区数组
		self.children = []
	# 根据名称查找地区对象函数
	def search(self, searchName):
		if self.name == searchName:
			return self
		for child in self.children:
			childSearchResult = child.search(searchName)
			if (None != childSearchResult):
				return childSearchResult

if __name__ == '__main__':
	# 读取json
	str_file = 'D:\\中国传媒大学\\大一下\\jupyter\\中国地名表.json'
	with open(str_file, 'r') as f:
		r = json.load(f)

	# 组装对象
	countryArea = Area(r['root']['name'], '')
	for province in r['root']['province']:
		provinceArea = Area(province['name'], countryArea.name)
		countryArea.children.append(provinceArea)
		if 'name' in province['city']:
			city = province['city']
			cityArea = Area(city['name'], provinceArea.name)
			provinceArea.children.append(cityArea)
			if 'area' in city:
				for county in city['area']:
					countyArea = Area(county['name'], cityArea.name)
		else:
			for city in province['city']:
				cityArea = Area(city['name'], provinceArea.name)
				provinceArea.children.append(cityArea)
				if 'area' in city:
					if 'name' not in city['area']:
						for county in city['area']:
							countyArea = Area(county['name'], cityArea.name)
							cityArea.children.append(countyArea)

	while True:
		# 根据传入参数调用查找地区
		searchName = input("请输入要查询的地区名称(输入exit退出查询)（请以xx省、xx市的格式输入）: ")
		if 'exit' == searchName:
			break
		searchArea = countryArea.search(searchName)

		#打印地区信息
		if None == searchArea:
			print('查询的地区"' + searchName + '"不存在!')
		else:
			print('上级地区名称：' + searchArea.parentName)
			print('下级地区名称列表：')
			for child in searchArea.children:
				print(child.name)
