import math
import numpy as np
import matplotlib.pyplot as plt

class Atom():

	def __init__(self, pos, c):
		self.pos = np.array(pos)	# Position array
		self.vel = np.zeros(len(pos))	# Velocity array
		self.bound = False			# Belongs to a Molecule?
		self.c = c					# Class assignment
				

class Molecule():

	def __init__(self, pos, vel, atoms):
		self.pos = pos
		self.vel = vel
		self.atoms = atoms


class Universe():
	
	def __init__(self, data, params):
		self.classes = 0
		self.a = params[0]
		self.b = params[1]
		self.c = params[2]
		self.d = params[3]
		self.atoms = []
		self.molecules = []

		self.make_atoms(data)

	def make_atoms(self, data):
		for point in data:
			self.atoms.append(Atom(point, self.classes))
			self.classes = self.classes + 1
			
	def interact_atoms(self):
		for atom in self.atoms:
			atom.interact(self.atoms)

	# TEMP - FOR DEBUGGING
	def draw_universe_2d(self):
		for atom in self.atoms:
			plt.plot(atom.pos[0], atom.pos[1], 'k.')
		plt.show()

# Get the DLVO result
def DLVO(d, a1, a2, a3, a4):
    HA = (a1)/(np.exp(a2*d)) 	# Hamaker Attraction
    ER = (a3)/(a4*d**2) 		# Electronic Repulsion
    return HA - ER				# Sum of Terms