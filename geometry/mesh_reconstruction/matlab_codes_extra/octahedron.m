function [octahedron] = octahedron(n)

% n nombre de punts

A([1 2 3 4],1) = 1;
A([5 6 7 8],1) = -1;
A([1 2 5 6],2) = 1;
A([3 4 7 8],2) = -1;
A([1 3 5 7],3) = 1;
A([2 4 6 8],3) = -1;

for i = 1:n
   a = floor(8*rand(1))+1;
   N(i,:) = A(a,:)/sqrt(3);
   p = [A(a,1) 0 0];
   q = [0 A(a,2) 0];
   r = [0 0 A(a,3)];
   f = rand(1);
   g = rand(1);
   if f+g>1
       f = 1-f;
       g = 1-g;
   end
   P(i,:) = p + f*(q-p) + g*(r-p);
%  P(i,:) = (1-f-g)*p + f*q + g*r;
end

octahedron(:,[1 2 3]) = P;
octahedron(:,[4 5 6]) = N;

end