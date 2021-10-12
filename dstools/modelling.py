import pandas as pd
import numpy as np
from sklearn.metrics import recall_score, precision_score, f1_score
import matplotlib.pyplot as plt

def eval_thresh(y_real, y_proba):
   '''
    Check the metrics varying the classification threshold

    Parameters:
            y_real (np.array): An array containing the ground truth labels
            y_proba (np.array): An array containing the probabilities of label equal 1
    Returns:
            df_metrics (pd.DataFrame): A pandas dataframe containing the thresholds and metrics associated
            
    '''
  recall_score_thresh = []
  precision_score_thresh = []
  f1_score_thresh = []
  q_rate = []
  tx = len(y_real)

  for thresh in np.arange(0,1,0.05):
    y_thresh = [1 if x >= thresh  else 0 for x in y_proba]
    q_rate.append(np.sum(y_thresh)/tx)
    recall_score_thresh.append(recall_score(y_real, y_thresh))
    precision_score_thresh.append(precision_score(y_real, y_thresh))
    f1_score_thresh.append(f1_score(y_real, y_thresh))

  dict_metrics = {'threshold':np.arange(0,1,0.05),'recall_score':recall_score_thresh,\
                    'precision_score':precision_score_thresh,'f1_score':f1_score_thresh, 'queue_rate':q_rate}
  df_metrics = pd.DataFrame(dict_metrics)
  return df_metrics

def plot_metrics(df):
    '''
    plot metrics calculated by the function eval_thresh

    Parameters:
            df (pandas.dataframe): A data frame that is the result of eval_thresh function
    Returns:
            None
            
    '''
  plt.plot(df['threshold'],df['recall_score'], '-.')
  plt.plot(df['threshold'],df['precision_score'], '-.')
  plt.plot(df['threshold'],df['f1_score'],'-.')
  plt.plot(df['threshold'],df['queue_rate'],'-.')
  plt.legend(['recall','precision','f1_score', 'queue_rate'])
  plt.xlabel("Threshold")
  plt.ylabel("Metric")
  display(plt.show())