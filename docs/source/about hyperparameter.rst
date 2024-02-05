About the hyperparameters
=========================

A. The latent dimensions
------------------------
The specific choice of the number of latent dimensions can vary depending on the specific application and dataset.
While we provide a default value of 100 in the tutorial as a starting point, it is important to emphasize that the selection of the latent dimensionality is not a one-size-fits-all approach.

The number of latent dimensions can impact downstream results and should be chosen carefully.
Here are some considerations to guide the selection process:

1.	**Complexity of the dataset:** More complex datasets may require higher-dimensional embeddings to capture the underlying patterns and variations adequately.
2.	**Computational resources:** Higher-dimensional embeddings generally require more computational resources for training and analysis. Therefore, the availability of computational power should be taken into account.
3.	**Overfitting and generalization:** Using a very high-dimensional embedding space can potentially lead to overfitting, where the model may capture noise or idiosyncrasies specific to the training data but fail to generalize well to unseen samples. Striking the right balance is crucial for achieving good generalization.
4.	**Evaluation metrics:** Depending on the evaluation metrics used to assess the quality of the clustering or downstream tasks, the number of latent dimensions can impact the performance. It is advisable to conduct sensitivity analyses by varying the dimensionality and examining the effect on relevant metrics.

In summary, the choice of the number of latent dimensions should be guided by a combination of factors, including the complexity of the dataset, available computational resources, potential overfitting concerns, and the evaluation metrics relevant to the downstream analysis.


B. The K nearest neighbor graph
-------------------------------
We assume that cells within the local spatial neighborhoods have the same or similar cellular properties.
The choice of k=15 for the k nearest neighbor graph in this study is a common default value used in many spatial transcriptomics methods.
However, it is essential to consider the characteristics and requirements of each technology when determining the optimal value of k.
Here are some factors to consider:

1.	**Spatial resolution:** Different spatial transcriptomics technologies, such as Visium, Stereo-seq, and MERFISH, may have varying spatial resolutions. The spatial resolution determines the scale at which neighboring spots or cells are considered relevant. Higher spatial resolutions may require smaller values of k to capture local spatial relationships accurately. For example, in the case of the mouse olfactory bulb, we converted the genetic data captured by stereo-seq technology into different bin sizes, with the aim of keeping the size of each spot in the same resolution.
2.	**Biological meaning:** The biological interpretation of the spatial neighborhood graph can differ based on the technology. In Visium, for instance, where spots represent discrete physical locations, the spatial neighborhood graph captures the local proximity between neighboring spots. On the other hand, in imaging-based technologies like MERFISH, where single-cell resolution is achieved, the spatial neighborhood graph may represent physical proximity between individual cells.
3.	**Data characteristics:** The choice of k can also be influenced by the characteristics of the dataset, such as the density of spots or cells, the level of noise, and the extent of spatial heterogeneity. Dense datasets with low noise levels may benefit from smaller values of k to capture fine-grained local relationships accurately.


Given these considerations, it is recommended to perform sensitivity analyses by varying the value of k and evaluating the impact on downstream analyses.
This approach can help identify the optimal value of k for a particular technology and dataset.

In summary, while the default value of k=15 is commonly used, it is crucial to take into account the spatial resolution and biological implications specific to each technology.
Adapting the value of k to suit the characteristics of the data can improve the accuracy and biological relevance of the spatial neighborhood graph.


C. Data scaling
---------------
In the tutorial, we set up the preprocessing methods using spatiAlign, including filtering cells and genes based on default configuration, normalization and log1p transform.
And we set the default scale parameter was ‘False’, it depends on the specific analysis and downstream methods being used.
Scaling can be beneficial in some cases, especially when incorporating algorithms that are sensitive to differences in data ranges or when performing dimensionality reduction techniques.
Scaling ensures that the features (genes) are on a comparable scale, preventing dominant features from overshadowing others during analysis.

