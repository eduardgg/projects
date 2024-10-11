% 2.2. Newton aproximat

clear all 
close all
format long

% DADES INICIALS

X = [1,1];
C = 2.1; % C = (L*O^2)/g

% METODE NEWTON RAPHSON AMB MATRIU JACOBIANA APROXIMADA

tic

it = 0;
tol = 1e-14;
itmax = 20;

vx = [X];
sx = sist(X, C);
ssx = [norm(sist(X, C))];

while and((norm(sist(X, C)) > tol), (it < itmax));   
    A = - jake(X, C)\sist(X, C)';
    X = X + A';

    it = it + 1;

    vx = [vx; X];
end

toc

it
X
X*180/pi
vx;

errel = ones(length(vx), 1);

for i = 1:length(vx)
    errel(i) = norm(vx(i,:)-X); 
end

errel

% REPRESENTACIO GRAFICA

vv = [1:1:length(errel)];
semilogy(vv, errel), grid on;
title('Error Relatiu')


