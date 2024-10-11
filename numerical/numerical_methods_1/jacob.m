function J = jacob(x, c)
% Funcio que calcula la jacobiana de forma analitica

C = c;

J(1,1) = -C*sin(x(1))*(8*sin(x(1))+3*sin(x(2)))+C*cos(x(1))*8*cos(x(1))-9*cos(x(1));
J(1,2) = C*cos(x(1))*3*cos(x(2));
J(2,1) = C*cos(x(2))*(3*cos(x(1)));
J(2,2) = -C*sin(x(2))*(3*sin(x(1))+2*sin(x(2)))+C*cos(x(2))*2*sin(x(2))-3*cos(x(2));
end

