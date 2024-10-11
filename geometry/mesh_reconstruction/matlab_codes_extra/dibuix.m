function [] = dibuix(data)

n = size(data,2);

% 2 Dimensions
if (n == 2) | (n == 4)
    if n == 2
        P = data;
        p = plot(P(:,1),P(:,2),'.')
        p.Color = 'black';
    else
        P = data(:, [1 2]);
        N = data(:, [4 5]);
        p = plot(P(:,1),P(:,2),'.')
        p.Color = [0 0 0];
        hold on
        q = quiver(P(:,1),P(:,2),N(:,1),N(:,2))
        q.Color = [1 0 1];
    end
    grid off
end

% 3 Dimensions
if (n == 3) | (n == 6)
    if n == 3
        P = data;
        p = plot3(P(:,1),P(:,2),P(:,3),'.')
        P.Color = 'black';
    else
        P = data(:, [1 2 3]);
        N = data(:, [4 5 6]);
        % p = plot3(P(:,1),P(:,2),P(:,3),'.')
        % p.Color = [0 0 0];
        % hold on
        q = quiver3(P(:,1),P(:,2),P(:,3),N(:,1),N(:,2),N(:,3))
        q.Color = 'red';
    end
    grid off
end

end