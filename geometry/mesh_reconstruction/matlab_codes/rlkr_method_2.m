function [] = rlkr2(data)

% CANVIAR ELS VALORS
% h ha de ser me/24 (almenys per PSR és un bon valor)
% hi = k*dmit, on k és un valor entre 1,4 i 4.

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

SigmaR = 0.5;
SigmaN = 0.5;  

for i = 1:nx
    for j = 1:ny
        for k = 1:nz

            p = c+[(i-1)*h,(j-1)*h,(k-1)*h];
            [v d] = knnsearch(P,p,'k',6);
            dmit = d*ones(6,1)/6;
            hi = 2*dmit;
            
            % Punt inicial
            S1 = 0;
            S2 = 0;
            S3 = 0;
            num = 0;
            den = 0;
            for u = 1:n
                base = max(1 - (norm(p - P(u,:))/hi)^2,0);
                fi(u) = base^4;
                gradfi(u,:) = -8 * base^3 * (p - P(u,:)) / hi^2;
                num = num + fi(u) * N(u,:) * (p - P(u,:))';
                den = den + fi(u);
            end
            f = num / den;
            % Càlcul de les sumes S1, S2, S3
            for u = 1:n
                S1 = S1 + fi(u) * N(u,:);
                S2 = S2 + gradfi(u,:) * (N(u,:) * (p - P(u,:))' - f);
                S3 = S3 + fi(u);
            end
            clear gradfi fi
            
            % Iteracions
            for iter = 1:3
                gradf = (S1 + S2)/S3;
                S1 = 0;
                S2 = 0;
                S3 = 0;
                num = 0;
                den = 0;
                for u = 1:n
                    base = max(1 - (norm(p - P(u,:))/hi)^2,0);
                    fi(u) = base^4;
                    gradfi(u,:) = -8 * base^3 * (p - P(u,:)) / hi^2;
                    r = f - N(u,:) * (p - P(u,:))';
                    Delta = norm(gradf - N(u,:));
                    w1 = exp(-(r/(SigmaR*hi))^2);
                    w2 = exp(-(Delta/SigmaN)^2);
                    w(u) = w1 * w2;
                    num = num + fi(u) * w(u) * N(u,:) * (p - P(u,:))';
                    den = den + fi(u) * w(u);
                end
                f = num / den;
                % Càlcul de les sumes S1, S2, S3
                for u = 1:n
                    S1 = S1 + w(u) * fi(u) * N(u,:);
                    S2 = S2 + w(u) * gradfi(u,:) * (N(u,:) * (p - P(u,:))' - f);
                    S3 = S3 + w(u) * fi(u);
                end
                clear gradfi fi w
            end
            
            V(i,j,k) = f;
            clear f r
            
        end    
    end
end

% La següent expressió té sidilla. Coses del Matlab.
[X, Y, Z] = meshgrid(c(2):h:c(2)+(ny-1)*h, c(1)+(nx-1)*h:-h:c(1), c(3):h:c(3)+(nz-1)*h);  
pat = patch(isosurface(X,Y,Z,V,0))

pat.FaceColor = 'yellow';
pat.EdgeColor = 'black';
axis tight
camlight 
lighting gouraud
% savefig("objecte") 

Temps = toc

end