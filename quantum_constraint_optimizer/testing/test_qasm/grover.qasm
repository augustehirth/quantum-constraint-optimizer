OPENQASM 2.0;
include "qelib1.inc";
qreg q[14];
u2(0.0,6.283185307179586) q[0];
u2(0,3.141592653589793) q[0];
u1(9.42477796076938) q[1];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(6.283185307179586,3.141592653589793) q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
u2(0.0,3.141592653589793) q[1];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0.0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];