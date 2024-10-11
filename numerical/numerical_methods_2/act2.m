% MAIN TREBALL PRACTIC 2 ACT 2

    clear, close all
    format long

% Funcio a integrar

    a = 0;
    b = 3;
    f = @(x)(sin(exp(x)));

% Integral exacta

    Iex = 0.60612447341877   % Iex = integral(f,a,b)

% APARTAT A

M = 4; % Nombre de 'm' 

Itrap = zeros(M,1);
Isimp = zeros(M,1);
mv = zeros(M,1);

for i = 1:M
    
    m = 2*2^i;
    mv(i) = m;
    
    % TRAPEZI COMPOSTA
    h1 = (b-a)/m;
    xm1 = [a:h1:b];
    Itrap(i) = h1*(0.5*(f(a)+f(b))+f(xm1(2:end-1))*ones(m-1,1));

    % SIMPSON COMPOSTA
    h2 = (b-a)/(2*m);
    xm2 = [a:h2:b];
    f1 = f(xm2(2:2:end-1));
    f2 = f(xm2(3:2:end-2));
    Isimp(i) = (f(a)+f(b))*h2/3 + 4*h2/3*(f1*ones(length(f1),1))...
        + 2*h2/3*(f2*ones(length(f2),1));
end

ertrap = abs(Itrap - Iex);
ersimp = abs(Isimp - Iex);

figure(1)

    subplot(1,2,1)
    loglog(mv, ertrap,'LineWidth',2), grid on;   
    title('Error absolut quadratura Trapezi composta')
    xlabel('Nombre de subintervals')
    ylabel('Error absolut')
    subplot(1,2,2)
    loglog(mv, ersimp,'LineWidth',2), grid on;
    title('Error absolut quadratura Simpson composta')
    xlabel('Nombre de subintervals')
    ylabel('Error absolut')
   
% APARTAT B

% Calculem les derivades de forma analítica i, mitjançant les gràfiques
% en busquem un màxim o una fita superior en valor absolut.

d1f = @(x)(exp(x).*cos(exp(x)));
d2f = @(x)(exp(x).*(cos(exp(x))-exp(x).*sin(exp(x))));
d3f = @(x)(exp(2*x).*(cos(exp(x)).*(1-exp(x))-3*sin(exp(x))));
d4f = @(x)(exp(2*x).*(2*((1-exp(x)).*cos(exp(x))-3*sin(exp(x)))... 
    - exp(x).*(1-exp(x)).*sin(exp(x))-4*exp(x).*cos(exp(x))));

figure(2)

xx = linspace(a, b, 1000);
subplot(2,2,1)
plot(xx, d1f(xx)), grid on;
title('Primera derivada')
subplot(2,2,2)
plot(xx, d2f(xx)), grid on;
title('Segona derivada')
subplot(2,2,3)
plot(xx, d3f(xx)), grid on;
title('Tercera derivada')
subplot(2,2,4)
plot(xx, d4f(xx)), grid on;
title('Quarta derivada')


% ALGORISME RECURSIU

% La funció S(a,b) retorna el valor de la integral aproximada 
% entre els extrems 'a' i 'b', mitjançant la quadratura de Simpson.
% Atenció: si es canvia la funcio f a integrar, cal canviar-la també
% en la funcio S.
% La funció rec és l'algorisme resursiu que retorna el valor aproximat 
% de la integral entre els valors 'a' i 'b' amb la tolerància indicada.

eps = 1e-4; % Tolerància
global xv; % Variable on es guarden els punts d'integració de l'algorisme
           % recursiu.
xv = [a;b];
Irec = rec(a,b,eps)
x = sort(xv);
O = zeros(length(x),1);
Err = abs(Iex-Irec)
nombre_subintervals = length(x)-1

figure(3)

xx = linspace(a, b, 1000);
plot(xx, f(xx),'b','LineWidth',2), grid on, hold on;
plot(x,O,'.r','LineWidth',2);
title('Funció a integrar i punts a d''integració de l''algorisme recursiu')
legend('Funció a integrar','Punts a d''integració de l''algorisme recursiu')
title('Error absolut menor a 10^-8')
axis([0 3 -1 1])
     
