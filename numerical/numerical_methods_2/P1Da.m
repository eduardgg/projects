x = [0 1 3 4 5 7];

[a b c d] = P1D(x);

X = 0:0.01:7;
Y = zeros (1, 701);


for i = 1:100
    
    Y(i) = a(1)*X(i)^3 + b(1)*X(i)^2 + c(1)*X(i) + d(1);
    
end



for i = 101:300
    
    Y(i) = a(2)*X(i)^3 + b(2)*X(i)^2 + c(2)*X(i) + d(2);
    
end



for i = 301:400
    
    Y(i) = a(3)*X(i)^3 + b(3)*X(i)^2 + c(3)*X(i) + d(3);
    
end



for i = 401:500
    
    Y(i) = a(4)*X(i)^3 + b(4)*X(i)^2 + c(4)*X(i) + d(4);
    
end



for i = 501:701
    
    Y(i) = a(5)*X(i)^3 + b(5)*X(i)^2 + c(5)*X(i) + d(5);
    
end

plot (X, Y);
