
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

	// BANDERA (fins aqu� actualitzat i revisat)
	-------------------------------------------------------------------------------------
	function[] = poisson(c, nx, ny, nz, h, E, data)

		% L'entrada del programa �s un "bloc de notes" que cont� n files, cada una
		% amb 6 nombres espaiats.Els tres primers corresponen a les coordenades
		% x, y, z dels punts, i els tres seg�ents a les components del vector normal
		% a la superf�cie en aquells punts.Per tal que tot funcioni b�, haurem
		% d'emmagatzemar aquests valors en dues matrius: P, de dimensi� n x 3, que
		% contindr� els punts, i N, de dimensi� n x 3, que contindr� els vectors
		% normals.


		% Per transformar - ho en una taula de valors i operar matricialment, usem
		% l'opci� "Import Data" de Matlab.

		% data �s la matriu de dimensi� n x 6 obtinguda de l' "import data".

		[n, m] = size(data);

	P = data(:, [1 2 3]);
	N = data(:, [4 5 6]);

	G = grad(nx, ny, nz, h);

	[v, W] = interpolation(c, n, nx, ny, nz, h, P, N);

	% Mitjan�ant el m�tode dels m�nims quadrats(least squares method), obtenim
		% el sistema lineal G'*G*g = G'*v.El problema d'aquest sistema �s que 
		% sovint(sempre ? ) la matriu G'*G no �s invertible, i per tant no es pot
		% resoldre.Per solucionar aquest problema, una opci� �s sumar una matriu
		% diagonal d' "epsilons" a G'*G perqu� deixi de ser singular.D'aquesta
		% manera s'obt� una soluci� bastant fidel a la real. Deixarem aquest
		% epsilon com a input del programa(E).

		g = (G'*G+E*eye(nx*ny*nz))\(G'*v);

	% L'altra opci� per resoldre el sistema �s fent �s del CG Solver (Conjugate
		% Gradient Solver) de Matlab, que simplement afegeix una restricci� a la
		% soluci� per tal que la suma de les solucions sigui zero.

		% Calculem l'iso-level "Sigma", fent servir la corresponent f�rmula:

		Sigma = 1 / n * ones(n, 1)' * W * g; 

		% Anem a construir la hipermatriu 3D(3D Array) de tamany nx�ny�nz que
		% cont� els valors del vector g de dimensi� nx*ny*nz ben classificats.

		counter = 1;
	for i = 1:nx
		for j = 1 : ny
			for k = 1 : nz
				V(i, j, k) = g(counter);
	counter = counter + 1;
	end
		end
		end

		% Investigar la funci� "isosurface" (ajuda Matlab)
		% Matlab function that implements an algorithm called "marching cubes"
		% La funci� "patch" representa l'estructura S

		p = patch(isosurface(V, Sigma))

		% Donem color a les cares i v�rtexs de la malla

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
