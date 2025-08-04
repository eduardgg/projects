function J = jake(x, c)
% Funcio que calcula la jacobiana de forma aproximada

C = c;
n = length(x);
J = zeros(n);
delta = 1e-4;

for j = 1:n 
    d = zeros(1,n);
    d(j) = delta;
    J(:,j) = ((sist(x+d, C)-sist(x-d, C))/(2*delta));
end

end

