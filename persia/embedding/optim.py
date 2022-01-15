from abc import ABC
from typing import Tuple

from persia.prelude import OptimizerBase


class Optimizer(ABC):
    r"""Base optimizer to configurate the embedding update behavior."""

    def __init__(self):
        self.optimizer_base = OptimizerBase()

    def apply(self):
        """Register sparse optimizer to embedding server."""
        self.optimizer_base.apply()


class SGD(Optimizer):
    r"""A wrapper to config the embedding-server SGD optimizer."""

    def __init__(self, lr: float, momentum: float = 0.0, weight_decay: float = 0.0):
        """
        Arguments:
            lr(float): learning rate.
            momentum(float, optional): momentum factor.
            weight_decay(float, optional): parameters L2 penalty factor.
        """
        super(SGD, self).__init__()
        self.lr = lr
        self.momentum = momentum
        self.weight_decay = weight_decay
        self.optimizer_base.init_sgd(self.lr, self.weight_decay)


class Adagrad(Optimizer):
    r"""A wrapper to config the embedding-server Adagrad optimizer."""

    def __init__(
        self,
        lr: float = 1e-2,
        initial_accumulator_value: float = 1e-2,
        weight_decay: float = 0,
        g_square_momentum: float = 1,
        eps: float = 1e-10,
        vectorwise_shared: bool = False,
    ):
        """
        Arguments:
            lr (float): learning rate.
            initial_accumulator_value (float, optional): initialization accumulator value for adagrad optimizer.
            weight_decay (float, optional): parameters L2 penalty factor.
            g_square_momentum (float, optional): factor of accumulator incremental.
            eps(float, optional): epsilon term to avoid divide zero.
            vectorwise_shared(bool, optional): whether to share optimizer status vectorwise of embedding.

        """
        super(Adagrad, self).__init__()
        self.lr = lr
        self.weight_decay = weight_decay
        self.initial_accumulator_value = initial_accumulator_value
        self.g_square_momentum = g_square_momentum
        self.eps = eps
        self.vectorwise_shared = vectorwise_shared
        self.optimizer_base.init_adagrad(
            self.lr,
            self.weight_decay,
            self.g_square_momentum,
            self.initial_accumulator_value,
            self.eps,
            self.vectorwise_shared,
        )
