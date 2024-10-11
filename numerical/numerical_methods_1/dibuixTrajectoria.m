function dibuixTrajectoria(theta)
% Dibuixa la trajectoria (x,y) per un angle de tir theta
% dibuixTrajectoria(theta)

options = odeset('Events',@criteriParada);
[t,Y]=ode45(@f, [0, 20], [0, 0, 120*cos(theta), 120*sin(theta)], options); 
plot(Y(:,1),Y(:,2),'b-',0,0,'bo',600,0,'ro','LineWidth',2), 
ejes= axis; hold on, plot([ejes(1),ejes(2)],[0,0],'k--'), hold off
title(sprintf('Trajectoria del projectil per theta = %g',theta))
xlabel('x'), ylabel('y')
axis equal