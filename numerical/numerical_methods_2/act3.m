% MAIN TREBALL PRACTIC 2 ACT 3

% Surten per pantalla el vector s = (x,y,r), que conté les coordenades del
% centre de la circumferència i el valor del radi d'aquesta. També surt
% el valor de la funcio 'distància' en el punt òptim

    clear, close all
    format long

    global xe; 
    global ye;
    
% Dades
    
    xe = [55.35 49.85 45.85 -25.15 -31.25 ...
        -34.95 -30.05 -25.85 25.65 33.49];
    ye = [43.49 49.58 54.65 55.35 50.28 ...
        42.19 -9.08 -14.55 -26.65 -24.95];
    plot(xe,ye,'.k','LineWidth',2), hold on;
    
    x0 = [0 0 0]; % Punt inicial per iterar
    
% METODE NEWTON-RAPHSON AMB MATRIU JACOBIANA APROXIMADA

it = 0;
tol = 1e-8;
itmax = 20;
X = x0;

while and((norm(dfunc(X)) > tol), (it < itmax));   
    A = - jake(X)\dfunc(X)';
    X = X + A';
    it = it + 1;
end

s = X'
df = dfunc(X)';
f = func(X)

t=0:pi/50:2*pi;
x1 = s(3)*cos(t) + s(1);
y1 = s(3)*sin(t) + s(2);
plot(x1,y1,'r','LineWidth',1), grid on, hold on;
   


