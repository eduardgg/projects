function [ a, b, c, d ] = P1D( x )

n = length (x) -1;

sig = zeros (4, n+1);
sigg = zeros (4, n+1);
psi = zeros (4, n+1);
psii = zeros (4, n+1);


v = [1
    0
    0
    0];

for i = 1:n
    
    T = [ x(i)^3 x(i)^2 x(i) 1
    x(i+1)^3 x(i+1)^2 x(i+1) 1    
    3*x(i)^2 2*x(i) 1 0
    3*x(i+1)^2 2*x(i+1) 1 0
    ];
    
    w = T\v;
    
    sigg(1,i)=w(1);
    sigg(2,i)=w(2);
    sigg(3,i)=w(3);
    sigg(4,i)=w(4);
    
end



for i = 2:n+1
    
    T = [ x(i)^3 x(i)^2 x(i) 1
    x(i-1)^3 x(i-1)^2 x(i-1) 1    
    3*x(i)^2 2*x(i) 1 0
    3*x(i-1)^2 2*x(i-1) 1 0
    ];
    
    w = T\v;
    
    sig(1,i)=w(1);
    sig(2,i)=w(2);
    sig(3,i)=w(3);
    sig(4,i)=w(4);
end


v = [0
    0
    1
    0];


for i = 1:n
    
    T = [ x(i)^3 x(i)^2 x(i) 1
    x(i+1)^3 x(i+1)^2 x(i+1) 1    
    3*x(i)^2 2*x(i) 1 0
    3*x(i+1)^2 2*x(i+1) 1 0
    ];
    
    w = T\v;
    
    psii(1,i)=w(1);
    psii(2,i)=w(2);
    psii(3,i)=w(3);
    psii(4,i)=w(4);
end


for i = 2:n+1
    
    T = [ x(i)^3 x(i)^2 x(i) 1
    x(i-1)^3 x(i-1)^2 x(i-1) 1    
    3*x(i)^2 2*x(i) 1 0
    3*x(i-1)^2 2*x(i-1) 1 0
    ];
    
    w = T\v;
    
    psi(1,i)=w(1);
    psi(2,i)=w(2);
    psi(3,i)=w(3);
    psi(4,i)=w(4);
end




A = zeros(2*n +2, 2*n +2);

for i = 1:n
    
    A(i,i) = sigg(1,i)^2 * (x(i+1)^7-x(i)^7) /7;
    A(i,i) = A(i,i) + 2*sigg(1,i)*sigg(2,i)*(x(i+1)^6-x(i)^6) /6; 
    A(i,i) = A(i,i) + 2*sigg(1,i)*sigg(3,i)*(x(i+1)^5-x(i)^5) /5;
    A(i,i) = A(i,i) + sigg(2,i)*sigg(2,i)*(x(i+1)^5-x(i)^5) /5;
    A(i,i) = A(i,i) + 2*sigg(1,i)*sigg(4,i)*(x(i+1)^4-x(i)^4) /4;
    A(i,i) = A(i,i) + 2*sigg(3,i)*sigg(2,i)*(x(i+1)^4-x(i)^4) /4;
    A(i,i) = A(i,i) + 2*sigg(2,i)*sigg(4,i)*(x(i+1)^3-x(i)^3) /3;
    A(i,i) = A(i,i) + sigg(3,i)*sigg(3,i)*(x(i+1)^3-x(i)^3) /3;
    A(i,i) = A(i,i) + 2*sigg(3,i)*sigg(4,i)*(x(i+1)^2-x(i)^2) /2;
    A(i,i) = A(i,i) + sigg(4,i)*sigg(4,i)*(x(i+1)-x(i));
    
end



for i = 2:n+1
    
    A(i,i) = A(i,i) + sig(1,i)^2 * (x(i)^7-x(i-1)^7) /7;
    A(i,i) = A(i,i) + 2*sig(1,i)*sig(2,i)*(x(i)^6-x(i-1)^6) /6; 
    A(i,i) = A(i,i) + 2*sig(1,i)*sig(3,i)*(x(i)^5-x(i-1)^5) /5;
    A(i,i) = A(i,i) + sig(2,i)*sig(2,i)*(x(i)^5-x(i-1)^5) /5;
    A(i,i) = A(i,i) + 2*sig(1,i)*sig(4,i)*(x(i)^4-x(i-1)^4) /4;
    A(i,i) = A(i,i) + 2*sig(3,i)*sig(2,i)*(x(i)^4-x(i-1)^4) /4;
    A(i,i) = A(i,i) + 2*sig(2,i)*sig(4,i)*(x(i)^3-x(i-1)^3) /3;
    A(i,i) = A(i,i) + sig(3,i)*sig(3,i)*(x(i)^3-x(i-1)^3) /3;
    A(i,i) = A(i,i) + 2*sig(3,i)*sig(4,i)*(x(i)^2-x(i-1)^2) /2;
    A(i,i) = A(i,i) + sig(4,i)*sig(4,i)*(x(i)-x(i-1));
    
end




for i = 1:n
    
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + psii(1,i)^2 * (x(i+1)^7-x(i)^7) /7;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + 2*psii(1,i)*psii(2,i)*(x(i+1)^6-x(i)^6) /6; 
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + 2*psii(1,i)*psii(3,i)*(x(i+1)^5-x(i)^5) /5;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + psii(2,i)*psii(2,i)*(x(i+1)^5-x(i)^5) /5;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + 2*psii(1,i)*psii(4,i)*(x(i+1)^4-x(i)^4) /4;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + 2*psii(3,i)*psii(2,i)*(x(i+1)^4-x(i)^4) /4;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + 2*psii(2,i)*psii(4,i)*(x(i+1)^3-x(i)^3) /3;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + psii(3,i)*psii(3,i)*(x(i+1)^3-x(i)^3) /3;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + 2*psii(3,i)*psii(4,i)*(x(i+1)^2-x(i)^2) /2;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + psii(4,i)*psii(4,i)*(x(i+1)-x(i));
    
end


for i = 2:n+1
    
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + psi(1,i)^2 * (x(i)^7-x(i-1)^7) /7;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + 2*psi(1,i)*psi(2,i)*(x(i)^6-x(i-1)^6) /6; 
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + 2*psi(1,i)*psi(3,i)*(x(i)^5-x(i-1)^5) /5;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + psi(2,i)*psi(2,i)*(x(i)^5-x(i-1)^5) /5;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + 2*psi(1,i)*psi(4,i)*(x(i)^4-x(i-1)^4) /4;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + 2*psi(3,i)*psi(2,i)*(x(i)^4-x(i-1)^4) /4;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + 2*psi(2,i)*psi(4,i)*(x(i)^3-x(i-1)^3) /3;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + psi(3,i)*psi(3,i)*(x(i)^3-x(i-1)^3) /3;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + 2*psi(3,i)*psi(4,i)*(x(i)^2-x(i-1)^2) /2;
    A(i+n+1,i+n+1) = A(i+n+1,i+n+1) + psi(4,i)*psi(4,i)*(x(i)-x(i-1));
    
end

%ya he hecho los elementos de la diagonal


%el elemento de A(n+1, n+2) = 0 si n > 1


for i = 1:n
    
    A(i+1,i) = A(i+1,i) + sigg(1,i)*sig(1, i+1)*(x(i+1)^7-x(i)^7) /7;
    A(i+1,i) = A(i+1,i) + sigg(1,i)*sig(2,i+1)*(x(i+1)^6-x(i)^6) /6;
    A(i+1,i) = A(i+1,i) + sigg(2,i)*sig(1,i+1)*(x(i+1)^6-x(i)^6) /6;
    A(i+1,i) = A(i+1,i) + sigg(1,i)*sig(3,i+1)*(x(i+1)^5-x(i)^5) /5;
    A(i+1,i) = A(i+1,i) + sigg(3,i)*sig(1,i+1)*(x(i+1)^5-x(i)^5) /5;
    A(i+1,i) = A(i+1,i) + sigg(2,i)*sig(2,i+1)*(x(i+1)^5-x(i)^5) /5;
    A(i+1,i) = A(i+1,i) + sigg(1,i)*sig(4,i+1)*(x(i+1)^4-x(i)^4) /4;
    A(i+1,i) = A(i+1,i) + sigg(4,i)*sig(1,i+1)*(x(i+1)^4-x(i)^4) /4;
    A(i+1,i) = A(i+1,i) + sigg(3,i)*sig(2,i+1)*(x(i+1)^4-x(i)^4) /4;
    A(i+1,i) = A(i+1,i) + sigg(2,i)*sig(3,i+1)*(x(i+1)^4-x(i)^4) /4;
    A(i+1,i) = A(i+1,i) + sigg(4,i)*sig(2,i+1)*(x(i+1)^3-x(i)^3) /3;
    A(i+1,i) = A(i+1,i) + sigg(2,i)*sig(4,i+1)*(x(i+1)^3-x(i)^3) /3;
    A(i+1,i) = A(i+1,i) + sigg(3,i)*sig(3,i+1)*(x(i+1)^3-x(i)^3) /3;
    A(i+1,i) = A(i+1,i) + sigg(3,i)*sig(4,i+1)*(x(i+1)^2-x(i)^2) /2;
    A(i+1,i) = A(i+1,i) + sigg(4,i)*sig(3,i+1)*(x(i+1)^2-x(i)^2) /2;
    A(i+1,i) = A(i+1,i) + sigg(4,i)*sig(4,i+1)*(x(i+1)-x(i));
    
    A(i,i+1) = A(i+1,i);
    
end


for i = 1:n
    
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(1,i)*psi(1, i+1)*(x(i+1)^7-x(i)^7) /7;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(1,i)*psi(2,i+1)*(x(i+1)^6-x(i)^6) /6;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(2,i)*psi(1,i+1)*(x(i+1)^6-x(i)^6) /6;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(1,i)*psi(3,i+1)*(x(i+1)^5-x(i)^5) /5;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(3,i)*psi(1,i+1)*(x(i+1)^5-x(i)^5) /5;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(2,i)*psi(2,i+1)*(x(i+1)^5-x(i)^5) /5;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(1,i)*psi(4,i+1)*(x(i+1)^4-x(i)^4) /4;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(4,i)*psi(1,i+1)*(x(i+1)^4-x(i)^4) /4;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(3,i)*psi(2,i+1)*(x(i+1)^4-x(i)^4) /4;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(2,i)*psi(3,i+1)*(x(i+1)^4-x(i)^4) /4;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(4,i)*psi(2,i+1)*(x(i+1)^3-x(i)^3) /3;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(2,i)*psi(4,i+1)*(x(i+1)^3-x(i)^3) /3;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(3,i)*psi(3,i+1)*(x(i+1)^3-x(i)^3) /3;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(3,i)*psi(4,i+1)*(x(i+1)^2-x(i)^2) /2;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(4,i)*psi(3,i+1)*(x(i+1)^2-x(i)^2) /2;
    A(i+1+n+1,i+n+1) = A(i+1+n+1,i+n+1) + psii(4,i)*psi(4,i+1)*(x(i+1)-x(i));
    
    A(i+n+1,i+1+n+1) = A(i+1+n+1,i+n+1);
    
end



for i = 1:n
    
    A(i+n+1,i) = A(i+n+1,i) + psii(1,i)*sigg(1, i)*(x(i+1)^7-x(i)^7) /7;
    A(i+n+1,i) = A(i+n+1,i) + psii(1,i)*sigg(2,i)*(x(i+1)^6-x(i)^6) /6;
    A(i+n+1,i) = A(i+n+1,i) + psii(2,i)*sigg(1,i)*(x(i+1)^6-x(i)^6) /6;
    A(i+n+1,i) = A(i+n+1,i) + psii(1,i)*sigg(3,i)*(x(i+1)^5-x(i)^5) /5;
    A(i+n+1,i) = A(i+n+1,i) + psii(3,i)*sigg(1,i)*(x(i+1)^5-x(i)^5) /5;
    A(i+n+1,i) = A(i+n+1,i) + psii(2,i)*sigg(2,i)*(x(i+1)^5-x(i)^5) /5;
    A(i+n+1,i) = A(i+n+1,i) + psii(1,i)*sigg(4,i)*(x(i+1)^4-x(i)^4) /4;
    A(i+n+1,i) = A(i+n+1,i) + psii(4,i)*sigg(1,i)*(x(i+1)^4-x(i)^4) /4;
    A(i+n+1,i) = A(i+n+1,i) + psii(3,i)*sigg(2,i)*(x(i+1)^4-x(i)^4) /4;
    A(i+n+1,i) = A(i+n+1,i) + psii(2,i)*sigg(3,i)*(x(i+1)^4-x(i)^4) /4;
    A(i+n+1,i) = A(i+n+1,i) + psii(4,i)*sigg(2,i)*(x(i+1)^3-x(i)^3) /3;
    A(i+n+1,i) = A(i+n+1,i) + psii(2,i)*sigg(4,i)*(x(i+1)^3-x(i)^3) /3;
    A(i+n+1,i) = A(i+n+1,i) + psii(3,i)*sigg(3,i)*(x(i+1)^3-x(i)^3) /3;
    A(i+n+1,i) = A(i+n+1,i) + psii(3,i)*sigg(4,i)*(x(i+1)^2-x(i)^2) /2;
    A(i+n+1,i) = A(i+n+1,i) + psii(4,i)*sigg(3,i)*(x(i+1)^2-x(i)^2) /2;
    A(i+n+1,i) = A(i+n+1,i) + psii(4,i)*sigg(4,i)*(x(i+1)-x(i));
    
    A(i,i+n+1) = A(i+n+1,i);
    
end



for i = 2:n+1
    
    A(i+n+1,i) = A(i+n+1,i) + psi(1,i)*sig(1, i)*(x(i)^7-x(i-1)^7) /7;
    A(i+n+1,i) = A(i+n+1,i) + psi(1,i)*sig(2,i)*(x(i)^6-x(i-1)^6) /6;
    A(i+n+1,i) = A(i+n+1,i) + psi(2,i)*sig(1,i)*(x(i)^6-x(i-1)^6) /6;
    A(i+n+1,i) = A(i+n+1,i) + psi(1,i)*sig(3,i)*(x(i)^5-x(i-1)^5) /5;
    A(i+n+1,i) = A(i+n+1,i) + psi(3,i)*sig(1,i)*(x(i)^5-x(i-1)^5) /5;
    A(i+n+1,i) = A(i+n+1,i) + psi(2,i)*sig(2,i)*(x(i)^5-x(i-1)^5) /5;
    A(i+n+1,i) = A(i+n+1,i) + psi(1,i)*sig(4,i)*(x(i)^4-x(i-1)^4) /4;
    A(i+n+1,i) = A(i+n+1,i) + psi(4,i)*sig(1,i)*(x(i)^4-x(i-1)^4) /4;
    A(i+n+1,i) = A(i+n+1,i) + psi(3,i)*sig(2,i)*(x(i)^4-x(i-1)^4) /4;
    A(i+n+1,i) = A(i+n+1,i) + psi(2,i)*sig(3,i)*(x(i)^4-x(i-1)^4) /4;
    A(i+n+1,i) = A(i+n+1,i) + psi(4,i)*sig(2,i)*(x(i)^3-x(i-1)^3) /3;
    A(i+n+1,i) = A(i+n+1,i) + psi(2,i)*sig(4,i)*(x(i)^3-x(i-1)^3) /3;
    A(i+n+1,i) = A(i+n+1,i) + psi(3,i)*sig(3,i)*(x(i)^3-x(i-1)^3) /3;
    A(i+n+1,i) = A(i+n+1,i) + psi(3,i)*sig(4,i)*(x(i)^2-x(i-1)^2) /2;
    A(i+n+1,i) = A(i+n+1,i) + psi(4,i)*sig(3,i)*(x(i)^2-x(i-1)^2) /2;
    A(i+n+1,i) = A(i+n+1,i) + psi(4,i)*sig(4,i)*(x(i)-x(i-1));
    
    A(i,i+n+1) = A(i+n+1,i);
    
end



for i = 1:n
    
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(1,i)*sig(1,i+1)*(x(i+1)^7-x(i)^7) /7;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(1,i)*sig(2,i+1)*(x(i+1)^6-x(i)^6) /6;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(2,i)*sig(1,i+1)*(x(i+1)^6-x(i)^6) /6;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(1,i)*sig(3,i+1)*(x(i+1)^5-x(i)^5) /5;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(3,i)*sig(1,i+1)*(x(i+1)^5-x(i)^5) /5;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(2,i)*sig(2,i+1)*(x(i+1)^5-x(i)^5) /5;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(1,i)*sig(4,i+1)*(x(i+1)^4-x(i)^4) /4;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(4,i)*sig(1,i+1)*(x(i+1)^4-x(i)^4) /4;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(3,i)*sig(2,i+1)*(x(i+1)^4-x(i)^4) /4;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(2,i)*sig(3,i+1)*(x(i+1)^4-x(i)^4) /4;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(4,i)*sig(2,i+1)*(x(i+1)^3-x(i)^3) /3;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(2,i)*sig(4,i+1)*(x(i+1)^3-x(i)^3) /3;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(3,i)*sig(3,i+1)*(x(i+1)^3-x(i)^3) /3;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(3,i)*sig(4,i+1)*(x(i+1)^2-x(i)^2) /2;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(4,i)*sig(3,i+1)*(x(i+1)^2-x(i)^2) /2;
    A(i+n+1,i+1) = A(i+n+1,i+1) + psii(4,i)*sig(4,i+1)*(x(i+1)-x(i));
    
    A(i+1,i+n+1) = A(i+n+1,i+1);
    
end


for i = 1:n
    
    A(i+n+2,i) = A(i+n+2,i) + psi(1,i+1)*sigg(1,i)*(x(i+1)^7-x(i)^7) /7;
    A(i+n+2,i) = A(i+n+2,i) + psi(1,i+1)*sigg(2,i)*(x(i+1)^6-x(i)^6) /6;
    A(i+n+2,i) = A(i+n+2,i) + psi(2,i+1)*sigg(1,i)*(x(i+1)^6-x(i)^6) /6;
    A(i+n+2,i) = A(i+n+2,i) + psi(1,i+1)*sigg(3,i)*(x(i+1)^5-x(i)^5) /5;
    A(i+n+2,i) = A(i+n+2,i) + psi(3,i+1)*sigg(1,i)*(x(i+1)^5-x(i)^5) /5;
    A(i+n+2,i) = A(i+n+2,i) + psi(2,i+1)*sigg(2,i)*(x(i+1)^5-x(i)^5) /5;
    A(i+n+2,i) = A(i+n+2,i) + psi(1,i+1)*sigg(4,i)*(x(i+1)^4-x(i)^4) /4;
    A(i+n+2,i) = A(i+n+2,i) + psi(4,i+1)*sigg(1,i)*(x(i+1)^4-x(i)^4) /4;
    A(i+n+2,i) = A(i+n+2,i) + psi(3,i+1)*sigg(2,i)*(x(i+1)^4-x(i)^4) /4;
    A(i+n+2,i) = A(i+n+2,i) + psi(2,i+1)*sigg(3,i)*(x(i+1)^4-x(i)^4) /4;
    A(i+n+2,i) = A(i+n+2,i) + psi(4,i+1)*sigg(2,i)*(x(i+1)^3-x(i)^3) /3;
    A(i+n+2,i) = A(i+n+2,i) + psi(2,i+1)*sigg(4,i)*(x(i+1)^3-x(i)^3) /3;
    A(i+n+2,i) = A(i+n+2,i) + psi(3,i+1)*sigg(3,i)*(x(i+1)^3-x(i)^3) /3;
    A(i+n+2,i) = A(i+n+2,i) + psi(3,i+1)*sigg(4,i)*(x(i+1)^2-x(i)^2) /2;
    A(i+n+2,i) = A(i+n+2,i) + psi(4,i+1)*sigg(3,i)*(x(i+1)^2-x(i)^2) /2;
    A(i+n+2,i) = A(i+n+2,i) + psi(4,i+1)*sigg(4,i)*(x(i+1)-x(i));
    
    A(i,i+n+2) = A(i+n+2,i);
    
end

%Ya tengo la matriz A
%Ahora a integrar


esc = zeros(2*n + 2, 1);

for i = 1:n
    %100 subintervalos
    h = x(i+1)- x(i);
    h = h/100;
    sum = 0;
    summ = 0;
    for j = 1:100
        k = x(i) + (j-1)*h;
        kh = k+h;
        sum = sum + h*( f(k)*(sigg(1,i)*k^3 + sigg(2,i)*k^2 + sigg(3,i)*k + sigg(4,i)))/2;
        sum = sum + h*( f(kh)*(sigg(1,i)*kh^3 + sigg(2,i)*kh^2 + sigg(3,i)*kh + sigg(4,i)))/2;
        summ = summ + h*( f(k)*(psii(1,i)*k^3 + psii(2,i)*k^2 + psii(3,i)*k + psii(4,i)))/2;
        summ = summ + h*( f(kh)*(psii(1,i)*kh^3 + psii(2,i)*kh^2 + psii(3,i)*kh + psii(4,i)))/2;
    end
    esc(i) = sum;
    esc(i+n+1) = summ;
    
end



for i = 2:n+1
    %100 subintervalos
    h = x(i)- x(i-1);
    h = h/100;
    sum = 0;
    summ = 0;
    for j = 1:100
        k = x(i-1) + (j-1)*h;
        kh = k+h;
        sum = sum + h*( f(k)*(sig(1,i)*k^3 + sig(2,i)*k^2 + sig(3,i)*k + sig(4,i)))/2;
        sum = sum + h*( f(kh)*(sig(1,i)*kh^3 + sig(2,i)*kh^2 + sig(3,i)*kh + sig(4,i)))/2;
        summ = summ + h*( f(k)*(psi(1,i)*k^3 + psi(2,i)*k^2 + psi(3,i)*k + psi(4,i)))/2;
        summ = summ + h*( f(kh)*(psi(1,i)*kh^3 + psi(2,i)*kh^2 + psi(3,i)*kh + psi(4,i)))/2;
    end
    esc(i) = esc(i) + sum;
    esc(i+n+1) = esc(i+n+1) + summ;
    
end


a = zeros(1, n);
b = zeros(1, n);
c = zeros(1, n);
d = zeros(1, n);


vect = A\esc;


for i = 1:n
    
    a(i) = sigg(1,i)*vect(i) + sig(1, i+1)*vect(i+1) + psii(1,i)*vect(i+n+1) + psi(1, i+1)*vect(i+n+2);
    b(i) = sigg(2,i)*vect(i) + sig(2, i+1)*vect(i+1) + psii(2,i)*vect(i+n+1) + psi(2, i+1)*vect(i+n+2);
    c(i) = sigg(3,i)*vect(i) + sig(3, i+1)*vect(i+1) + psii(3,i)*vect(i+n+1) + psi(3, i+1)*vect(i+n+2);
    d(i) = sigg(4,i)*vect(i) + sig(4, i+1)*vect(i+1) + psii(4,i)*vect(i+n+1) + psi(4, i+1)*vect(i+n+2);
    
    
end



end

