function y = S(a,b)
% Retorna el valor de la integral aproximada de f en l'interval (a,b)
f = @(x)(sin(exp(x))); % Funcio a integrar
h = (b-a)/2;
y = (h/3)*(f(a)+4*f((a+b)/2)+f(b));
end

