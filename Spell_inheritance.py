'''
Class example from internet
'''

class Spell(object):

	def __init__(self, incantation, name):
		self.name = name
		self.incantation = incantation

	def __str__(self):
		return self.name + ' ' + self.incantation + '\n' + self.get_description()

	def get_description(self):
		return 'No description'

	def execute(self):
		print (self.incantation)


class Accio(Spell):

	def __init__(self):
		Spell.__init__(self, 'Accio', 'Summoning Charm')

	def __str__(self):
		return self.incantation +' '+ self.name +'\n' + self.get_description()

	def get_description(self):
		return 'This charm summons an object to the caster, potentially over a significant distance.'

class Confundo(Spell):

	def __init__(self):
		Spell.__init__(self, 'Confundo', 'Confundus Charm')

	def get_description(self):
		return 'Causes the victim to become confused and befuddled.'



def study_spell(spell):
	print (spell)


spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())
print (Accio())