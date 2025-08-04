function [x] = secmet(a, b)
%Primero lo resuelvo por el m�todo de la secante. Este m�todo tiene una
%convergencia "�urea".

%cuando tengamos un error de 1e-6 daremos la soluci�n por buena.


x = a;
x1 = b;

while abs((x - x1)/x) > 1e-6
    m = (distancia(x1) - distancia(x))/(x1-x);
    x1 = x;
    x = x-(distancia(x)-600)/m;   
end





end

