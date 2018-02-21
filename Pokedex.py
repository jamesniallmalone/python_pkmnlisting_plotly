import json
import os

class Pokedex:
	
	def __list_withconditions_b(self, listpoke, term):
		return list(element for element in listpoke if element[term])
	
	def __list_withconditions(self, listpoke, term, expectedresult):
		return list(element for element in listpoke if element[term] == expectedresult)
	
	def __dictionary_of_pokedexbreakdown(self, name, listpoke):
		self.__exampledict[name] = len(list(element for element in listpoke if element["Game"] == name))
	
	def __init__(self, name, jsondata):
		self.__pokedexname = name

		#RBY, GSC, FRLG, RSE, DPP, HGSS, BW, XY, ORAS, SM, USUM
		pokemon_in_dex = self.__list_withconditions(jsondata, name, True)
		
		standardgen = self.__list_withconditions(pokemon_in_dex, 'Legendary', 0)
		standardshiny = self.__list_withconditions_b(pokemon_in_dex, 'Game')
		
		self.__standardindex = len(standardgen)
		
		self.__shinydex = len(standardshiny)
		self.__exampledict = {}
		self.__dictionary_of_pokedexbreakdown("RBY", standardshiny)
		self.__dictionary_of_pokedexbreakdown("GSC", standardshiny)
		self.__dictionary_of_pokedexbreakdown("RSE", standardshiny)
		self.__dictionary_of_pokedexbreakdown("FRLG", standardshiny)
		self.__dictionary_of_pokedexbreakdown("DPP", standardshiny)
		self.__dictionary_of_pokedexbreakdown("HGSS", standardshiny)
		self.__dictionary_of_pokedexbreakdown("BW", standardshiny)
		self.__dictionary_of_pokedexbreakdown("XY", standardshiny)
		self.__dictionary_of_pokedexbreakdown("ORAS", standardshiny)
		self.__dictionary_of_pokedexbreakdown("SM", standardshiny)
		self.__dictionary_of_pokedexbreakdown("USUM", standardshiny)
		
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
		
		
		
	def print_details_to_file(self):
		print("{0}\n".format(os.getcwd()))
		
		directory = os.getcwd() +  "/GeneratedFile"
		print("{0}".format(directory))
		if not os.path.exists(directory):
			os.mkdir(directory)
		os.chdir(os.getcwd() + "/GeneratedFile")
		
		directory = os.getcwd() +"/Pokedex"
		if not os.path.exists(directory):
			os.mkdir(directory)
		os.chdir("Pokedex")
			
		filename = open("{0}dex.txt".format(self.__pokedexname), "w")
		
		
		
		filename.write("{0} dex. \nTotal standard: {1}. Total shiny standard: {2}. Percentage: {3}\n".format(
			self.__pokedexname, self.get_totalindex(), self.get_shinydex(), 
			self.get_percentage(self.get_shinydex(), self.get_totalindex())
		))
		
		filename.write("{0}\n".format(self.__exampledict))
		filename.close()
		
		os.chdir("../../")