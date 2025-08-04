function S = func(x)
% Donat un punt x, func(x) retorna el valor de la funcio en el punt x.

global xe;
global ye;
n = length(xe);
s1 = 0;

for i = 1:n
    s1 = s1 + (((x(1)-xe(i))^2+(x(2)-ye(i))^2)^0.5-x(3))^2;
end
S = s1;
end

