% Numerical methods for economics
% Author: Camilla Nore
% Date: 2015-08-13

%% Task 2.1 Variable and statement
%  Task 2.1.1 Check output and order of operations
25/4*4
3+4^2
4/12+12
3^2
(5-2)*3

% Task 2.1.2 Rounding numbers

% Task 2.1.3 Normal distribution
X = linspace(0,10,101);
mean = 5;
sigmasq = 1^2;
pdf = normpdf(X,mean,sigmasq);
cdf = normcdf(X,mean,sigmasq);
plot(X,pdf)
hold on
plot(X,cdf)
hold off
title('PDF and CDF for normal distribution')

% Find the probability that x is between 4.2 and 5.5.
P = cdf(56)-cdf(43)

%% Task 2.1.4 Loading data file
testmat= rand(2,3)*4-1; % Random numbers between -1 and 3
save('testmat.mat','testmat')
% Clear all variables, and Load from file
clear all
load('testmat.mat','testmat')
testmat
% Calculate the mean of every column in the matrix
dim_column = 1;
mean_of_columns = mean(testmat,dim_column)

%% Task 2.2 Vector and Matrix

% 2.2.2 

matrixA = zeros(6,6);
for i = 1:6
  for j = 1:6
    matrixA(i,j) = i*10 + j;
  end
end
matrixA
%(a) Matrix of dimension 4*4 from center.
center4 = matrixA(2:5,2:5)
%(b) Matrix of dimension 5*3 selecting column 2, 3, 5.
selected = matrixA(1:5, 2:4);
selected(:,3) = matrixA(1:5,5)    % selection by substituting last row
selected2 = matrixA(1:5, [2,3,5]) % selection by list of indices
%(c) Vector with elements from the first row.
vector = matrixA(1,[1,3,4,5])'

%% Task 2.2.3 Square matrix
A = [1,3;2,3]
B = [7,6
     8,9]
% (a)
check_inverse = A*A^-1 - eye(2)
% (b)
check_division_minus_inverse = A/B - A*B^-1 % A division operator x = A\b 
% produces the solution using Gaussian elimination, without forming the 
% inverse. See mldivide (\) and mrdivide (/) for further information.
% http://se.mathworks.com/help/matlab/ref/inv.html 
% (c)
check_ldivision = A\B -A^-1*B
% (d)
check_commutativity_of_transposed = (A*B)' - B'*A'

%% Task 2.2.4
Y = [2,2,3,4.5,2.3,5.5,6.2,8]'
X = ones(8,2);
X(:,2) = [4.2 3.7 2.9 7.1 2.5 6 4.9 6.9]

% (a)
beta = (X'*X)^-1 * X'*Y
% (b)
sigma = 1
etha = sigma^2*(X'*X)

%% Task 2.2.5 
% Generate this matrix, but what is the trick?
m = [
0 0 1 1 1 1 0 0
0 1 2 3 2 2 1 0
2 3 4 4 4 4 1 1
1 3 4 5 4 3 2 1
0 0 2 3 2 2 0 0
0 0 0 1 1 0 0 0 ];

% (a)
p = zeros(50);
%(b)
p(5:10,5:12) = m;
% (c)
p(20:25,30:37) = m;
%(d)
surf(p)

%% Task 2.3 Loop

% 2.3.1 Row vector, by loop and vector notation.

vectorA = zeros(1,100);
for i = 1:100
  vectorA(i) = 1 / i^2;
end


