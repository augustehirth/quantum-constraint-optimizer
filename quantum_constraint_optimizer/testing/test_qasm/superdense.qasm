OPENQASM 2.0;
include "qelib1.inc";
qreg q[14];
creg meas[2];
u2(0.0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
barrier q[0],q[1];
u3(3.141592653589793,0.0,3.141592653589793) q[0];
barrier q[0],q[1];
u2(0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
cx q[1],q[0];
u2(0,3.141592653589793) q[0];
u2(0.0,3.141592653589793) q[0];
u2(0,3.141592653589793) q[1];
barrier q[0],q[1];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
