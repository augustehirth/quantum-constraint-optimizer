OPENQASM 2.0;
include "qelib1.inc";
qreg q[14];
u2(3.141592653589793,3.141592653589793) q[0];
u1(0.7853981633974483) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
u3(3.141592653589793,0.39269908169872414,3.141592653589793) q[2];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u1(-0.39269908169872414) q[1];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u1(0.39269908169872414) q[1];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
u1(-0.7853981633974483) q[1];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0.0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
u1(0.7853981633974483) q[1];
u2(0,3.141592653589793) q[2];
u1(0.7853981633974483) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
cx q[1],q[0];
u1(-0.7853981633974483) q[0];
cx q[1],q[0];
u1(0.7853981633974483) q[0];
u2(0.0,3.141592653589793) q[1];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
u2(0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[2];
cx q[1],q[2];
