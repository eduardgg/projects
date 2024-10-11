function S = broyden(M, X1, X0)

u = sist(X1)/((X1-X0)*(X1-X0)');
v = X1-X0;

S = M + u*v';
end

