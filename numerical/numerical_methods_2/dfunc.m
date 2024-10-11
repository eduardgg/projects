function sol = dfunc(x)
% Donat un punt x, dfunc(x) retorna el valor de la derivada de func()
% en el punt x.

global xe;
global ye;
n = length(xe);
dx1 = 0;
dy1 = 0;
dr1 = 0;

for i = 1:n
    dx1 = dx1 + (x(1)-xe(i))*(1-x(3)/((xe(i)-x(1))^2+(ye(i)-x(2))^2)^0.5);
    dy1 = dy1 + (x(2)-ye(i))*(1-x(3)/((xe(i)-x(1))^2+(ye(i)-x(2))^2)^0.5);
    dr1 = dr1 + x(3)-((xe(i)-x(1))^2+(ye(i)-x(2))^2)^0.5;
end
sol(1) = dx1;
sol(2) = dy1;
sol(3) = dr1;
end

