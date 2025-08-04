function [ v ] = errbis( a,b )
x = 0;
x1 = a;
x2 = b;
x = (x1+x2)/2;

w = [];

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
    
    w = [w; x];
    
end

v = zeros (1, length(w)-1);
for i = 1:length(w)-1;
    v(i) = abs((w(i)-w(1+i))/w(i+1));
end

end

