---------------
Experimentateur
---------------


.. toctree::
   :maxdepth: 1

   experience.rst

~~~~~~~~~~
Etat du TP
~~~~~~~~~~

En cours

~~~~~~~~~~~~~~~~~~~~~~
Réponses aux questions
~~~~~~~~~~~~~~~~~~~~~~

Indiquez ici les réponses aux questions posées dans le TP. Vous
reprendrez le numéro de la section et le numéro de la question. Par
exemple pour répondre à la question 3 de la section 2.4 vous
indiquerez.

Question 1.2.2
--------------

OP= nombres de comparaisons

Question 1.2.3
--------------

pire cas: si il n'y a pas de marqueurs positif

meilleur cas: le premier marqueur est positif

Question 1.2.4
--------------
pire cas : c1(m,p)=taille de p * taille de m

meilleur cas: c1(m,p)=1


Question 1.3.2
--------------

pire cas: si le tableau est trie a l'envers (ordre décroissant) et qu'il n'y a pas de marqueurs positif
	  n=taille du tableau p
	  c2(m,p)= nlog(n) +c1


Question 1.4.2
--------------
pire cas : le marqueur positif est au dernier emplacement du tableau marqueur et positive
	  n=taille du tableau m

	  c3(m,p)= nlog(n) +c2

Question 1.5.2
--------------
Versions:
	Strategie 1:
		Markers: ['m9', 'm2', 'm3', 'm0', 'm7', 'm4', 'm6', 'm5', 'm8', 'm1']

		Positive markers: ['m9', 'm2']

		Negative markers: [] 

		Nb. comparaisons: 1	#strategie 1

		Negative markers: []

		Nb. comparaisons: 2	#strategie 2

		Negative markers: ['m0', 'm1']

		Nb. comparaisons: 5	#strategie 3


	Strategie 2:
		Markers: ['m4', 'm5', 'm1', 'm9', 'm3', 'm7', 'm0', 'm6', 'm8', 'm2']

		Positive markers: ['m8', 'm4']

		Negative markers: []

		Nb. comparaisons: 2	#strategie 1

		Negative markers: []

		Nb. comparaisons: 1	#strategie 2

		Negative markers: ['m0', 'm1', 'm2', 'm3']

		Nb. comparaisons: 9	#strategie 3

	
	Strategie 3:
		Markers: ['m1', 'm2', 'm5', 'm4', 'm3', 'm9', 'm6', 'm7', 'm8', 'm0']

		Positive markers: ['m0', 'm8']

		Negative markers: ['m1', 'm2', 'm5', 'm4', 'm3', 'm9', 'm6', 'm7']

		Nb. comparaisons: 18	#strategie 1

		Negative markers: ['m1', 'm2', 'm5', 'm4', 'm3', 'm9', 'm6', 'm7']

		Nb. comparaisons: 18	#strategie 2

		Negative markers: []

		Nb. comparaisons: 1	#strategie 3



	

On peut constater quand fonctions des situations, une strategie peut être plus performante que les autres.
Cela vient du fait que selon la disposition des markers dans les tableaux, les algorithmes de tri effectuent plus ou moins de comparaisons.

Question 1.5.6
--------------

<img src='../src/fichier1.png'/>

