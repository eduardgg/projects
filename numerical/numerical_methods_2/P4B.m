x = [10 30 100 300 1000 3000 10000 30000 100000];

y = zeros (1, 9);

for i = 1:9
    
    [v, w] = P4(x(i));
    
    y(i) = w( x(i) + 1);
    
    
end

err = zeros (1, 8);

for i = 1:8
    err (i) = abs(  (y(i+1)-y(i))/y(i+1)   );
    
end

X = zeros(1,8);
Y = zeros(1,8);

for i = 1:8
    X(i) = log (x(i));
    Y(i) = log (err(i));


end

plot (X, Y);
