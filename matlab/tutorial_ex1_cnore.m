% Numerical methods for economics
% Author: Camilla Nore
% Date: 2015-08-13

%% Task 2.2 Vector and Matrix

% 2.2.2 

matrixA = zeros(6,6);
for i = 1:6
  for j = 1:6
    matrixA(i,j) = i*10 + j;
  end
end
matrixA



%% Task 2.3 Loop

% 2.3.1 Row vector, by loop and vector notation.

vectorA = zeros(1,100);
for i = 1:100
  vectorA(i) = 1 / i^2;
end


