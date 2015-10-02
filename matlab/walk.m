function [y,b] = walk(p)
  q = zeros(3,1);
  for i=1:3
    value_test = (p(i)<0 | p(i)>=1);
    if value_test
      fprintf('Error: p( %d ) has value out of bounds: %f.', i, p(i));
      break;
    end
    q(i) = 1-p(i);
  end
  A = [ 1     -q(1)   0
        -p(1)   1  -q(2)
        0     -p(3)  1  ];
  % Fritt valg av b, her er det et lurespm jeg ikke skjonner.
  b = [ 1 1 1 ]';
  y = inv(A)*b;
end
