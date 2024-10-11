
#include "stdafx.h"
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<double> VD;
typedef vector<vector<double>> MD;

int i, j, k;

int main()
{

	// BANDERA (fins aquí actualitzat i revisat)
	-------------------------------------------------------------------------------------
	function[] = poisson(c, nx, ny, nz, h, E, data)

		% L'entrada del programa és un "bloc de notes" que conté n files, cada una
		% amb 6 nombres espaiats.Els tres primers corresponen a les coordenades
		% x, y, z dels punts, i els tres següents a les components del vector normal
		% a la superfície en aquells punts.Per tal que tot funcioni bé, haurem
		% d'emmagatzemar aquests valors en dues matrius: P, de dimensió n x 3, que
		% contindrà els punts, i N, de dimensió n x 3, que contindrà els vectors
		% normals.


		% Per transformar - ho en una taula de valors i operar matricialment, usem
		% l'opció "Import Data" de Matlab.

		% data és la matriu de dimensió n x 6 obtinguda de l' "import data".

		[n, m] = size(data);

	P = data(:, [1 2 3]);
	N = data(:, [4 5 6]);

	G = grad(nx, ny, nz, h);

	[v, W] = interpolation(c, n, nx, ny, nz, h, P, N);

	% Mitjançant el mètode dels mínims quadrats(least squares method), obtenim
		% el sistema lineal G'*G*g = G'*v.El problema d'aquest sistema és que 
		% sovint(sempre ? ) la matriu G'*G no és invertible, i per tant no es pot
		% resoldre.Per solucionar aquest problema, una opció és sumar una matriu
		% diagonal d' "epsilons" a G'*G perquè deixi de ser singular.D'aquesta
		% manera s'obté una solució bastant fidel a la real. Deixarem aquest
		% epsilon com a input del programa(E).

		g = (G'*G+E*eye(nx*ny*nz))\(G'*v);

	% L'altra opció per resoldre el sistema és fent ús del CG Solver (Conjugate
		% Gradient Solver) de Matlab, que simplement afegeix una restricció a la
		% solució per tal que la suma de les solucions sigui zero.

		% Calculem l'iso-level "Sigma", fent servir la corresponent fórmula:

		Sigma = 1 / n * ones(n, 1)' * W * g; 

		% Anem a construir la hipermatriu 3D(3D Array) de tamany nx·ny·nz que
		% conté els valors del vector g de dimensió nx*ny*nz ben classificats.

		counter = 1;
	for i = 1:nx
		for j = 1 : ny
			for k = 1 : nz
				V(i, j, k) = g(counter);
	counter = counter + 1;
	end
		end
		end

		% Investigar la funció "isosurface" (ajuda Matlab)
		% Matlab function that implements an algorithm called "marching cubes"
		% La funció "patch" representa l'estructura S

		p = patch(isosurface(V, Sigma))

		% Donem color a les cares i vèrtexs de la malla

		p.FaceColor = 'yellow';
	p.EdgeColor = 'none';

	axis tight
		camlight
		lighting gouraud

		end
	-------------------------------------------------------------------------------------
	cin >> i;
    return 0;
}
