
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

tx=linspace(0,5,2);
ty=linspace(0,3,2);
tz=linspace(0,2,2);

for i=0:5
    plot3(ty*0+i,ty,ty*0,'k','linewidth',3)
    hold on
    plot3(tz*0+i,tz*0,tz,'k','linewidth',3)
    hold on
end
for j=0:3
    plot3(tz*0,tz*0+j,tz,'k','linewidth',3)
    hold on
    plot3(tx,tx*0+j,tx*0,'k','linewidth',3)
    hold on
end
for k=0:2
    plot3(tx,tx*0,tx*0+k,'k','linewidth',3)
    hold on
    plot3(ty*0,ty,ty*0+k,'k','linewidth',3)
    hold on
end



for i=0:4
    plot3(ty*0+i+0.5,ty,ty*0,'c','linewidth',3)
    hold on
    plot3(tz*0+i+0.5,tz*0,tz,'c','linewidth',3)
    hold on
end
for j=0:2
    plot3(tz*0,tz*0+j+0.5,tz,'m','linewidth',3)
    hold on
    plot3(tx,tx*0+j+0.5,tx*0,'m','linewidth',3)
    hold on
end
for k=0:1
    plot3(tx,tx*0,tx*0+k+0.5,'y','linewidth',3)
    hold on
    plot3(ty*0,ty,ty*0+k+0.5,'y','linewidth',3)
    hold on
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

tx=linspace(0,5,2);
ty=linspace(0,3,2);
tz=linspace(0,2,2);

ta=linspace(0,4,2);
tb=linspace(0,2,2);
tc=linspace(0,1,2);

for i=0:5
    plot3(ty*0+i,0.5+tb,ty*0,'m','linewidth',3)
    hold on
    plot3(tz*0+i,tz*0,0.5+tc,'y','linewidth',3)
    hold on
end
for j=0:3
    plot3(tz*0,tz*0+j,0.5+tc,'y','linewidth',3)
    hold on
    plot3(0.5+ta,tx*0+j,tx*0,'c','linewidth',3)
    hold on
end
for k=0:2
    plot3(0.5+ta,tx*0,tx*0+k,'c','linewidth',3)
    hold on
    plot3(ty*0,0.5+tb,ty*0+k,'m','linewidth',3)
    hold on
end



for i=0:4
    plot3(ty*0+i+0.5,ty,ty*0,'c','linewidth',3)
    hold on
    plot3(tz*0+i+0.5,tz*0,tz,'c','linewidth',3)
    hold on
end
for j=0:2
    plot3(tz*0,tz*0+j+0.5,tz,'m','linewidth',3)
    hold on
    plot3(tx,tx*0+j+0.5,tx*0,'m','linewidth',3)
    hold on
end
for k=0:1
    plot3(tx,tx*0,tx*0+k+0.5,'y','linewidth',3)
    hold on
    plot3(ty*0,ty,ty*0+k+0.5,'y','linewidth',3)
    hold on
end




for i=0:5
    plot3(ty*0+i,ty,ty*0,'k:','linewidth',3)
    hold on
    plot3(tz*0+i,tz*0,tz,'k:','linewidth',3)
    hold on
end
for j=0:3
    plot3(tz*0,tz*0+j,tz,'k:','linewidth',3)
    hold on
    plot3(tx,tx*0+j,tx*0,'k:','linewidth',3)
    hold on
end
for k=0:2
    plot3(tx,tx*0,tx*0+k,'k:','linewidth',3)
    hold on
    plot3(ty*0,ty,ty*0+k,'k:','linewidth',3)
    hold on
end



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


X1 = rand(1, 10);
X2 = rand(1, 10);
Y1 = rand(1, 10);
Y2 = rand(1, 10);
subplot(1,2,1)
plot([X1; X2], [Y1; Y2])      % A bunch of separate lines
subplot(1,2,2)
plot([X1; X2].', [Y1; Y2].')  % Two polygones


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

X1 = rand(1, 10);
X2 = rand(1, 10);
X3 = rand(1, 10);
Y1 = rand(1, 10);
Y2 = rand(1, 10);
Y3 = rand(1, 10);
plot3([X1; X2; X3], [Y1; Y2; Y3])


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

t = 0:pi/50:10*pi;
plot3(sin(t),cos(t),t, 'linewidth',6);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

syms u v
ezsurf(cos(u)*sin(v),sin(u)*sin(v),cos(v));
axis equal
colormap('summer')
shading interp

syms u v
ezsurf(cos(u)*sin(v),sin(u)*sin(v),cos(v));
axis equal
colormap('autumn')
shading interp

[x,y,z] = sphere(40);
surf (x,y,z)
colormap('cool')


[x,y,z] = sphere(40);
ezsurf (x,y,z)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

subplot(2,2,1)
p = patch(isosurface(X,Y,Z,V,0))
p.FaceColor = [0.6 1 0.6];
p.EdgeColor = 'black';
camlight
lighting gouraud

subplot(2,2,2)
p = patch(isosurface(X,Y,Z,V,0))
p.FaceColor = [0.6 1 0.6];
p.EdgeColor = 'black';
camlight
lighting gouraud

subplot(2,2,3)
p = patch(isosurface(X,Y,Z,V,0))
p.FaceColor = [0.6 1 0.6];
p.EdgeColor = 'none';
camlight
lighting gouraud

subplot(2,2,4)
p = patch(isosurface(X,Y,Z,V,0))
p.FaceColor = [0.6 1 0.6];
p.EdgeColor = 'none';
camlight
lighting gouraud

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
