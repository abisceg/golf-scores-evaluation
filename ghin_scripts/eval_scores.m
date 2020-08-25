## Copyright (C) 2020 
## 
## This program is free software; you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

## -*- texinfo -*- 
## @deftypefn {Function File} {@var{retval} =} eval_scores (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Anthony <abisceg>
## Created: 2020-08-25

function [retval] = eval_scores (scores, totalnumscores, numscorestoeval)
  scores = scores((totalnumscores-(numscorestoeval-1)):end) 
  
  numrounds = size(scores,2)
  highscore = max(scores)
  lowscore = min(scores)
  medianscore = median(scores)
  avescore = mean(scores)
  mostfreqscore = mode(scores)
  nummostfreqscore = sum(scores(1,:)==mode(scores))
  
  figure;
  plot(scores);
  ylim([(min(scores)-12),(max(scores)+16)]);
  title("Scores");
  annotation('textbox',[.72,.55,.2,.2],'String',...
  {'Average Score:',avescore,...
  'Median Score:', medianscore,...
  'High Score:',highscore,...
  'Low Score:',lowscore,...
  'Most Frequent Score:',mostfreqscore,...
  'Based on Last:',numrounds...
  });
  
  retval = scores

endfunction
