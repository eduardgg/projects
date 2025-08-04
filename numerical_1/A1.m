v = 0:0.1:1.5;
w = zeros (1, 16);

for i = 1:16
    w(i) = distancia(v(i));
end

% distancia(0) = 953.5830, pero para valores de x próximos a 0,
% distancia(x) es próximo a 0, por ejemplo, distancia(0.0001) = 0.2938.

w

% por otra parte si nos fijamos en los valores de w, el quinto elemento y
% el undécimo elemento son menores que 600, y el sexto y décimo elemento
% son mayores que 600. Es decir, que tendrá el problema dos soluciones,
% una entre 0.4 y 0.5, y la otra entre 0.9 y 1.



