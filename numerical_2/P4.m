function [ v , w ] = P4( n )

%n es el número de intervalos

deltat = 10/n;
R = 0.00132;
g = 9.8;

w = zeros (1, n+1);

v = zeros (1, n+1);

xp = [100*cos(pi/4) 100*sin(pi/4) 0 0];

xp(3) = -R*xp(1)*sqrt(xp(1)*xp(1) + xp(2)*xp(2));
xp(4) = -R*xp(2)*sqrt(xp(1)*xp(1) + xp(2)*xp(2)) - g;


for i = 1:n
    
   v(i+1) = v(i) + deltat*xp(1);
   w(i+1) = w(i) + deltat*xp(2); 
    
   xp(1) = xp(1) + deltat*xp(3); 
   xp(2) = xp(2) + deltat*xp(4); 
   xp(3) = -R*xp(1)*sqrt(xp(1)*xp(1) + xp(2)*xp(2));
   xp(4) = -R*xp(2)*sqrt(xp(1)*xp(1) + xp(2)*xp(2)) - g; 
    
end



end

