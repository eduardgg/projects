function [] = rlkr1(data)

% CANVIAR ELS VALORS
% h ha de ser me/24 (almenys per PSR és un bon valor)
% hi = k*dmit, on k és un valor entre 1,4 i 4.

P = data(:, [1 2 3]);
N = data(:, [4 5 6]);
n = size(data,1);
me = max(max(P)-min(P));
h = me/20;
c = min(P)-2*h;
nx = 5+floor((max(P(:,1))-min(P(:,1)))/h);
ny = 5+floor((max(P(:,2))-min(P(:,2)))/h);
nz = 5+floor((max(P(:,3))-min(P(:,3)))/h);

SigmaR = 0.5;
SigmaN = 0.5;  

for i = 1:nx
    for j = 1:ny
        for k = 1:nz
            
            num = 0;
            den = 0;
            p = c+[(i-1)*h,(j-1)*h,(k-1)*h];
            [v d] = knnsearch(P,p,'k',6);
            dmit = d*ones(6,1)/6;
            hi = 2*dmit;
            
            % Punt inicial
            for u = 1:n
                pu = P(u,:);
                nu = N(u,:);
                base = 1 - (norm(p - pu)/hi)^2;
                fi = max(base,0)^4;
                num = num + fi * nu * (p - pu)';
                den = den + fi;
            end
            f(1) = num / den;
            
            % Iteracions
            for iter = 2:4
                for u = 1:n
                    pu = P(u,:);
                    nu = N(u,:);
                    base = max(1 - (norm(p - pu)/hi)^2,0);
                    fi = base^4;
                    r(iter-1,u) = f(iter-1) - nu * (p - pu)';
                    w1 = exp(-(r(iter-1,u)/(SigmaR*hi))^2);
                    num = num + fi * w1 * nu * (p - pu)';
                    den = den + fi * w1;
                end
                f(iter) = num / den;
            end
            
            V(i,j,k) = f(4);
            clear f r
            
        end    
    end
end

% La següent expressió té sidilla. Coses del Matlab.
[X, Y, Z] = meshgrid(c(2):h:c(2)+(ny-1)*h, c(1)+(nx-1)*h:-h:c(1), c(3):h:c(3)+(nz-1)*h);  
P = patch(isosurface(X,Y,Z,V,0))
P.FaceColor = 'yellow';
P.EdgeColor = 'black';
axis tight
camlight 
lighting gouraud

end