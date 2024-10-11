
#include "stdafx.h"
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<double> VD;
typedef vector<vector<double>> MD;
typedef vector<int> VI;
typedef vector<vector<int>> MI;

int nx, ny, nz, n;
int i, j, k, u;
int r, s, t;
int xi, yi, zi;
int xf, yf, zf;
bool b;
double h;
double wx, wy, wz;
VD c(3);

MD prodmm(MD A, MD B)
{
	r = A.size();
	s = B.size();
	t = B[0].size();
	MD C(r, VD(t, 0));
	for (i = 0; i < r; ++i)
	{
		for (j = 0; j < t; ++j)
		{
			for (k = 0; k < s; ++k)
			{
				C[i][j] = C[i][j] + A[i][k] * B[k][j];
			}
		}
	}
	return C;
}

VD prodmv(MD A, VD v)
{
	r = A.size();
	s = v.size();
	VD w(r,0);
	for (i = 0; i < r; ++i)
	{
		for (j = 0; j < s; ++j)
		{
			w[i] = w[i] + A[i][j] * v[j];
		}
	}
	return w;
}

MD trans(MD A)
{
	r = A.size();
	s = A[0].size();
	MD T(s, VD(r));
	for (i = 0; i < r; ++i)
	{
		for (j = 0; j < s; ++j)
		{
			T[j][i] = A[i][j];
		}
	}
	return T;
}

MD vectomat(VD v)
{
	r = v.size();
	MD M(r, VD(1));
	for (i = 0; i < r; ++i)
	{
		M[i][0] = v[i];
	}
	return M;
}

int main()
{

	cin >> nx >> ny >> nz >> n >> h;
	cin >> c[1] >> c[2] >> c[3];

	MD P(n, VD(3));
	MD N(n, VD(3));
	VD Nx(n);
	VD Ny(n);
	VD Nz(n);
	VD vx((nx - 1)*ny*nz);
	VD vy(nx*(ny - 1)*nz);
	VD vz(nx*ny*(nz - 1));
	VD v((nx - 1)*ny*nz + nx*(ny - 1)*nz + nx*ny*(nz - 1));
	MD W(n, VD(nx*ny*nz, 0));
	MD Wx(n, VD((nx - 1)*ny*nz, 0));
	MD Wy(n, VD(nx*(ny - 1)*nz, 0));
	MD Wz(n, VD(nx*ny*(nz - 1), 0));
	MD Wxt((nx - 1)*ny*nz, VD(n, 0));
	MD Wyt(nx*(ny - 1)*nz, VD(n, 0));
	MD Wzt(nx*ny*(nz - 1), VD(n, 0));
	MI Sx(n, VI(3));
	MI Sy(n, VI(3));
	MI Sz(n, VI(3));
	MI PG(n, VI(3));

	for (u = 0; u < n; ++u)
	{
		cin >> P[u][0] >> P[u][1] >> P[u][2];
		cin >> N[u][0] >> N[u][1] >> N[u][2];
	}

	for (u = 0; u < n; ++u)
	{

		if (P[u][0] < c[0] + h / 2)
		{
			Sx[u][0] = 0;
		}
		else if (P[u][0] >= c[0] + (nx - 3 / 2)*h)
		{
			Sx[u][0] = nx - 1;
		}
		else
		{
			b = true;
			i = 1;
			while ((i <= nx - 2) && (b == 1))
			{
				if ((P[u][0] >= c[0] + h*(i - 1 / 2)) && (P[u][0] < c[0] + h*(i + 1 / 2)))
				{
					Sx[u][0] = i;
					b = 0;
				}
				++i;
			}
		}

		if (P[u][1] < c[1] + h / 2)
		{
			Sy[u][1] = 0;
		}
		else if (P[u][1] >= c[1] + (ny - 3 / 2)*h)
		{
			Sy[u][1] = ny - 1;
		}
		else
		{
			b = 1;
			i = 1;
			while ((i <= ny - 2) && (b == 1))
			{
				if ((P[u][1] >= c[1] + h*(i - 1 / 2)) && (P[u][1] < c[1] + h*(i + 1 / 2)))
				{
					Sy[u][1] = i;
					b = 0;
				}
				++i;
			}
		}

		if (P[u][2] < c[2] + h / 2)
		{
			Sz[u][2] = 0;
		}
		else if (P[u][2] >= c[2] + (nz - 3 / 2)*h)
		{
			Sz[u][2] = nz - 1;
		}
		else
		{
			b = 1;
			i = 1;
			while ((i <= nz - 2) && (b == 1))
			{
				if ((P[u][2] >= c[2] + h*(i - 1 / 2)) && (P[u][2] < c[2] + h*(i + 1 / 2)))
				{
					Sz[u][2] = i;
					b = 0;
				}
				++i;
			}
		}

		b = 1;
		i = 0;
		while ((i <= nx - 1) && (b == 1))
		{
			if ((P[u][0] >= c[0] + h*i) && (P[u][0] < c[0] + h*(i + 1)))
			{
				Sy[u][0] = i;
				Sz[u][0] = i;
				b = 0;
			}
			++i;
		}

		b = 1;
		i = 0;
		while ((i <= ny - 1) && (b == 1))
		{
			if ((P[u][1] >= c[1] + h*i) && (P[u][1] < c[1] + h*(i + 1)))
			{
				Sz[u][1] = i;
				Sx[u][1] = i;
				b = 0;
			}
			++i;
		}

		b = 1;
		i = 0;
		while ((i <= nz - 1) && (b == 1))
		{
			if ((P[u][2] >= c[2] + h*i) && (P[u][2] < c[2] + h*(i + 1)))
			{
				Sx[u][2] = i;
				Sy[u][2] = i;
				b = 0;
			}
			++i;
		}

	}

	for (u = 0; u < n; ++u)
	{

		wx = (c[0] + h*(Sx[u][0] + 1 / 2) - P[u][0]) / h;
		wy = (c[1] + h*(Sx[u][1] + 1) - P[u][1]) / h;
		wz = (c[2] + h*(Sx[u][2] + 1) - P[u][2]) / h;

		xi = Sx[u][0] - 1;
		yi = Sx[u][1];
		zi = Sx[u][2];

		xf = xi + 1;
		yf = yi + 1;
		zf = zi + 1;

		if (Sx[u][0] < nx - 1)
		{
			Wx[u][zi + nz*yi + nz*ny*xf] = (1 - wx)*wy*wz;
			Wx[u][zf + nz*yi + nz*ny*xf] = (1 - wx)*wy*(1 - wz);
			Wx[u][zi + nz*yf + nz*ny*xf] = (1 - wx)*(1 - wy)*wz;
			Wx[u][zf + nz*yf + nz*ny*xf] = (1 - wx)*(1 - wy)*(1 - wz);
		}

		if (Sx[u][0] > 0)
		{
			Wx[u][zi + nz*yi + nz*ny*xi] = wx*wy*wz;
			Wx[u][zf + nz*yi + nz*ny*xi] = wx*wy*(1 - wz);
			Wx[u][zi + nz*yf + nz*ny*xi] = wx*(1 - wy)*wz;
			Wx[u][zf + nz*yf + nz*ny*xi] = wx*(1 - wy)*(1 - wz);
		}

	}

	for (u = 0; u < n; ++u)
	{

		wx = (c[0] + h*(Sy[u][0] + 1) - P[u][0]) / h;
		wy = (c[1] + h*(Sy[u][1] + 1 / 2) - P[u][1]) / h;
		wz = (c[2] + h*(Sy[u][2] + 1) - P[u][2]) / h;

		xi = Sy[u][0];
		yi = Sy[u][1] - 1;
		zi = Sy[u][2];

		xf = xi + 1;
		yf = yi + 1;
		zf = zi + 1;

		if (Sy[u][1] < ny - 1)
		{
			Wy[u][zi + nz*yf + nz*(ny - 1)*xi] = wx*(1 - wy)*wz;
			Wy[u][zf + nz*yf + nz*(ny - 1)*xi] = wx*(1 - wy)*(1 - wz);
			Wy[u][zi + nz*yf + nz*(ny - 1)*xf] = (1 - wx)*(1 - wy)*wz;
			Wy[u][zf + nz*yf + nz*(ny - 1)*xf] = (1 - wx)*(1 - wy)*(1 - wz);
		}

		if (Sy[u][1] > 0)
		{
			Wy[u][zi + nz*yi + nz*(ny - 1)*xi] = wx*wy*wz;
			Wy[u][zf + nz*yi + nz*(ny - 1)*xi] = wx*wy*(1 - wz);
			Wy[u][zi + nz*yi + nz*(ny - 1)*xf] = (1 - wx)*wy*wz;
			Wy[u][zf + nz*yi + nz*(ny - 1)*xf] = (1 - wx)*wy*(1 - wz);
		}
	
	}

	for (u = 0; u < n; ++u)
	{

		wx = (c[0] + h*(Sz[u][0] + 1) - P[u][0]) / h;
		wy = (c[1] + h*(Sz[u][1] + 1) - P[u][1]) / h;
		wz = (c[2] + h*(Sz[u][2] + 1 / 2) - P[u][2]) / h;

		xi = Sz[u][0];
		yi = Sz[u][1];
		zi = Sz[u][2] - 1;

		xf = xi + 1;
		yf = yi + 1;
		zf = zi + 1;

		if (Sz[u][2] < nz - 1)
		{
			Wz[u][zf + (nz - 1)*yi + (nz - 1)*ny*xi] = wx*wy*(1 - wz);
			Wz[u][zf + (nz - 1)*yi + (nz - 1)*ny*xf] = (1 - wx)*wy*(1 - wz);
			Wz[u][zf + (nz - 1)*yf + (nz - 1)*ny*xi] = wx*(1 - wy)*(1 - wz);
			Wz[u][zf + (nz - 1)*yf + (nz - 1)*ny*xf] = (1 - wx)*(1 - wy)*(1 - wz);
		}

		if (Sz[u][2] > 0)
		{
			Wz[u][zi + (nz - 1)*yi + (nz - 1)*ny*xi] = wx*wy*wz;
			Wz[u][zi + (nz - 1)*yi + (nz - 1)*ny*xf] = (1 - wx)*wy*wz;
			Wz[u][zi + (nz - 1)*yf + (nz - 1)*ny*xi] = wx*(1 - wy)*wz;
			Wz[u][zi + (nz - 1)*yf + (nz - 1)*ny*xf] = (1 - wx)*(1 - wy)*wz;
		}

	}

	for (u = 0; u < n; ++u)
	{
		Nx[u] = N[u][0];
		Ny[u] = N[u][1];
		Nz[u] = N[u][2];
	}

	Wxt = trans(Wx);
	Wyt = trans(Wy);
	Wzt = trans(Wz);

	vx = prodmv(Wxt, Nx);
	vy = prodmv(Wyt, Ny);
	vz = prodmv(Wzt, Nz);

	for (i = 0; i < (nx - 1)*ny*nz; ++i) v[i] = vx[i];
	for (i = 0; i < nx*(ny - 1)*nz; ++i) v[i + (nx - 1)*ny*nz] = vy[i];
	for (i = 0; i < nx*ny*(nz - 1); ++i) v[i + (nx - 1)*ny*nz + nx*(ny - 1)*nz] = vz[i];

	for (i = 0; i < n; ++i)
	{
		PG[i][0] = Sy[i][0];
		PG[i][1] = Sz[i][1];
		PG[i][2] = Sx[i][2];
	}

	for (u = 0; u < n; ++u)
	{

		wx = (c[0] + h*(PG[u][0] + 1) - P[u][0]) / h;
		wy = (c[1] + h*(PG[u][1] + 1) - P[u][1]) / h;
		wz = (c[2] + h*(PG[u][2] + 1) - P[u][2]) / h;

		xi = PG[u][0];
		yi = PG[u][1];
		zi = PG[u][2];

		xf = xi + 1;
		yf = yi + 1;
		zf = zi + 1;

		W[u][zi + nz*yi + nz*ny*xf] = (1 - wx)*wy*wz;
		W[u][zf + nz*yi + nz*ny*xf] = (1 - wx)*wy*(1 - wz);
		W[u][zi + nz*yf + nz*ny*xf] = (1 - wx)*(1 - wy)*wz;
		W[u][zf + nz*yf + nz*ny*xf] = (1 - wx)*(1 - wy)*(1 - wz);
		W[u][zi + nz*yi + nz*ny*xi] = wx*wy*wz;
		W[u][zf + nz*yi + nz*ny*xi] = wx*wy*(1 - wz);
		W[u][zi + nz*yf + nz*ny*xi] = wx*(1 - wy)*wz;
		W[u][zf + nz*yf + nz*ny*xi] = wx*(1 - wy)*(1 - wz);

	}

	cin >> i;
    return 0;
}