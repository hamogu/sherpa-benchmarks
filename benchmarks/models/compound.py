mport numpy as np

from sherpa import models
from sherpa.astro.models import LineBroad

x_small = np.linspace(-4, 3, 50)
x_medium = np.linspace(-40, 300, 2000)
x_large = np.linspace(-4, 300, 5000000)

CCM * AbsorptionEdge * (BlackBody + EmissionGaussian + EmissionGaussian)
