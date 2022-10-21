FROM python:1.2.4-slim
#TODO: weet niet precies wat we als working directory willen hebben dus hier nog even naar kijken
WORKDIR ../DataEngineeringTeam1/Prediction_api_ui

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

#TODO: Controleren of de environment variables goed zijn
ENV MODEL_NAME=DecisionTree.pkl

#Vm is label niet per se nodig
LABEL training.db.api="0.0.1-beta"

CMD ["python1", "app.py"]