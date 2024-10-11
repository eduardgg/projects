x = [0 1 3 4 5 7];

[a b c d] = P1D(x);

X = 0:0.01:7;
Y = zeros (1, 701);


for i = 1:5
    
    A = [X(i)^3 X(i)^2 X(i) 1
    X(i+1)^3 X(i+1)^2 X(i+1) 1
    0 3*X(i)^2 2*X(i) 1
    0 3*X(i+1)^2 2*X(i+1) 1];
    
    vv = [f(X(i))
        f(X(i+1))
        df(X(i))
        df(X(i+1))
        ];
    
    ww = A\vv;
    
    a(i) = ww(1) - a(i);
    b(i) = ww(2) - b(i);
    c(i) = ww(3) - c(i);
    d(i) = ww(4) - d(i);
    
end




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