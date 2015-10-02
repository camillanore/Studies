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
% Sannsynligheten for at en partikkel går langs s3 -> s2 -> s1 
% i løpet av 2 tidsskritt.
p_s3_s2_s1 = P(1,2)*P(2,3)

% Sannsynligheten for å gå fra ett punkt til ett annet, i løpet av to
% skritt, finner vi i P^2. Dette omfatter alle mulige mellomsteg.
i = 1; % til
j = 3; % fra
p_s3_s1_2steg = (P^2)*P(i,j)

% Deloppgave 1: Finn P^k for k = {2,3,4,40,80}, og deretter sannsynligheten
% for å gå s4->s2 etter eksakt k steg.
k_vec = [2,3,4,40,80]
for k=k_vec
  Pk = P^k;
  p42 = Pk(2,4);
  fprintf('The P^k matrix for k=%d is showed below, and p(s4->s2) is %e.\n', k, p42);
  Pk
end

% Alternativ tolkning: Vi har gått s4->s2 i løpet av k, eller færre steg.
p42_kumulativ = 0;
for k=[1:80]
  Pk = P^k;
  p42_kumulativ = p42_kumulativ + Pk(2,4);
  if (any (k_vec == k))
    fprintf('The cumulativ probabilty p(s4->s2) for %d steps is %f.\n', k, p42_kumulativ);
  end
end

%% Deloppgave 2: Regulære Markov Rekker
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

%% Deloppgave 4

% Her har Jo feil. Det er umulig at K1 x2=1 og samtidig at K2 x2=0.1.
% Se på P^80, der har du nesten svaret. Ligningssettet blir rekursivt, og 
% svaret ser ut til å være P^uendelig.

% skriv opp ligningene, men pass på indekser, ikke gjøre samme feil som Jo på
% x2 = ... 0.3x2
xK1_approx = (Pk^80)
xK5_approx = (Pk^80)