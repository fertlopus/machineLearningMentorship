import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Perceptron(torch.nn.Module):
    """
    Персептрон - модель нейронной сети из 1-го слоя.
    """
    def __init__(self, input_dimension):
        """
        Конструктор для модели Персептрона.
        :param input_dimension: размер входного веткора-признаков.
        """
        super(Perceptron, self).__init__()
        self.fully_connected_layer = torch.nn.Linear(input_dimension, 1)

    def forward(self, x_input):
        """
        Прямой проход персептрона.
        :param x_input: тензор входных данных (batch_size, num_features)
        :return: Tensor. tensor.shape = (batch_size, )
        """
        return self.fully_connected_layer(x_input)


def linreg(dataset_path):
    data = pd.read_csv(dataset_path, header=None).values
    X, y = data[:, 0], data[:, 1]
    X, y = X.reshape(-1, 1), np.log(y.reshape(-1, 1))

    mean_x, mean_y = X.mean(), y.mean()
    std_x, std_y = X.std(), y.std()
    X, y = (X - mean_x) / std_x, (y - mean_y) / std_y
    features, target = torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)

    model = Perceptron(input_dimension=features.shape[1])
    loss = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.7)

    n_epochs = 150
    losses = []

    for epoch in range(n_epochs):
        optimizer.zero_grad()
        model.zero_grad()
        outputs = model(features)
        loss_metric = loss(target, outputs)
        losses.append(loss_metric.item())
        loss_metric.backward()
        optimizer.step()
        print("Epoch: {}    MSE Loss: {}".format(epoch, loss_metric.item()))

    plt.figure(figsize=(10, 5))
    plt.plot(losses)
    plt.show()

    predicted = model(torch.tensor(X, dtype=torch.float32)).detach().numpy()
    plt.scatter(X, y, label='Реальные данные')
    plt.plot(X, predicted, label='Подобраная Линейная Регрессия', color='r')
    plt.legend()
    plt.show()

    return None
