function [cube] = cube(n)

% n nombre de punts

A(1,1) = 1;
A(2,1) = -1;
A(3,2) = 1;
A(4,2) = -1;
A(5,3) = 1;
A(6,3) = -1;

for i = 1:n
    a = floor(6*rand(1))+1;
    N(i,:) = A(a,:);
    for j = 1:3
        if A(a,j) == 0
            P(i,j) = rand(1);
        end
        if A(a,j) == 1
            P(i,j) = 1;
        end
        if A(a,j) == -1
            P(i,j) = 0;            
        end        
    end
end

cube(:,[1 2 3]) = P;
cube(:,[4 5 6]) = N;

end