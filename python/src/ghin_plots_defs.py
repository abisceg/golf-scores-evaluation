import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import array
import statistics as stats
from datetime import datetime as date



def plotScores(scores,dates,player,fig,ax):
    plt.figure(fig.number)
    # TODO add date min and max to title
    ax.title.set_text("Scores")
    ax.set_ylim(65,(max(scores)+10))
    ax.plot(dates,scores,'o',label = player)
    plt.xticks(rotation=90)
    #ax.set_yticks([65,70,73,75,80,85,90],minor=False, color = 'red')
    ax.grid(True)
    ax.legend()
    #ax.draw()
    #plt.show()

def plotHistogram(scores):
    plt.figure()
    plt.title("2020 Scores Histogram")
    plt.hist(scores,bins=[60,65,70,75,80,85,90,95,100,105,110,115,120])
    plt.ylim(0,40)
    plt.draw()
    plt.show()

def plotHistogramOverlay(scores,scores1):
    plt.figure()
    plt.title("2020 vs. 2019")
    plt.hist(scores,bins=[60,65,70,75,80,85,90,95,100,105,110,115,120],\
    alpha=0.9, label='2020')
    plt.hist(scores1,bins=[60,65,70,75,80,85,90,95,100,105,110,115,120],\
    alpha=0.5, label='2019')
    plt.legend(loc='upper right')
    plt.ylim(0,40)
    plt.draw()

def statsScores(scores):

    print("Latest " + str(len(scores)) + " Scores: \n" + str(scores))
    print("High Score: " + str(max(scores)))
    print("Low Score: " + str(min(myscores)))
    print("Average Score: " + str(stats.mean(scores)))
    print("Median Score: " + str(stats.median(scores)))

