% Golf Scores evaluation and plotting
% Github @abisceg

% Replace scores below with your scores
scores = [ 88 88 87 86 78 81 78 79 80 78 76 81 86 82 79 77 84 79 81 75 79 80 86 ...
        82 80 83 80 75 77 77 87 73 78 78 82 76 79 75 77 79 77 ];
totalnumscores = size(scores,2);
x = [1:size(scores,2)];


% all Year
numscorestoeval=totalnumscores;
evaluated_scores = eval_scores(scores,totalnumscores,numscorestoeval);

% last 10 rounds
numscorestoeval=10;
evaluated_scores = eval_scores(scores,totalnumscores,numscorestoeval);

% last 5 rounds
numscorestoeval=5;
evaluated_scores = eval_scores(scores,totalnumscores,numscorestoeval);
