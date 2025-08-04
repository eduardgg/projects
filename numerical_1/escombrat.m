clear all
close all
format long

vecom = [];
Cmax = 100; % Constant: C = (L*O^2)/g;
res = 0.1; % Ressolucio

for C = 0:res:Cmax
    
    X = [1,1];

    % METODE NEWTON RAPHSON

    it = 0;
    tol = 1e-5;
    itmax = 20; 

    while and((norm(sist(X, C)) > tol), (it < itmax));   
        A = - jacob(X, C)\sist(X, C)';
        X = X + A';
        it = it + 1;
    end
    vecom = [vecom; X(1), X(2)]; % Vector on guardem per cada C els 
                                 % resultats dels angles.
end

vecom;

% REPRESENTACIO GRAFICA

C = [0:res:Cmax];

subplot(2,2,1)
    plot(C, vecom(:, 1)), grid on;
    title('Omega 1');
    axis([0,Cmax,-0.2,1.6]);

subplot(2,2,2)
    plot(C, vecom(:, 2), 'r'), grid on;
    title('Omega 2');
    axis([0,Cmax,-0.2,1.6]);
    
subplot(2,2,3)
    plot(C, vecom(:,1)),hold on;
    plot(C, vecom(:,2), 'r'), grid on;
    legend('Omega 1','Omega 2','Location','southeast')
    line([0, Cmax],[pi/2, pi/2],'Color','k','LineWidth',2)


