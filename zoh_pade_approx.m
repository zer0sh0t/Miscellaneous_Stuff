% Ts = 0.2;
Ts = 0.02;

s = tf('s');
P = 1 / (0.2 * s + 1);
C = (500 * s + 50) / (100 * (s ^ 2) + s);
w_p = 2 / Ts;
pade = 1 / (1 + (s / w_p))

F = feedback(C * P, 1);
F_ = feedback(C * pade * P, 1);

dC = c2d(C, Ts, 'tustin')
dP = c2d(P, Ts, 'zoh')
dF = feedback(dC * dP, 1);
step(F, F_, dF);
legend('no pade', 'pade', 'dig');
