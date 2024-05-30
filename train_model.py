{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "13e9cff2",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.datasets import load_iris\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "import pickle "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c24d45a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load the Iris dataset\n",
    "iris = load_iris()\n",
    "X, y = iris.data, iris.target\n",
    "# Train a decision tree classifier\n",
    "clf = DecisionTreeClassifier() \n",
    "clf.fit(X, y) \n",
    "# Save the model to a file \n",
    "with open('model.pkl', 'wb') as f: \n",
    "    pickle.dump(clf, f) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f95b34c5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
