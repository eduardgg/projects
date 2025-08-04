function [ v ] = errnew( a )
x = a;

w = [];

while (abs((distancia(x)-600)/600) > 1e-6)
    
    m = (distancia(x+(1e-5))-distancia(x-(1e-5)) )/(2*(1e-5));
    x = x+(600-distancia(x))/m;
    w = [w; x];
    
    
end

v = zeros (1, length(w)-1);
for i = 1:length(w)-1;
    v(i) = abs((w(i)-w(1+i))/w(i+1));
end


end

