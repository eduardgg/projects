function [ x ] = bismet(a, b)
%intentamos buscar la soluci�n al problema, es decir, buscar la x tal que
%distancia(x) = 600, o lo que es lo mismo, resolver la ecuaci�n 
%distancia(x)- 600 = 0.
%cuando tengamos un error inferior a 1e-6 daremos por v�lida la soluci�n.

x = 0;
x1 = a;
x2 = b;
x = (x1+x2)/2;

while (abs((x2-x1)/x2) > 1e-6)
    if ((distancia(x1)-600)*(distancia((x1+x2)/2)-600) > 0)
        x = (x1+x2)/2;
        x1 = (x1+x2)/2;
    elseif ((distancia(x1)-600)*(distancia((x1+x2)/2)-600) < 0)
        x = (x1+x2)/2;
        x2 = (x1+x2)/2;
    else
        x = (x1+x2)/2;
        x1 = (x1+x2)/2;
        x2 = (x1+x2)/2;
    end
    
    
    
end


end

