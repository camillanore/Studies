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

% Sannsynligheten for a ga fra ett punkt til ett annet, i lopet av to
% skritt, finner vi i P^2. Dette omfatter alle mulige mellomsteg.
i = 1; % til
j = 3; % fra
P2 = P^2;
p_s3_s1_2steg = P2(i,j)

% Deloppgave 1: Finn P^k for k = {2,3,4,40,80}, og deretter sannsynligheten
% for a ga s4->s2 etter eksakt k steg.
k_vec = [2,3,4,40,80]
for k=k_vec
  Pk = P^k;
  p42 = Pk(2,4);
  fprintf('The P^k matrix for k=%d is showed below, and p(s4->s2) is %e.\n', k, p42);
  Pk
end

% Alternativ tolkning: Vi har gatt s4->s2 i lopet av k, eller faerre steg.
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
% 

%% Deloppgave 4

Pk80 = Pk^80;
xK1_approx = Pk80(1,:)
xK5_approx = Pk80(5,:)

%% Deloppgave 5

% d)
y = walk( [.2 .5 .3])