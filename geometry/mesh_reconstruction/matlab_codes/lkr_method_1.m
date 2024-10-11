
function [] = lkr1(data)

P = data(:, [1 2 3]);
N = data(:, [4 5 6]);
n = size(data,1);
me = max(max(P)-min(P));
h = me/24;
c = min(P)-h;
nx = 3+floor((max(P(:,1))-min(P(:,1)))/h);
ny = 3+floor((max(P(:,2))-min(P(:,2)))/h);
nz = 3+floor((max(P(:,3))-min(P(:,3)))/h);

syms x y z;
num = 0;
den = 0;
p = [x y z];

for u = 1:n
    pu = P(u,:);
    nu = N(u,:);
    hi = 0.01;
    fi = (1 - norm(p - pu)/(hi^2))^4;
    num = num + fi * nu * (p - pu)';
    den = den + fi;
end

f = num/den;

for i = 1:nx
    for j = 1:ny
        for k = 1:nz
            V(i,j,k) = subs(f, [x y z], c+[(i-1)*h,(j-1)*h,(k-1)*h]);
        end
    end
end

p = patch(isosurface(V, 0))

p.FaceColor = 'yellow';
p.EdgeColor = 'black';
axis tight
camlight 
lighting gouraud

end