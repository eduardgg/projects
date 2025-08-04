function y = rec(a,b,e)
% y: Retorna el valor aproximat de la integral 
%    entre els valors 'a' i 'b' amb la tolerancia indicada.
% xv: S'hi guarden els valors de les absisses dels punts que divideixen 
%     l'interval (a,b) en subintervals.

global xv;

    if ((abs(S(a,b) - S(a,(a+b)/2) - S((a+b)/2,b))) < e*(b-a))
       y = S(a,b);
    else
       xv = [xv; (a+b)/2];
       y = rec(a,(a+b)/2,e) + rec((a+b)/2,b,e);
    end
end

