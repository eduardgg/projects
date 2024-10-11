function [ v ] = errsec( a, b )


x = a;
x1 = b;
w=[];
while abs((x - x1)/x) > 1e-6
    m = (distancia(x1) - distancia(x))/(x1-x);
    x1 = x;
    x = x-(distancia(x)-600)/m;
    w = [w; x];
end

v = zeros (1, length(w)-1);
for i = 1:length(w)-1;
    v(i) = abs((w(i)-w(1+i))/w(i+1));
end



end

