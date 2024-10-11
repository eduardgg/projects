clear all 
close all
format long

% CONDICIONS INICIALS (en aquest cas punt inicial i matriu inicial)

X = [1,1];
S = jacob(X);

% METODE BROYDEN

it = 1;
tol = 1e-14;
itmax = 30;

% PRIMERA ITERACIO:

tic

Xa = X;
A = - jacob(X)\sist(X)';
X = X + A'; 
vx = [Xa; X];
sx = [sist(Xa); sist(X)];
ssx = [norm(sist(Xa)); norm(sist(X))];

% BUCLE

while and((norm(sist(X)) > tol), (it < itmax));   

S = broyden(S, X, Xa);
A = - S\sist(X)'; 

Xa = X;
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
