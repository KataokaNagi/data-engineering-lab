# -*- coding: utf-8 -*-
"""simple_transformers_classification_tutorial.py

@author    Kataoka Nagi (calm1836[at]gmail.com)
@date      2021-12-04 06:20:06
@version   1.0
@history   added
@see       [Multi-Class Classification ](https://simpletransformers.ai/docs/multi-class-classification/)

"""

# from utils.log import Log as log
import logging
import pandas as pd
from simpletransformers.classification import ClassificationModel, ClassificationArgs
NUM_EPOCHS = 500
# CLASSIFICATION_MODEL_TYPE = 'bert'
CLASSIFICATION_MODEL_TYPE = 'roberta'
# CLASSIFICATION_MODEL_NAME = 'bert-base-cased'
CLASSIFICATION_MODEL_NAME = 'roberta-base'


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

# Preparing train data
train_data = [
    ["Aragorn was the heir of Isildur", 1],
    ["Frodo was the heir of Isildur", 0],
    ["Pippin is stronger than Merry", 2],
]
train_df = pd.DataFrame(train_data)
train_df.columns = ["text", "labels"]

# Preparing eval data
eval_data = [
    ["Aragorn was the heir of Elendil", 1],
    ["Sam was the heir of Isildur", 0],
    ["Merrry is stronger than Pippin", 2],
]
eval_df = pd.DataFrame(eval_data)
eval_df.columns = ["text", "labels"]

# Optional model configuration
model_args = ClassificationArgs(num_train_epochs=1)

# Create a ClassificationModel
model = ClassificationModel(
    CLASSIFICATION_MODEL_TYPE,
    CLASSIFICATION_MODEL_NAME,
    num_labels=3,
    args=model_args
)

# Train the model
model.train_model(train_df)

# Evaluate the model
result, model_outputs, wrong_predictions = model.eval_model(eval_df)

# Make predictions with the model
predictions, raw_outputs = model.predict(["Sam was a Wizard"])

print(predictions)
