"""Implementation of a Gaussian Policy"""
# Libraries
from policies import BasePolicy
from abc import ABC
import numpy as np
import copy


class LinearGaussianPolicy(BasePolicy, ABC):
    """
    Implementation of a Gaussian Policy which is linear in the state.
    Thus, the mean will be: parameters @ state.
    The standard deviation is fixed and is defined by the user.
    """
    def __init__(
            self, parameters: np.array = None,
            std_dev: float = 0.1,
            std_decay: float = 0,
            std_min: float = 1e-4,
            dim_state: int = 1,
            dim_action: int = 1,
            multi_linear: bool = False

    ) -> None:
        # Superclass initialization
        super().__init__()

        # Attributes with checks
        err_msg = "[GaussPolicy] parameters is None!"
        assert parameters is not None, err_msg
        self.parameters = parameters

        err_msg = "[GaussPolicy] standard deviation is negative!"
        assert std_dev > 0, err_msg
        self.std_dev = std_dev

        # Additional attributes
        self.dim_state = dim_state
        self.dim_action = dim_action
        self.tot_params = dim_action * dim_state
        self.multi_linear = multi_linear
        self.std_decay = std_decay
        self.std_min = std_min

        return

    def draw_action(self, state) -> float:
        if len(state) != self.dim_state:
            err_msg = "[GaussPolicy] the state has not the same dimension of the parameter vector:"
            err_msg += f"\n{len(state)} vs. {self.dim_state}"
            raise ValueError(err_msg)
        mean = np.array(self.parameters @ state, dtype=np.float64)
        action = np.array(np.random.normal(mean, self.std_dev), dtype=np.float64)
        return action

    def reduce_exploration(self):
        self.std_dev = np.clip(self.std_dev - self.std_decay, self.std_min, np.inf)

    def set_parameters(self, thetas) -> None:
        if not self.multi_linear:
            self.parameters = copy.deepcopy(thetas)
        else:
            self.parameters = np.array(np.split(thetas, self.dim_action))
            
    def get_parameters(self):
        return self.parameters
    

        # TODO: check if this is correct
    def compute_products(self, state_queue, action_queue):
        # Convert inputs to numpy arrays if needed
        state_queue = np.array(state_queue)
        action_queue = np.array(action_queue)

        products = []
        #for each sequence of actions and states, compute the product of the probabilities
        for state_sequence, action_sequence in zip(state_queue, action_queue):
            product = self._compute_sequence_product(np.array(state_sequence), np.array(action_sequence))
            products.append(product)

        return np.array(products)

    def compute_sequence_product(self, state_sequence, action_sequence):
        # Handle both single inputs and batches
        if state_sequence.ndim == 1:
            mean = np.array(self.parameters @ state_sequence, dtype=np.float64)
        else:
            mean = np.array(state_sequence @ self.parameters.T, dtype=np.float64)
        
        # Compute Gaussian probability density
        fact = 1 / (np.sqrt(2 * np.pi) * self.std_dev)
        probs = fact * np.exp(-((action_sequence - mean) ** 2) / (2 * (self.std_dev ** 2)))
        
        return np.prod(probs)
    
    def compute_pi(self, state, action):

        mean = np.array(self.parameters @ state, dtype=np.float64)
        fact = 1 / (np.sqrt(2 * np.pi) * self.std_dev)
        prob = fact * np.exp(-((action - mean) ** 2) / (2 * (self.std_dev ** 2)))
        
        return prob 

    def compute_score(self, state, action) -> np.array:
        if self.std_dev == 0:
            return super().compute_score(state, action)

        state = np.ravel(state)
        action_deviation = action - (self.parameters @ state)
        if self.multi_linear:
            # state = np.tile(state, self.dim_action).reshape((self.dim_action, self.dim_state))
            action_deviation = action_deviation[:, np.newaxis]
        scores = (action_deviation * state) / (self.std_dev ** 2)
        if self.multi_linear:
            scores = np.ravel(scores)
        return scores
    
    def diff(self, state):
        raise NotImplementedError 
