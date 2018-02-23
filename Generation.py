import json
import os

class Generation1:
	def __init__(self):
		self.gen = 1
		self.term = ["RBY"]
		self.lowercount = 1
		self.uppercount = 151
	
class Generation2:
	def __init__(self):
		self.gen = 2
		self.term = ["GSC"]
		self.uppercount = 251
		self.lowercount = 152
		
class Generation3:
	def __init__(self):
		self.gen = 3
		self.term = ["RSE","FRLG"]
		self.lowercount = 252
		self.uppercount = 386
	
class Generation4:
	def __init__(self):
		self.gen = 4
		self.term = ["DPP", "HGSS"]
		self.uppercount = 493
		self.lowercount = 387
		
class Generation5:
	def __init__(self):
		self.gen = 5
		self.term = ["BW"]
		self.lowercount = 494
		self.uppercount = 649
	
class Generation6:
	def __init__(self):
		self.gen = 6
		self.term = ["XY", "ORAS"]
		self.uppercount = 721
		self.lowercount = 650
		
class Generation7:
	def __init__(self):
		self.gen = 7
		self.term = ["SM", "USUM"]
		self.uppercount = 806
		self.lowercount = 721

class Generation:
	
	def __list_withconditions(self, listpoke, term, expectedresult):
		return list(element for element in listpoke if element[term] == expectedresult)
	
	def __dictionary_of_pokedexbreakdown(self, name, genobj, instance, listpoke):
		
		self.__standardgencount = len(list(element for element in listpoke if 
										  	genobj.lowercount <= element["DexNo"] <= genobj.uppercount and 
										   element["ShinyLocked"] == 0 and
										   element["Legendary"] == 0))
		
		self.__legendgencount =len(list(element for element in listpoke if 
											genobj.lowercount <= element["DexNo"] <= genobj.uppercount and 
										element["ShinyLocked"] == 0 and
										element["Legendary"] == 1))
		
		self.__ubgencount =len(list(element for element in listpoke if 
											genobj.lowercount <= element["DexNo"] <= genobj.uppercount and 
										element["Legendary"] == 3))
		
		self.__exampledict[name] = len(list(element for element in listpoke if 
											element["Game"] in instance.term and 
											genobj.lowercount <= element["DexNo"] <= genobj.uppercount and
										    element["Legendary"] == 0))
		
		self.__legendarydict[name] = len(list(element for element in listpoke if 
											element["Game"] in instance.term and 
											genobj.lowercount <= element["DexNo"] <= genobj.uppercount and
										    element["Legendary"] == 1))
		
		self.__ubdict[name] = len(list(element for element in listpoke if 
											element["Game"] in instance.term and 
											genobj.lowercount <= element["DexNo"] <= genobj.uppercount and
										    element["Legendary"] == 3))
		
	def get_percentage(self, part, whole):
		return "{:0.2f}".format(100 * float(part) / float (whole))
	
	def select_gen(self, indexno):
		if indexno == 1:
			genobj = Generation1()
		elif indexno == 2:
			genobj = Generation2()
		elif indexno == 3:
			genobj = Generation3()
		elif indexno == 4:
			genobj = Generation4()
		elif indexno == 5:
			genobj = Generation5()
		elif indexno == 6:
			genobj = Generation6()
		elif indexno == 7:
			genobj = Generation7()
		else:
			pass
		
		return genobj
	
	def __init__(self, gennum, jsondata):
		self.__gen_num = gennum

		self.__exampledict = {}
		self.__legendarydict = {}
		self.__ubdict = {}
		
		genunderinvestigation = self.select_gen(gennum)
		
			
		for i in range(7):
			instance = self.select_gen(i+1)
			self.__dictionary_of_pokedexbreakdown(i+1, genunderinvestigation, instance, jsondata)
			
		
		
	def print_details_to_file(self):
		
		directory = os.getcwd() +  "/GeneratedFile"
		print("{0}".format(directory))
		if not os.path.exists(directory):
			os.mkdir(directory)
		os.chdir(os.getcwd() + "/GeneratedFile")
		
		directory = os.getcwd() +"/Generation"
		if not os.path.exists(directory):
			os.mkdir(directory)
		os.chdir("Generation")
		
		filename = open("Generation{0}.txt".format(self.__gen_num), "w")
		
		#########
		filename.write("Generation{0}. \nStandard Total: {1}. Total shiny: {2}. Percentage: {3}\n".format(
			self.__gen_num, self.__standardgencount, sum(self.__exampledict.values()), 
			self.get_percentage(sum(self.__exampledict.values()), self.__standardgencount)
		))
		
		filename.write("{0}\n".format(self.__exampledict))
		
		#########
		filename.write("Generation{0}. \nLegendary Total: {1}. Total shiny: {2}. Percentage: {3}\n".format(
			self.__gen_num, self.__legendgencount, sum(self.__legendarydict.values()), 
			self.get_percentage(sum(self.__legendarydict.values()), self.__legendgencount)
		))
		filename.write("{0}\n".format(self.__legendarydict))
		
		#########
		print("Generation{0}: {1}".format(self.__gen_num, self.__ubgencount))
		if self.__ubgencount > 0:
			filename.write("Generation{0}. \nUB Total: {1}. Total shiny: {2}. Percentage: {3}\n".format(
				self.__gen_num, self.__ubgencount, sum(self.__ubdict.values()), 
				self.get_percentage(sum(self.__ubdict.values()), self.__ubgencount)
			))
			
			filename.write("{0}\n".format(self.__ubdict))
		
		#########
		
		filename.close()
		
		os.chdir("../../")