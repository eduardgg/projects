
function [] = lkr3(data)

% CANVIAR ELS VALORS
% h ha de ser me/24 (almenys per PSR �s un bon valor)
% Isovalor sembla que dep�n de cada superf�cie (?)
% hi ha de ser algun valor no gaire clar, i que dep�n localment.

P = data(:, [1 2 3]);
N = data(:, [4 5 6]);
n = size(data,1);
me = max(max(P)-min(P));
h = me/20;
c = min(P)-h;
nx = 3+floor((max(P(:,1))-min(P(:,1)))/h);
ny = 3+floor((max(P(:,2))-min(P(:,2)))/h);
nz = 3+floor((max(P(:,3))-min(P(:,3)))/h);

hi = 0.5;

for i = 1:nx
    for j = 1:ny
        for k = 1:nz
            num = 0;
            den = 0;
            p = c+[(i-1)*h,(j-1)*h,(k-1)*h];
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

P = patch(isosurface(V, 0))
P.FaceColor = 'yellow';
P.EdgeColor = 'black';
axis tight
camlight 
lighting gouraud

end