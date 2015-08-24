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

%% Task 2.3 Loop

% 2.3.1 Row vector, by loop and vector notation.

vectorA = zeros(1,100);
for i = 1:100
  vectorA(i) = 1 / i^2;
end


