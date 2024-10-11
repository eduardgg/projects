#include "stdafx.h"
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<double> VD;
typedef vector<vector<double>> MD;

int main() 
{

	int nx, ny, nz;
	double h;
	int i, j;
	cin >> nx >> ny >> nz >> h;

	MD Dx((nx - 1)*ny*nz, VD(nx*ny*nz, 0));
		for (i = 0; i < (nx - 1)*ny*nz; ++i) 
		{
			Dx[i][i] = -1;
			Dx[i][i + ny*nz] = 1;
		}

	MD Dy(nx*(ny - 1)*nz, VD(nx*ny*nz, 0));
	for (i = 0; i < nx; ++i) 
	{
		for (j = 0; j < (ny - 1)*nz; ++j) 
		{
			Dy[i*(ny - 1)*nz + j][i*ny*nz + j] = -1;
			Dy[i*(ny - 1)*nz + j][i*ny*nz + j + nz] = -1;
		}
	}

	MD Dz(nx*ny*(nz - 1), VD(nx*ny*nz, 0));
	for (i = 0; i < nx*ny; ++i) 
	{
		for (j = 0; j < nz - 1; ++j) 
		{
			Dz[i*(nz - 1) + j][i*nz + j] = -1;
			Dz[i*(nz - 1) + j][i*nz + j + 1] = 1;
		}
	}
	
	MD G((nx - 1)*ny*nz + nx*(ny - 1)*nz + nx*ny*(nz - 1), VD(nx*ny*nz));
	for (i = 0; i < (nx - 1)*ny*nz; ++i) 
	{
		for (j = 0; j < nx*ny*nz; ++j) 
		{
			G[i][j] = Dx[i][j];
		}
	}
	for (i = 0; i < nx*(ny-1)*nz; ++i) 
	{
		for (j = 0; j < nx*ny*nz; ++j) 
		{
			G[i + (nx - 1)*ny*nz][j] = Dy[i][j];
		}
	}
	for (i = 0; i < nx*ny*(nz-1); ++i) 
	{
		for (j = 0; j < nx*ny*nz; ++j) 
		{
			G[i + (nx - 1)*ny*nz + nx*(ny - 1)*nz][j] = Dz[i][j];
		}
	}

	for (i = 0; i < (nx - 1)*ny*nz + nx*(ny - 1)*nz + nx*ny*(nz - 1); ++i) 
	{
		for (j = 0; j < nx*ny*nz; ++j) 
		{
			G[i][j] = G[i][j] / h;
			if (G[i][j] < 0) cout << " " << G[i][j];
			else cout << "  " << G[i][j];
		}
		cout << endl;
	}

}