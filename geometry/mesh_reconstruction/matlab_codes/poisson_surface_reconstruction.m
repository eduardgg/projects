function [V] = PSR (data)

% MAIN

% c = bottom-left-front must corner node
% n = number of sample points (and normal vectors)

% Valors per defecte:
% P = data(:, [1 2 3]);
% N = data(:, [4 5 6]);
% n = size(data,1);
% me = max(max(P)-min(P));
% h = me/20;
% c = min(P)-h;
% nx = 3+floor((max(P(:,1))-min(P(:,1)))/h);
% ny = 3+floor((max(P(:,2))-min(P(:,2)))/h);
% nz = 3+floor((max(P(:,3))-min(P(:,3)))/h);

% Valors millorats:
% P = data(:, [1 2 3]);
% N = data(:, [4 5 6]);
% n = size(data,1);
% me = max(max(P)-min(P));
% h = me/24;
% c = min(P)-2*h;
% nx = 5+floor((max(P(:,1))-min(P(:,1)))/h);
% ny = 5+floor((max(P(:,2))-min(P(:,2)))/h);
% nz = 5+floor((max(P(:,3))-min(P(:,3)))/h);

tic;

P = data(:, [1 2 3]);
N = data(:, [4 5 6]);
n = size(data,1);
me = max(max(P)-min(P));
h = me/20;
c = min(P)-2*h;
nx = 5+floor((max(P(:,1))-min(P(:,1)))/h);
ny = 5+floor((max(P(:,2))-min(P(:,2)))/h);
nz = 5+floor((max(P(:,3))-min(P(:,3)))/h);

% GRADIENT MATRIX

Dx = -eye((nx-1)*ny*nz, nx*ny*nz);
for i = 1:(nx-1)*ny*nz
   Dx(i,i+ny*nz) = 1; 
end

Dy = zeros(nx*(ny-1)*nz, nx*ny*nz);
for i = 1:nx
   for j = 1:(ny-1)*nz
      Dy((i-1)*(ny-1)*nz+j, (i-1)*ny*nz+j) = -1;
      Dy((i-1)*(ny-1)*nz+j, (i-1)*ny*nz+j+nz) = 1;
   end
end

Dz = zeros(nx*ny*(nz-1), nx*ny*nz);
for i = 1:nx*ny
    for j = 1:nz-1
        Dz((i-1)*(nz-1)+j, (i-1)*nz+j) = -1;
        Dz((i-1)*(nz-1)+j, (i-1)*nz+j+1) = 1;
    end
end

G = cat(1, Dx, Dy, Dz)/h;

% INTERPOLATION

Wx = zeros(n, (nx-1)*ny*nz);
Wy = zeros(n, nx*(ny-1)*nz);
Wz = zeros(n, nx*ny*(nz-1));

for u = 1:n
    
    if P(u,1) < c(1)+h/2
        stagx(u,1) = 0;
    elseif P(u,1) >= c(1)+(nx-3/2)*h
        stagx(u,1) = nx-1;
    else
        for i = 1:nx-2
            if  P(u,1) >= c(1)-h/2+h*i & P(u,1) < c(1)+h/2+h*i
                stagx(u,1) = i;
                break
            end
        end
    end

    if P(u,2) < c(2)+h/2
        stagy(u,2) = 0;
    elseif P(u,2) >= c(2)+(ny-3/2)*h
        stagy(u,2) = ny-1;
    else
        for i = 1:ny-2
            if  P(u,2) >= c(2)-h/2+h*i & P(u,2) < c(2)+h/2+h*i
                stagy(u,2) = i;
                break
            end
        end
    end    
    
    if P(u,3) < c(3)+h/2
        stagz(u,3) = 0;
    elseif P(u,3) >= c(3)+(nz-3/2)*h
        stagz(u,3) = nz-1;
    else
        for i = 1:nz-2
            if  P(u,3) >= c(3)-h/2+h*i & P(u,3) < c(3)+h/2+h*i
                stagz(u,3) = i;
                break
            end
        end
    end    
   
    
    for i = 0:nx-2
        if P(u,1) >= c(1)+i*h & P(u,1) < c(1)+(i+1)*h
            stagy(u,1) = i;
            stagz(u,1) = i;
            break
        end
    end
    
    for i = 0:ny-2
        if P(u,2) >= c(2)+i*h & P(u,2) < c(2)+(i+1)*h
            stagz(u,2) = i;
            stagx(u,2) = i;
            break
        end
    end
    
    for i = 0:nz-2
        if P(u,3) >= c(3)+i*h & P(u,3) < c(3)+(i+1)*h
            stagx(u,3) = i;
            stagy(u,3) = i;
            break
        end
    end
end



for u = 1:n
    
    wx = (c(1)-P(u,1)+h*(stagx(u,1)+1/2))/h;
    wy = (c(2)+h*(stagx(u,2)+1)-P(u,2))/h;
    wz = (c(3)+h*(stagx(u,3)+1)-P(u,3))/h;
        
    x0 = stagx(u,1)-1;
    y0 = stagx(u,2);
    z0 = stagx(u,3);
    
    x1 = x0+1;
    y1 = y0+1;
    z1 = z0+1;
    
    if stagx(u,1) < nx-1 
        
        Wx(u, 1+z0+nz*y0+nz*ny*x1) = (1-wx)*wy*wz;
        Wx(u, 1+z1+nz*y0+nz*ny*x1) = (1-wx)*wy*(1-wz);
        Wx(u, 1+z0+nz*y1+nz*ny*x1) = (1-wx)*(1-wy)*wz;
        Wx(u, 1+z1+nz*y1+nz*ny*x1) = (1-wx)*(1-wy)*(1-wz);
        
    end
        
    if stagx(u,1) > 0
        
        Wx(u, 1+z0+nz*y0+nz*ny*x0) = wx*wy*wz;
        Wx(u, 1+z1+nz*y0+nz*ny*x0) = wx*wy*(1-wz);
        Wx(u, 1+z0+nz*y1+nz*ny*x0) = wx*(1-wy)*wz;
        Wx(u, 1+z1+nz*y1+nz*ny*x0) = wx*(1-wy)*(1-wz);
    
    end
    
end

for u = 1:n
    
    wx = (c(1)+h*(stagy(u,1)+1)-P(u,1))/h;
    wy = (c(2)-P(u,2)+h*(stagy(u,2)+1/2))/h;
    wz = (c(3)+h*(stagy(u,3)+1)-P(u,3))/h;
        
    x0 = stagy(u,1);
    y0 = stagy(u,2)-1;
    z0 = stagy(u,3);
    
    x1 = x0+1;
    y1 = y0+1;
    z1 = z0+1;
    
    if stagy(u,2) < ny-1 
        
        Wy(u, 1+z0+nz*y1+nz*(ny-1)*x0) = wx*(1-wy)*wz;
        Wy(u, 1+z1+nz*y1+nz*(ny-1)*x0) = wx*(1-wy)*(1-wz);
        Wy(u, 1+z0+nz*y1+nz*(ny-1)*x1) = (1-wx)*(1-wy)*wz;
        Wy(u, 1+z1+nz*y1+nz*(ny-1)*x1) = (1-wx)*(1-wy)*(1-wz);
        
    end
        
    if stagy(u,2) > 0
        
        Wy(u, 1+z0+nz*y0+nz*(ny-1)*x0) = wx*wy*wz;
        Wy(u, 1+z1+nz*y0+nz*(ny-1)*x0) = wx*wy*(1-wz);
        Wy(u, 1+z0+nz*y0+nz*(ny-1)*x1) = (1-wx)*wy*wz;
        Wy(u, 1+z1+nz*y0+nz*(ny-1)*x1) = (1-wx)*wy*(1-wz);
        
    end
    
end

for u = 1:n
    
    wx = (c(1)+h*(stagz(u,1)+1)-P(u,1))/h;
    wy = (c(2)+h*(stagz(u,2)+1)-P(u,2))/h;
    wz = (c(3)-P(u,3)+h*(stagz(u,3)+1/2))/h;
        
    x0 = stagz(u,1);
    y0 = stagz(u,2);
    z0 = stagz(u,3)-1;
    
    x1 = x0+1;
    y1 = y0+1;
    z1 = z0+1;
    
    if stagz(u,3) < nz-1 
        
        Wz(u, 1+z1+(nz-1)*y0+(nz-1)*ny*x0) = wx*wy*(1-wz);
        Wz(u, 1+z1+(nz-1)*y0+(nz-1)*ny*x1) = (1-wx)*wy*(1-wz);
        Wz(u, 1+z1+(nz-1)*y1+(nz-1)*ny*x0) = wx*(1-wy)*(1-wz);
        Wz(u, 1+z1+(nz-1)*y1+(nz-1)*ny*x1) = (1-wx)*(1-wy)*(1-wz);
        
    end
        
    if stagz(u,3) > 0
        
        Wz(u, 1+z0+(nz-1)*y0+(nz-1)*ny*x0) = wx*wy*wz;
        Wz(u, 1+z0+(nz-1)*y0+(nz-1)*ny*x1) = (1-wx)*wy*wz;
        Wz(u, 1+z0+(nz-1)*y1+(nz-1)*ny*x0) = wx*(1-wy)*wz;
        Wz(u, 1+z0+(nz-1)*y1+(nz-1)*ny*x1) = (1-wx)*(1-wy)*wz;
    
    end
    
end

Nx = N(:, 1);
Ny = N(:, 2);
Nz = N(:, 3);

vx = (Wx') * Nx;
vy = (Wy') * Ny;
vz = (Wz') * Nz;

v = cat(1, vx, vy, vz);

% Ara aprofitem aquest programa per construir tamb� la matriu W
% d'interpolaci� trilineal a la "primary grid". Construir aquesta matriu �s
% molt m�s senzill que construir Wx, Wy i Wz. A m�s podem aprofitar els
% resultats trobats. En comptes de construir una matriu com stagx (que
% indica a quin cub per cada eix, i enumerats des de 0, es troba el punt u
% en l'staggered grid per les derivades en x, muntem la matriu prim amb la
% mateixa idea. Afortunadament, tenim aquesta relaci�:

% prim(:,1) = stagy(:,1) = stagz(:,1)
% prim(:,2) = stagz(:,2) = stagx(:,2)
% prim(:,3) = stagx(:,3) = stagy(:,3)

prim(:,1) = stagy(:,1);
prim(:,2) = stagz(:,2);
prim(:,3) = stagx(:,3);

W = zeros(n, nx*ny*nz);

for u = 1:n
    
    wx = (c(1)+h*(prim(u,1)+1)-P(u,1))/h;
    wy = (c(2)+h*(prim(u,2)+1)-P(u,2))/h;
    wz = (c(3)+h*(prim(u,3)+1)-P(u,3))/h;
        
    x0 = prim(u,1);
    y0 = prim(u,2);
    z0 = prim(u,3);
    
    x1 = x0+1;
    y1 = y0+1;
    z1 = z0+1;
    
    W(u, 1+z0+nz*y0+nz*ny*x1) = (1-wx)*wy*wz;
    W(u, 1+z1+nz*y0+nz*ny*x1) = (1-wx)*wy*(1-wz);
    W(u, 1+z0+nz*y1+nz*ny*x1) = (1-wx)*(1-wy)*wz;
    W(u, 1+z1+nz*y1+nz*ny*x1) = (1-wx)*(1-wy)*(1-wz);       
    W(u, 1+z0+nz*y0+nz*ny*x0) = wx*wy*wz;
    W(u, 1+z1+nz*y0+nz*ny*x0) = wx*wy*(1-wz);
    W(u, 1+z0+nz*y1+nz*ny*x0) = wx*(1-wy)*wz;
    W(u, 1+z1+nz*y1+nz*ny*x0) = wx*(1-wy)*(1-wz);
    
end

% Amb tot aix� ja tenim constru�da la matriu W, que ens servir� per
% calcular el iso-level "sigma", un dels �ltims passos del programa.

% POISSON SURFACE RECONSTRUCTION

% L'entrada del programa �s un .txt que cont� n files, cada una
% amb 6 nombres espaiats. Els tres primers corresponen a les coordenades
% x,y,z dels punts, i els tres seg�ents a les components del vector normal
% a la superf�cie en aquells punts. Per tal que tot funcioni b�, haurem
% d'emmagatzemar aquests valors en dues matrius: P, de dimensi� n x 3, que
% contindr� els punts, i N, de dimensi� n x 3, que contindr� els vectors
% normals.

% Per transformar-ho en una taula de valors i operar matricialment, usem
% l'opci� "Import Data" de Matlab.

% data �s la matriu de dimensi� n x 6 obtinguda de l' "import data".

% Mitjan�ant el m�tode dels m�nims quadrats (least squares method), obtenim
% el sistema lineal G'*G*g = G'*v. El problema d'aquest sistema �s que 
% sovint (sempre?) la matriu G'*G no �s invertible, i per tant no es pot
% resoldre. Per solucionar aquest problema, una opci� �s sumar una matriu
% diagonal d' "epsilons" a G'*G perqu� deixi de ser singular. D'aquesta
% manera s'obt� una soluci� bastant fidel a la real.

E = 1e-7;

g = (G'*G+E*eye(nx*ny*nz))\(G'*v);

% L'altra opci� per resoldre el sistema �s fent �s del CG Solver (Conjugate
% Gradient Solver) de Matlab, que simplement afegeix una restricci� a la
% soluci� per tal que la suma de les solucions sigui zero.

% Calculem l'iso-level "Sigma", fent servir la corresponent f�rmula:

Sigma = 1/n * ones(n,1)' * W * g; 

% Anem a construir la hipermatriu 3D (3D Array) de tamany nx�ny�nz que 
% cont� els valors del vector g de dimensi� nx*ny*nz ben classificats.

counter = 1;
for i = 1:nx
    for j = 1:ny
        for k = 1:nz
            V(i,j,k) = g(counter);
            counter = counter +1;
        end
    end
end

% TODO: Investigar la funci� "isosurface" (ajuda Matlab)
% Matlab function that implements an algorithm called "marching cubes"
% La funci� "patch" representa l'estructura S
% p = patch(isosurface(V, Sigma))
% El problema d'aquesta funci� �s que la isosuperf�cie no queda als punts
% correctes perqu� Matlab "no sap" on s�n aquests punts.
% Fem-ho col�locant la hipermatriu en els punts correctes de la malla:

[X, Y, Z] = meshgrid(c(2):h:c(2)+(ny-1)*h, c(1)+(nx-1)*h:-h:c(1), c(3):h:c(3)+(nz-1)*h);
p = patch(isosurface(X,Y,Z,V,Sigma))

% Donem color a les cares i v�rtexs de la malla:

p.FaceColor = 'yellow';
p.EdgeColor = 'black';
% axis tight
camlight 
lighting gouraud

% Finalment representem tamb� els vectors normals sobre la figura:
% hold on
% quiver3(P(:,1),P(:,2),P(:,3),N(:,1),N(:,2),N(:,3));

Temps = toc

end