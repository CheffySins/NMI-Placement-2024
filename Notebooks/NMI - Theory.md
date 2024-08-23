# Theory
## Overview of Asymmetric Flow Field-Flow Fractionation (AF4) [^1]


**Asymmetric Flow Field-Flow Fractionation (AF4)** is a powerful technique used for the separation and characterisation of macromolecules and nanoparticles. It is particularly useful in the field of nanotechnology and polymer science due to its gentle separation conditions and ability to work with a broad size range of particles. The fundamental principle of AF4 is the separation of particles based on their diffusion coefficients in a flow channel. A cross-flow field perpendicular to the direction of the channel flow forces particles of different sizes to different positions within the parabolic flow profile, leading to their separation. Larger particles, with lower diffusion coefficients, are pushed closer to the channel walls and elute later than smaller particles.

### Explanation of Parameters

1. **Hydrodynamic Radius (Rh) / Hydrodynamic Diameter (dh)**
   - **Hydrodynamic Radius (Rh)** is a measure of how a particle diffuses in a fluid and is defined using the Stokes-Einstein equation:
     $$
     Rh = \frac{k_B T}{6 \pi \eta D}
     $$
     where $ k_B $ is the Boltzmann constant, $ T $ is the absolute temperature, $ \eta $ is the viscosity of the medium, and $ D $ is the diffusion coefficient.
   - **Hydrodynamic Diameter (dh)** is simply twice the hydrodynamic radius ($ dh = 2 \times Rh $).

2. **Radius of Gyration (Rg)**
   - **Radius of Gyration (Rg)** is a measure of the distribution of a particle’s mass around its center of mass. For larger molecules (>10 nm), it can be determined using multi-angle light scattering (MALS). The relation for Rg in terms of molecular weight $ M $ and the scattering intensity $ I $ is:
     $$
     Rg^2 = \frac{I(q)}{q^2}
     $$
     where $ q $ is the scattering vector.

3. **Recovery % (from UV data)**
   - **Recovery %** is used to quantify the amount of sample that has been successfully eluted and detected. It is calculated using:
     $$
     \text{Recovery \%} = \left( \frac{\text{Amount detected}}{\text{Initial amount}} \right) \times 100
     $$

4. **Burchard Stockmayer Shape Factor**
   - This factor relates the radius of gyration to the hydrodynamic radius and provides insight into the shape of the macromolecule:
     $$
     \text{Shape Factor} = \frac{Rg}{Rh}
     $$

## Data Treatments
### Despiking
Despiking is the process of identifying and removing extreme deviations (spikes) in data. Spikes in data are typically due to noise or external anomalies and do not represent the underlying signal. Example can be seen in the raw data plots in the Practical Notebook. There are three different despiking algorithms that I investigated and tested;
1. Smoothing / Rolling Mean Method
2. Z-Score Method
3. Median Filter Method

_**Z-Score Method Equation**_ <br>
A z-score / Standard Score describes a value’s relationship to the mean of a group of values. It indicates how many standard deviations a data point is from the mean of the dataset. The formula for calculating the z-score of a value $x$ is:
$$z=\frac{x-\mu}{\sigma}$$

* $x$ is the value being evaluated.
* $\mu$ is the mean of the dataset.
* $\sigma$ is the standard deviation of the dataset.

Interpretation:

- A z-score of 0 means the data point is exactly at the mean.
- A positive z-score indicates the data point is above the mean.
- A negative z-score indicates the data point is below the mean.
- For example, a z-score of 2 means the data point is 2 standard deviations above the mean, while a z-score of -1.5 means it is 1.5 standard deviations below the mean.

#### Description Table

|Method|Description|Applications|Notes|
|-|-|-|-|
|**Rolling Mean**| A technique where each data point in a time series is replaced by the average of the neighboring points within a defined window. This method smooths the data by reducing the impact of random noise and spikes.|Useful when the goal is to smooth out short-term fluctuations and highlight longer-term trends or cycles in the data. It’s commonly used in any context where gradual trends are more important than short-lived variations.| While Rolling mean is useful for identifying overall trends, it can smooth out significant but brief variations (potentially losing important data features). Additionally, rolling mean is not very reliable at boundaries due to fewer points being available.|
|**Z-Score**| Involves calculating the standard score (Z-score) of each data point, which measures how many standard deviations a point is from the mean. Data points with Z-scores exceeding a certain threshold are considered outliers or spikes and can be replaced or removed.|best suited for situations where outliers are expected to be rare and significantly different from the rest of the data, such as in sensor readings or quality control processes. It’s also useful when the data is approximately normally distributed.|Useful for identifying significant outliers, it assumes that the data is normally distributed, which is not always the case.
|**Median Filter**|A median filter replaces each data point with the median of its neighbors within a specified window. Unlike the rolling mean, the median filter is robust to outliers because the median is less affected by extreme values.|Effective in applications where spikes are frequent but not indicative of true data trends, such as in image processing, environmental sensor data, or any scenario where random, sharp noise needs to be removed without distorting the underlying signal.|Particularly useful to preserve sharp features / edges within the data.


[^1]:Asymmetric Flow Field-Flow Fractionation (2021)