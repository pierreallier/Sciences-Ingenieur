clear
a=4.25*2*%pi/360     // angle alpha en rd
b=5.885*2*%pi/360    // angle béta en rd
rf=0.270             // rayon sur plate forme fixe
rm=0.195             // rayon sur plate forme mobile
h=0.276              // hauteur de référence (hauteur lorsque les vérins sont rentrés)

// définition en ligne
function [L]=longueurs(x,y,z,theta1,theta2,theta3)
    xf=zeros(6)
    yf=zeros(6)
    zf=zeros(6)
    xm=zeros(6)
    ym=zeros(6)
    zm=zeros(6)
    alpha=zeros(6)
    bet=zeros(6)

    u=0
    v=1
    //Calcul des angles alpha
    for i=1:2:5
        alpha(i)=u*2*%pi/3+a
        u=u+1   
    end
    for i=2:2:6
        alpha(i)=v*2*%pi/3-a
        v=v+1
    end

    //Calcul des angles beta
    for i=1:2:5
        bet(i)=(u+1)*2*%pi/3-b
        u=u+1
    end
    for i=2:2:6
        bet(i)=v*2*%pi/3+b
        v=v+1
    end

    //Coordonnées de OFBi
    xf=rf*cos(bet)
    yf=rf*sin(bet)

    //Coordonnées de OMAi dans le repère RM
    xm=rm*cos(alpha)
    ym=rm*sin(alpha)

    //Coordonnées de OMAi dans le repère RF
    xmf=(-sin(theta1)*sin(theta2)*sin(theta3)+cos(theta1)*cos(theta3))*xm-sin(theta1)*cos(theta2)*ym+(sin(theta1)*sin(theta2)*cos(theta3)+cos(theta1)*sin(theta3))*zm
    ymf=(cos(theta1)*sin(theta2)*sin(theta3)+sin(theta1)*cos(theta3))*xm+cos(theta1)*cos(theta2)*ym +(-cos(theta1)*sin(theta2)*cos(theta3)+sin(theta1)*sin(theta3))*zm
    zmf=-(sin(theta3)*cos(theta2))*xm+sin(theta2)*ym+(cos(theta3)*cos(theta2))*zm

    //plot2d(xf,yf)
    //plot2d(xmf,ymf)

    //Coordonnées de BiAi dans le repère RF
    xt=xmf+x-xf
    yt=ymf+y-yf
    zt=zmf+z+h-zf

    //Normes des longueurs
    L=sqrt(xt.^2+yt.^2+zt.^2)

endfunction

x=0
y=0
z=0
theta2=0
theta3=0
a=%pi/8
w=50
A=[]
temps=[]

for t=0:0.001:1
    temps=[temps;t]
    theta1=a*sin(w*t)+%pi/3
    L1=longueurs(x,y,z,theta1,theta2,theta3)
    L2=L1'
    A = [A;L2]
end

plot2d(temps,[A(:,1),A(:,2),A(:,3),A(:,4)])

