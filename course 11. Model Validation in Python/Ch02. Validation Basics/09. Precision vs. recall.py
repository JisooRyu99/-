'''
The accuracy metrics you use to evaluate your model should always be based on the specific application. For this example, let's assume you are a really sore loser when it comes to playing Tic-Tac-Toe, but only when you are certain that you are going to win.

Choose the most appropriate accuracy metric, either precision or recall, to complete this example. But remember, if you think you are going to win, you better win!

Use rfc, which is a random forest classification model built on the tic_tac_toe dataset.
'''



from sklearn.metrics import precision_score, recall_score

test_predictions = rfc.predict(X_test)

# Create precision score based on the metric
score = precision_score(y_test, test_predictions)
r_score = recall_score(y_test, test_predictions) 

# Print the final result
print('The precision value is {0:.2f}, The recall value is {1:.2f}'.format(score, r_score))
