import math
import numpy as np
import matplotlib.pyplot as plt

class Atom():

	def __init__(self, pos, c):
		self.pos = np.array(pos)		# Position array
		self.vel = np.zeros(len(pos))	# Velocity array
		self.bound = False				# Belongs to a Molecule?
		self.c = c						# Class assignment
				

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
			
	def attraction(self):
		for atom1 in self.atoms:
			atom1.vel = np.zeros(len(atom1.vel))
			for atom2 in self.atoms:
				atom1.vel = atom1.vel + self.DLVO(atom1, atom2)

		for atom in self.atoms:
			atom.pos = atom.pos + atom.vel

	# Get the DLVO result
	def DLVO(self, atom1, atom2):
		dist = np.linalg.norm(atom1.pos - atom2.pos)
		if dist == 0:
			return np.zeros(len(atom1.vel))
		HA = (self.a)/(np.exp(self.b*dist))
		ER = (self.c)/(self.d*dist**2)
		E = np.abs(HA - ER)
		return E * (atom1.pos - atom2.pos)/dist

	# TEMP - FOR DEBUGGING
	def draw_universe_2d(self):
		for atom in self.atoms:
			plt.plot(atom.pos[0], atom.pos[1], 'k.')
		plt.show()

	# TEMP - FOR DEBUGGING
	def return_frame(self):
		X = []
		Y = []
		for atom in self.atoms:
			X.append(atom.pos[0])
			Y.append(atom.pos[1])

		return [X.copy(), Y.copy()]
