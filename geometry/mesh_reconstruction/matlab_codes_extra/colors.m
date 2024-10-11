function [] = colors()

for i=0:0.1:1
    for j=0:0.1:1
        for k=0:0.1:1
            q = plot3(i,j,k,'*');
            q.Color = [i,j,k];
            hold on
        end
    end
end
grid off