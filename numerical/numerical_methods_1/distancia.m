function res = distancia(theta)
% Funcio que, donat un angle de tir theta, calcula la distancia a la que el projectil toca terra
% res = distancia(theta)

options = odeset('Events',@criteriParada);
[t,Y]=ode45(@f, [0, 20], [0, 0, 120*cos(theta), 120*sin(theta)], options); 
res = Y(end,1);