function [ v ] = P1BC(x)

n = length(x) - 1;


%la matriz A sera la del producto escalar
A = zeros (n+1, n+1);

A(1,1) = (x(2) - x(1))/3;
A(n+1, n+1) = (x(n+1) - x(n))/3;







t = (x(2).^3)/3;
t = t - 0.5 * (x(1)+x(2)) * x(2) * x(2);
t = t + x(1)*x(2)*x(2);

tt = (x(1).^3)/3;
tt = tt - 0.5 * (x(1)+x(2)) * x(1) * x(1);
tt = tt + x(1)*x(2)*x(1);

A(1, 2) = (tt-t) / ((x(2)-x(1))*(x(2)-x(1)));
A(2, 1) = (tt-t)/ ((x(2)-x(1))*(x(2)-x(1)));


if n > 2
    
    for i = 2:n
       A(i,i) =  (x(i+1) - x(i-1))/3;
        t = (x(i+1).^3)/3;
        t = t - 0.5 * (x(i)+x(i+1)) * x(i+1) * x(i+1);
        t = t + x(i)*x(i+1)*x(i+1);

        tt = (x(i).^3)/3;
        tt = tt - 0.5 * (x(i)+x(i+1)) * x(i) * x(i);
        tt = tt + x(i)*x(i+1)*x(i);

       A(i, i+1) = (tt-t)/ ((x(1+i)-x(i))*(x(1+i)-x(i)));
       A(i+1, i) = (tt-t) / ((x(1+i)-x(i))*(x(1+i)-x(i))); 
    end
    
    
    
    
end


% hare el metodo del trapecio

% "f" es una función que nos la dan y queremos hallar su spline

b = zeros (n+1, 1);
for i = 1:n
    
   
    
    %hago la integral con la formula del trapecio
    h = x(i+1) - x(i);
    h = h/100;
    
   for j = 1:100
       
       sum = h*( (j-1)*f(x(i) + j*h -h) + j*f(x(i) + j*h) ) / 200;
       
       b(i+1) = b(i+1) + sum;
                     
       
   end
    
    
   for j = 1:100
       
      sum = h*( (101-j)*f(x(i) + j*h -h) + (100-j)*f(x(i) + j*h) ) / 200;
       
      b(i) = b(i) + sum; 
      
   end
   
    
    
end

v = A\b;

end



