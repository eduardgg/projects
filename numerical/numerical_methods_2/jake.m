function J = jake(x)
% Donat un vector x, retorna la matriu Jacobiana aproximada en 
% aquest punt.

n = length(x);
J = zeros(n);
delta = 1e-3;

for j = 1:n 
    d = zeros(1,n);
    d(j) = delta;
    J(:,j) = ((dfunc(x+d)-dfunc(x-d))/(2*delta));
end
end

