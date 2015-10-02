% Mat1120 H2015 - Obligatorisk oppgave 1
% Av: Camilla Nore
% 2015-09-23
  
%% Deloppgave 1.

P = [ 1 0.7 0   0    0
      0 0   0.5 0    0
      0 0.3 0   0.65 0
      0 0   0.5 0    0
      0 0   0   0.35 1 ]

% Bekreft eksempelet fra oppgaven.
% Sannsynligheten for at en partikkel gar langs s3 -> s2 -> s1 
% i lopet av 2 tidsskritt.
p_s3_s2_s1 = P(1,2)*P(2,3)

% Sannsynligheten for a gaa fra ett punkt til ett annet, i lopet av to
% skritt, finner vi i P^2. Dette omfatter alle mulige mellomsteg.
i = 1; % til
j = 3; % fra
p_s3_s1_2steg = (P^2)*P(i,j)

% Deloppgave 1: Finn P^k for k = {2,3,4,40,80}, og deretter sannsynligheten
% for aa gaa s4->s2 etter eksakt k steg.
k_vec = [2,3,4,40,80]
for k=k_vec
  Pk = P^k;
  p42 = Pk(2,4);
  fprintf('The P^k matrix for k=%d is showed below, and p(s4->s2) is %e.\n', k, p42);
  Pk
end

% Alternativ tolkning: Vi har gaatt s4->s2 i lopet av k, eller faerre steg.
p42_kumulativ = 0;
for k=[1:80]
  Pk = P^k;
  p42_kumulativ = p42_kumulativ + Pk(2,4);
  if (any (k_vec == k))
    fprintf('The cumulativ probabilty p(s4->s2) for %d steps is %f.\n', k, p42_kumulativ);
  end
end

%% Deloppgave 2: Regulaere Markov Rekker
% A markov chain is called regular if some power of the transition matrix has
% only positive elements. I.e. in some number of steps, it is possible to go
% from any state to any other state.

% The chain defined by P, is neither Ergodic or Regular. It is not possible
% to get out of s1 and s5.
% From the calculations above we can see that P^k does not converge towared a 
% a stable W matrix with rows converging to a non-zero vector w.
null(P - eye(5))
% I do not know how this relates to the null space.
% Hmm, there must exist a vector v such that 
% vP = vI <=> v(P-I) = 0 thus v is the left nullspace of P-I.
% Since there exists no strictly positive v for P, P is not regular.

%% Deloppgave 3
% Ok svar fra Jo.

%% Deloppgave 4

% Her har Jo feil. Det er umulig at K1 x2=1 og samtidig at K2 x2=0.1.
% Se paa P^80, der har du nesten svaret. Ligningssettet blir rekursivt, og 
% svaret ser ut til aa vaere P^uendelig.

% skriv opp ligningene, men pass paa indekser, ikke gjoere samme feil som
% Jo paa
% x2 = ... 0.3x2
Pk80 = Pk^80;
xK1_approx = Pk80(1,:)
xK5_approx = Pk80(5,:)

%% Deloppgave 5

% a) Jo tar feil, 1 og 5 er absorberende.
% b) Skriv ligningsettet paa matriseform. Du faar da xK = P'*xK, hvor du kan 
% flytte over til xK - P'xK = 0, xK(I - P') = 0.
% P' er P transponert.

% c) Row2: Subtract -p1*Row1
%    Row3: Subtract -p2/(1-p1q1)*Row2
%    Result: 
%             1    -q1       0
%             0  1-p1q1     -q2
%             0     0   -p/(1-p1q1)
% d)

function [y,b] = walk(p)
  q = zeros(3,1);
  for i=1:3
    if (p(i)>0 & p(i)<1)
      fprintf('Error: p(%d) has value out of bounds: %d\n', i, p(i))
    end
    q(i) = 1-p(i);
  end
  A = [ 1     -q(1)   0
        -p(1)   1  -q(2)
        0     -p(3)  1  ];
  % Fritt valg av b, her er det ett lurespm jeg ikke skjonner.
  b = [ 1 1 1 ]';
  y = inv(A)*b;
end

y = walk( [.2 .5 .3])
      
