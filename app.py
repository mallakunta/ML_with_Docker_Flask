{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c5173d4f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "import pickle\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "91f35ff2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on all addresses (0.0.0.0)\n",
      " * Running on http://127.0.0.1:80\n",
      " * Running on http://10.111.67.173:80\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [28/May/2024 15:01:16] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [28/May/2024 15:01:16] \"GET /favicon.ico HTTP/1.1\" 404 -\n",
      "10.111.67.173 - - [28/May/2024 15:01:46] \"GET / HTTP/1.1\" 200 -\n",
      "10.111.67.173 - - [28/May/2024 15:01:46] \"GET /favicon.ico HTTP/1.1\" 404 -\n",
      "10.111.67.173 - - [28/May/2024 15:02:16] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [28/May/2024 15:03:16] \"GET / HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "app = Flask(__name__) \n",
    "\n",
    "# Load the trained model \n",
    "with open('model.pkl', 'rb') as f:\n",
    "    model = pickle.load(f)\n",
    "\n",
    "@app.route('/') \n",
    "def hello_world(): \n",
    "    return 'Hello, Docker!' \n",
    "\n",
    "@app.route('/predict', methods=['POST']) \n",
    "def predict(): \n",
    "    data = request.get_json(force=True) \n",
    "    prediction = model.predict(np.array(data['input']).reshape(1, -1)) \n",
    "    return jsonify({'prediction': int(prediction[0])}) \n",
    "\n",
    "if __name__ == '__main__': \n",
    "    app.run(host='0.0.0.0', port=80) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dadbd9f7",
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
