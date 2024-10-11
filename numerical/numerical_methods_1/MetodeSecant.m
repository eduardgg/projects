function [x] = secmet(a, b)
%Primero lo resuelvo por el mátodo de la secante. Este método tiene una
%convergencia "áurea".

%cuando tengamos un error de 1e-6 daremos la solución por buena.


x = a;
x1 = b;

while abs((x - x1)/x) > 1e-6
    m = (distancia(x1) - distancia(x))/(x1-x);
    x1 = x;
    x = x-(distancia(x)-600)/m;   
end





end

