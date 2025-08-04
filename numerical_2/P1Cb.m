x = [0 1 3 4 5 7];

y = P1BC(x);

for i = 1:6
    y(i) = f(x(i)) - y(i);
end


plot (x, y);