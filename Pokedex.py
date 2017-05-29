import json

class Pokedex:
	
	def __list_withconditions_b(self, listpoke, term):
		return list(element for element in listpoke if element[term])
	
	def __list_withconditions(self, listpoke, term, expectedresult):
		return list(element for element in listpoke if element[term] == expectedresult)
	
	def __dictionary_of_pokedexbreakdown(self, name, listpoke):
		self.__exampledict[name] = len(list(element for element in listpoke if element["Game"] == name))
	
	def __init__(self, name, jsondata):
		self.__pokedexname = name

		#RBY, GSC, RSE, DPP, HGSS, BW, XY, ORAS, SM
		pokemon_in_dex = self.__list_withconditions(jsondata, name, True) #list(element for element in jsondata if element[name] == True)
		
		#gen = (element for element in jsondata if element[name] == True)
		
		standardgen = self.__list_withconditions(pokemon_in_dex, 'Legendary', 0) # list(element for element in pokemon_in_dex if element["Legendary"] == 0)
		standardshiny = self.__list_withconditions_b(pokemon_in_dex, 'Game') #list(element for element in pokemon_in_dex if element["Game"])
		
		self.__standardindex = len(standardgen)
		
		self.__shinydex = len(standardshiny)
		self.__exampledict = {}
		self.__dictionary_of_pokedexbreakdown("RBY", standardshiny)
		self.__dictionary_of_pokedexbreakdown("GSC", standardshiny)
		self.__dictionary_of_pokedexbreakdown("RSE", standardshiny)
		self.__dictionary_of_pokedexbreakdown("DPP", standardshiny)
		self.__dictionary_of_pokedexbreakdown("HGSS", standardshiny)
		self.__dictionary_of_pokedexbreakdown("BW", standardshiny)
		self.__dictionary_of_pokedexbreakdown("XY", standardshiny)
		self.__dictionary_of_pokedexbreakdown("ORAS", standardshiny)
		self.__dictionary_of_pokedexbreakdown("SM", standardshiny)
		
	def get_totalindex(self):
		return self.__standardindex
	
	def get_shinydex(self):
		return self.__shinydex
	
	def get_percentage(self, part, whole):
		return "{:0.2f}".format(100 * float(part) / float (whole))
	
	def print_details(self):
		print("{0} dex. \nTotal standard: {1}. Total shiny standard: {2}. Percentage: {3}".format(
			self.__pokedexname, self.get_totalindex(), self.get_shinydex(), 
			self.get_percentage(self.get_shinydex(), self.get_totalindex())
		))
		
		print("{0}\n".format(self.__exampledict))