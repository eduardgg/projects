function [esfera] = esfera(n)

% n nombre de punts

for i = 1:n
    A = 2*pi*rand(1);
    B = pi*(rand(1)-0.5);
    P(i,1) = cos(B)*cos(A);
    P(i,2) = cos(B)*sin(A);
    P(i,3) = sin(B);
end

esfera(:,[1 2 3]) = P;
esfera(:,[4 5 6]) = P;
    
end