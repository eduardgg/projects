function dydt = f(t,y)
% 
% dydt = f(t,y)

R = 0.00132;
modv = sqrt(y(3)^2 + y(4)^2);
dydt = [y(3); y(4); -R*modv*y(3); -R*modv*y(4)-9.8];
