# Supervised VS Unsupervised VS Reinforcement

## Supervised Learning
The model learns from labeled data like a student learning with a teacher who also provides the correct answers. The goal is to map inputs to known outputs.

| Feature        | Description                                              |
| -------------- | -------------------------------------------------------- |
| **Data**       | Input-Output pairs (e.g., photos of cats labeled "cat"). |
| **Goal**       | Predict the output for new, unseen inputs.               |
| **Techniques** | Regression, Classification.                              |

**Examples:**
- Email spam filter - SPAM vs  NOT SPAM
- House Price Prediction - using historical data( like size, location, number of rooms) and their actual sale prices to predict the price of a new house.

## Unsupervised Learning
The model looks for hidden patterns in the unlabeled data i.e. the system tries to find structure on its own.

|Feature|Description|
|---|---|
|**Data**|Only inputs, no labels.|
|**Goal**|Discover underlying structure or groupings.|
|**Techniques**|Clustering, Dimensionality Reduction, Association.|
**Examples:**
- Customer Segmentation: A retailer analyzes purchase history to group customers into categories (e.g. "budget shoppers", "luxury buyers") without being told those groups exist beforehand.
- Anomaly detection: Identifying unusual credit card transactions that don't fit the normal spending pattern of a user.

## Reinforcement Learning
An Agent learns by interacting with an environment. It receives rewards for good actions and penalties for bad ones, aiming to maximize total reward over time.

|Feature|Description|
|---|---|
|**Data**|Experience gained through trial and error.|
|**Goal**|Learn a strategy (policy) to achieve a long-term objective.|
|**Techniques**|Q-Learning, Deep Q-Networks (DQN), Policy Gradients.|
**Examples:**
- Game Playing(AlphaGo): The AI plays millions of games against itself. It gets a "reward" for winning a "penalty" for losing, eventually learning which moves lead to victory.
- Robotics: Teaching a robot to walk. It gets small reward for moving forward and a large penalty for falling over.