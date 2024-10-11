
function [] = lkr4(data)

% CANVIAR ELS VALORS
% h ha de ser me/24 (almenys per PSR �s un bon valor)
% hi = k*dmit, on k �s un valor entre 1,4 i 4.

tic;

P = data(:, [1 2 3]);
N = data(:, [4 5 6]);
n = size(data,1);
me = max(max(P)-min(P));
h = me/20;
c = min(P)-2*h;
nx = 5+floor((max(P(:,1))-min(P(:,1)))/h);
ny = 5+floor((max(P(:,2))-min(P(:,2)))/h);
nz = 5+floor((max(P(:,3))-min(P(:,3)))/h);

for i = 1:nx
    for j = 1:ny
        for k = 1:nz
            num = 0;
            den = 0;
            p = c+[(i-1)*h,(j-1)*h,(k-1)*h];
            [v d] = knnsearch(P,p,'k',6);
            dmit = d*ones(6,1)/6;
            hi = 2*dmit;
            for u = 1:n
                pu = P(u,:);
                nu = N(u,:);
                fi = max(1 - (norm(p - pu)/hi)^2,0)^4;
                num = num + fi * nu * (p - pu)';
                den = den + fi;
            end
            f = num / den;
            V(i,j,k) = f;
        end
    end
end

[X, Y, Z] = meshgrid(c(2):h:c(2)+(ny-1)*h, c(1)+(nx-1)*h:-h:c(1), c(3):h:c(3)+(nz-1)*h);  
P = patch(isosurface(X,Y,Z,V,0))
P.FaceColor = 'yellow';
P.EdgeColor = 'black';
axis tight
camlight 
lighting gouraud

Temps = toc

end