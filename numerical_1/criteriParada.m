function [value,isterminal,direction] = criteriParada(t,y)
% 
% [value,isterminal,direction] = criteriParada(t,y)

value = y(2);       % detecta cuando este valor es 0
isterminal = 1;     % la integración se detiene cuando "value" es 0    
direction =  -1;    % detecta el valor 0 sólo si la función está decreciendo