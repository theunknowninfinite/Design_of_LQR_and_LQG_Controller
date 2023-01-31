clc
clear all
A = [[0    0       0     1.0   0    0];[0    0       0      0   1.0   0 ];[0    0       0      0    0   1.0];[0  -0.98   -0.98    0    0    0 ];[0  -0.539  -0.049   0    0    0];[0  -0.098  -1.078   0    0    0]];
B = [ 0 ; 0;0 ;0.001 ;5.0e-5; 0.0001];
C = [eye(3),zeros(3)];
D = zeros(3,1);
Q = [[10,0,0,0,0,0];[0,0.00001,0,0,0,0];[0,0,1000,0,0,0];
    [0,0,0,0,0,0];[0,0,0,0,1000,0];[0,0,0,0,0,0]];
R = 0.0001;
[K,S,P]=lqr(A,B,Q,R);
sys1 = ss(A-B*K,B,C,D);
step(sys1);