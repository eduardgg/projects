function [ x ] = newmet( a )

%Ahora utilizaré el método de newton. Para ello hallaremos la derivada
%aproximándola con épsilons pequeñitos.

%cuando el error sea aceptable, daremos la solución por válida.

x = a;



while (abs((distancia(x)-600)/600) > 1e-6)
    
    m = (distancia(x+(1e-5))-distancia(x-(1e-5)) )/(2*(1e-5));
    x = x+(600-distancia(x))/m;
    
    
    
end




end

