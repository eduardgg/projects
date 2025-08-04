function [ x ] = newmet( a )

%Ahora utilizar� el m�todo de newton. Para ello hallaremos la derivada
%aproxim�ndola con �psilons peque�itos.

%cuando el error sea aceptable, daremos la soluci�n por v�lida.

x = a;



while (abs((distancia(x)-600)/600) > 1e-6)
    
    m = (distancia(x+(1e-5))-distancia(x-(1e-5)) )/(2*(1e-5));
    x = x+(600-distancia(x))/m;
    
    
    
end




end

