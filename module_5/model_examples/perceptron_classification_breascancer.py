import numpy as np
import torch
import os
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from module_5.utils.helpers import get_run_logdir


def classification(save_path):
    data = load_breast_cancer()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Custom Parameters
    N, D = X_train.shape
    n_epochs = 1000

    # Converting to torch tensor
    X_train, X_test = torch.tensor(X_train, dtype=torch.float32), torch.tensor(X_test, dtype=torch.float32)
    y_train, y_test = torch.tensor(y_train.reshape(-1, 1), dtype=torch.float32), torch.tensor(y_test.reshape(-1,1), dtype=torch.float32)

    # losses array
    train_losses = np.zeros(n_epochs)
    test_losses = np.zeros(n_epochs)

    model = torch.nn.Sequential(
        torch.nn.Linear(D, 1),
        torch.nn.Sigmoid()
    )

    loss = torch.nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters())

    for epoch in range(n_epochs):
        optimizer.zero_grad()

        # Forward propagation
        outputs = model(X_train)
        loss_metric = loss(outputs, y_train)

        # Backward propagation
        loss_metric.backward()
        optimizer.step()

        # Test loss
        outputs_test = model(X_test)
        loss_metric_test = loss(outputs_test, y_test)

        # Save losses
        train_losses[epoch] = loss_metric.item()
        test_losses[epoch] = loss_metric_test.item()

        if(epoch + 1) % 50 == 0:
            print("Epoch: {}\nTrain Loss: {}\nTest Loss: {}".format(epoch, round(loss_metric.item(), 4), round(loss_metric_test.item(), 4)))

    plt.plot(train_losses, label='train loss')
    plt.plot(test_losses, label='test loss')
    plt.legend()
    plt.show()

    with torch.no_grad():
        p_train = model(X_train)
        p_train = (p_train.numpy() > 0)
        train_acc = np.mean(y_train.numpy() == p_train)

        p_test = model(X_test)
        p_test = (p_test.numpy() > 0)
        test_acc = np.mean(y_test.numpy() == p_test)
    print(f"Train acc: {train_acc:.4f}, Test acc: {test_acc:.4f}")


    # save_to = get_run_logdir(save_path)
    torch.save(model.state_dict(), "model.pt")
    return None
