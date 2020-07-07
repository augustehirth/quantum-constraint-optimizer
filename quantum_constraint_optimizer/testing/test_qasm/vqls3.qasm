OPENQASM 2.0;
include "qelib1.inc";
qreg q[14];
creg c[7];
u2(-3.1415926535897936,2.1345619608734707) q[0];
u2(0,3.141592653589793) q[0];
u3(0.5,0.0,0.0) q[1];
u3(0.5,0.0,0.0) q[2];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[3];
cx q[2],q[3];
u2(0,3.141592653589793) q[2];
u3(-0.5,0.0,0.0) q[2];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[3];
u2(0,3.141592653589793) q[3];
cx q[2],q[3];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[3];
cx q[11],q[3];
u2(0,3.141592653589793) q[11];
u2(0,3.141592653589793) q[3];
cx q[11],q[3];
u2(0,3.141592653589793) q[11];
u2(0,3.141592653589793) q[3];
cx q[11],q[3];
u3(0.5,0.0,0.0) q[13];
cx q[13],q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[13];
cx q[13],q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[13];
cx q[13],q[12];
cx q[11],q[12];
u3(-0.5,0.0,0.0) q[12];
cx q[11],q[12];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
cx q[13],q[1];
u3(1.570796326794896,0.0,3.141592653589793) q[13];
u2(0,3.141592653589793) q[13];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
cx q[11],q[12];
u2(0,3.141592653589793) q[11];
u2(0,3.141592653589793) q[12];
cx q[11],q[12];
u2(0,3.141592653589793) q[11];
u2(0,3.141592653589793) q[12];
cx q[11],q[12];
cx q[11],q[3];
u2(0,3.141592653589793) q[11];
u2(-3.3306690738754696e-16,1.5707963267948966) q[12];
u2(0,3.141592653589793) q[12];
cx q[13],q[12];
u2(0,3.141592653589793) q[12];
u2(-4.71238898038469,4.440892098500626e-16) q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[13];
u2(-3.141592653589794,-1.5707963267948961) q[13];
u2(0,3.141592653589793) q[13];
cx q[13],q[12];
u2(0,3.141592653589793) q[12];
u3(2.641592653589793,0.0,4.71238898038469) q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[13];
u2(-4.440892098500626e-16,4.71238898038469) q[13];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u3(5.120361579871434e-16,2.7582282678139007,-0.18040124830268178) q[1];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(-4.71238898038469,4.440892098500626e-16) q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
u2(-3.141592653589794,-1.5707963267948961) q[1];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(3.7053582876683677,-1.5707963267948968) q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
u3(2.577827019511219,3.9269908169872405,-6.661338147750939e-16) q[1];
cx q[13],q[1];
u1(0.7853981633974483) q[1];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u1(0.7853981633974483) q[0];
u2(0,3.141592653589793) q[1];
u1(-0.7853981633974483) q[1];
cx q[13],q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u1(7.0685834705770345) q[0];
cx q[13],q[1];
u1(-0.7853981633974483) q[1];
u1(1.5707963267948966) q[13];
cx q[13],q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[3];
cx q[11],q[3];
u2(0,3.141592653589793) q[11];
u2(0,3.141592653589793) q[3];
cx q[11],q[3];
cx q[2],q[3];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[3];
cx q[2],q[3];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[3];
cx q[2],q[3];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
u1(-0.7853981633974483) q[1];
cx q[13],q[1];
u1(0.7853981633974483) q[1];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u1(0.7853981633974483) q[0];
u2(0,3.141592653589793) q[1];
u1(-0.7853981633974483) q[1];
cx q[13],q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u1(7.0685834705770345) q[0];
cx q[13],q[1];
u1(-0.7853981633974483) q[1];
cx q[13],q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u3(0.5,0.0,0.0) q[0];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u1(-0.7853981633974483) q[1];
cx q[13],q[1];
u1(0.7853981633974483) q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u1(-0.7853981633974483) q[1];
cx q[13],q[1];
u1(7.0685834705770345) q[1];
u2(0,3.141592653589793) q[13];
cx q[13],q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[13];
cx q[13],q[12];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u3(0.5,0.0,0.0) q[13];
u2(0,3.141592653589793) q[2];
u1(0.7853981633974483) q[2];
cx q[12],q[2];
u1(0.7853981633974483) q[12];
u1(-0.7853981633974483) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u1(-0.7853981633974483) q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u1(0.7853981633974483) q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u1(-0.7853981633974483) q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
u1(0.7853981633974483) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(2.2285979674052676,-3.1415926535897936) q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u1(7.0685834705770345) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u2(-3.8110296325719526,-1.5707963267948963) q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
u3(3.141592653589793,0.3619927613485978,5.074381741733287) q[2];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u3(0.6578016406103717,0.7853981633974496,-5.38182595936685) q[12];
cx q[13],q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[13];
cx q[13],q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[13];
cx q[13],q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
u3(3.1415926535897927,0.6701050880103484,-1.6860894021819952) q[2];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u3(-0.5,0.0,0.0) q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u3(-0.5,0.0,0.0) q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
cx q[13],q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[13];
cx q[13],q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[13];
cx q[13],q[12];
cx q[13],q[1];
u1(-0.7853981633974483) q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u1(0.7853981633974483) q[1];
cx q[13],q[1];
u1(-0.7853981633974483) q[1];
u2(0,3.141592653589793) q[1];
u1(0.7853981633974483) q[13];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u1(7.0685834705770345) q[13];
u2(0,3.141592653589793) q[13];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u1(-0.7853981633974483) q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
u1(0.7853981633974483) q[2];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[1];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u3(0.5,0.0,0.0) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
u2(0,3.141592653589793) q[13];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
u1(-0.7853981633974483) q[13];
u2(0,3.141592653589793) q[13];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
u1(0.7853981633974483) q[13];
u2(0,3.141592653589793) q[13];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
cx q[13],q[12];
u2(0,3.141592653589793) q[12];
u1(0.7853981633974483) q[12];
u2(0,3.141592653589793) q[13];
u1(-0.7853981633974483) q[13];
u2(0,3.141592653589793) q[13];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
cx q[13],q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[13];
cx q[13],q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[13];
cx q[13],q[12];
u3(1.5707963267948972,-3.141592653589793,10.210176124166829) q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[13];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u1(0.7853981633974483) q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
u1(-0.7853981633974483) q[13];
u2(0,3.141592653589793) q[13];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
u2(-2.220446049250313e-16,1.5707963267948968) q[2];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u2(-3.141592653589794,-1.5707963267948961) q[12];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
u2(-4.71238898038469,4.440892098500626e-16) q[2];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u2(-4.440892098500626e-16,-1.5707963267948966) q[12];
u2(0,3.141592653589793) q[2];
u1(-5.497787143782138) q[2];
cx q[1],q[2];
u1(0.7853981633974483) q[2];
cx q[12],q[2];
u1(0.7853981633974483) q[12];
u1(-0.7853981633974483) q[2];
cx q[1],q[2];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
cx q[13],q[1];
cx q[13],q[12];
u1(-0.7853981633974483) q[12];
u1(0.7853981633974483) q[13];
cx q[13],q[12];
u1(7.0685834705770345) q[2];
cx q[1],q[2];
u3(0.5,0.0,0.0) q[1];
cx q[12],q[2];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
cx q[13],q[1];
u2(0,3.141592653589793) q[13];
u1(-0.7853981633974483) q[2];
cx q[1],q[2];
u1(0.7853981633974483) q[2];
cx q[12],q[2];
u1(0.7853981633974483) q[12];
u1(-0.7853981633974483) q[2];
cx q[1],q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0,3.141592653589793) q[12];
u2(0,3.141592653589793) q[2];
cx q[12],q[2];
u2(0.0,3.9269908169872414) q[12];
u2(2.2285979674052676,-3.1415926535897936) q[2];
cx q[1],q[2];
u3(3.141592653589793,0.3619927613485978,5.074381741733287) q[1];
u2(-3.8110296325719526,-1.5707963267948963) q[2];
cx q[1],q[2];
u3(3.1415926535897927,0.6701050880103484,-1.6860894021819952) q[1];
cx q[1],q[0];
u3(-0.5,0.0,0.0) q[0];
cx q[1],q[0];
u2(0,3.141592653589793) q[1];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
u3(-0.5,0.0,0.0) q[13];
u2(0,3.141592653589793) q[13];
cx q[13],q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[13];
u3(0.6578016406103717,0.78539816339744926,-5.38182595936685) q[2];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];
measure q[11] -> c[4];
measure q[12] -> c[5];
measure q[13] -> c[6];