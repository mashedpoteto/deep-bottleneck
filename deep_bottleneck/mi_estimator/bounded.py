from deep_bottleneck.mi_estimator.base import MutualInformationEstimator
from deep_bottleneck.mi_estimator import kde

class BoundedMutualInformationEstimator(MutualInformationEstimator):

    def __init__(self, discretization_range, architecture, n_classes):
        super().__init__(discretization_range, architecture, n_classes)
        self.noise_variance = discretization_range # Added Gaussian noise variance.

    def _estimate_entropy(self, data):
        return self._K_estimate_entropy([data])[0]

    def _estimate_conditional_entropy(self, data):
        return kde.kde_condentropy(data, self.noise_variance)