
.. _preface:

*******
Preface
*******

This online book is meant to provide an open science “living” resource on uncertainty characterization methods for the MultiSector Dynamics (MSD) community and other technical communities confronting sustainability, climate, and energy transition challenges. The last decade has seen rapid growth in science efforts seeking to address the interconnected nature of these challenges across scales, sectors, and systems. Accompanying these advances is the growing realization that the deep integration of research from many disciplinary fields is non-trivial and raises important questions. How and why models are developed seems to have an obvious answer (“to gain understanding”). But what does it actually mean to gain understanding? What if a small change in a model or its data fundamentally changes our perceptions of what we thought we understood? What controls the outcomes of our model(s)? How do we understand the implications of model coupling, such as when one model is on the receiving end of several other models that are considered “input data”? 

The often quoted “All models are wrong, but some are useful.” (George Box) is a bit of a conflation trap, often used to excuse known weaknesses in complex models as just an unavoidable outcome of being a modeler. In fact, the quote actually refers to a specific class of small-scale statistical models within an application context that assures a much higher degree of understanding and data quality control than is typical for the coupled human-natural systems applications in the MSD area. Moreover, Box was actually warning readers to avoid overparameterization and emphasizing the need to better understand what underlying factors cause your model to be wrong :cite:p:`box_1976`. 

So, in short, there is a tension when attaining better performance by means of increasing the complexity of a model or model-based workflow. Box highlights that a modeler requires a clear diagnostic understanding of this performance-complexity tradeoff. If we move from small-scale models simulating readily-observed phenomena to the MSD context, things get quite a bit more complicated. How can we provide robust insights for unseen futures that emerge across a myriad of human and natural systems? Sometimes even asking, “what is a model?” or “what is data?” is complicated (e.g., data assimilated weather products, satellite-based signals translated through retrieval algorithms, demographic changes, resource demands, etc.). This MSD guidance text seeks to help readers navigate these challenges. It is meant to serve as an evolving resource that helps the MSD community learn how to better address uncertainty while working with complex chains of models bridging sectors, scales, and systems. It is not intended to be an exhaustive resource, but instead should be seen as a guided tour through state-of-the-science methods in uncertainty characterization, including global sensitivity analysis and exploratory modeling, to provide insights into complex human-natural systems interactions. 

To aid readers in navigating the text, the key goals for each chapter are summarized below.

:numref:`introduction` uses the `Integrated Multisector Multiscale Modeling <https://im3.pnnl.gov>`_ project as a living lab to encapsulate the challenges that emerge in bridging disciplines to make consequential model-based insights while acknowledging the tremendous array of uncertainties that shape them.

:numref:`2_diagnostic_modeling` helps the reader to better understand the importance of using diagnostic modeling to interrogate why uncertain model behaviors may emerge. The chapter also aids readers to better understand the diverse disciplinary perspectives that exist on how best to pursue consequential model-based discoveries.

:numref:`3_sensitivity_analysis_the_basics` is a technical tools-focused primer for readers on the key elements of uncertainty characterization that includes ensemble-based design of experiments, quantitative methods for computing global sensitivities, and a summary of existing software packages.

:numref:`4_sensitivity_analysis` narrates for readers how and why the tools from the previous chapter can be applied in a range of tasks from diagnosing model performance to formal exploratory modeling methods for making consequential model-based discoveries.

The supplemental appendices provided in the text are also important resources for readers. They provide a glossary to help bridge terminology challenges, a brief summary of uncertainty quantification tools for more advanced readers, and a suite of Jupyter notebook tutorials that provide hands-on training tied to the contents of :numref:`3_sensitivity_analysis_the_basics` and :numref:`4_sensitivity_analysis`.

This text was written with a number of different audiences in mind. 

Technical experts in uncertainty may find this to be a helpful and unique resource bridging a number of perspectives that have not been combined in prior books (e.g., formal model diagnostics, global sensitivity analysis, and exploratory modeling under deep uncertainty). 

Readers from different sector-specific and disciplinary-specific backgrounds can use this text to better understand potential differences and opportunities in how to make model-based insights.

Academic or junior researchers can utilize this freely available text for training and teaching resources that include hands-on coding experiences.

This text itself represents our strong commitment to open science and will evolve as a living resource as the communities of researchers provide feedback, innovations, and future tools.
