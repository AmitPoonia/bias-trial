
## Bias/Fairness evaluation in machine learning

This repository is sort of a playground for different freely available tools or
libraries to interpret/inspect a trained machine learning model and compare them



1. Fairlearn (https://github.com/fairlearn/fairlearn)

    - backed by Microsoft
    - both evaluation and mitigation
    - well defined approach with categorisation of "fairness" and detailed metrics
    - provides dashboard 
    - supports scikit-learn
    

2. LIME (https://github.com/marcotcr/lime)

    - focuses more on explaining/interpreting the model
    - one can quantify impact of individual features on prediction
    - matplotlib based visualization support


3. Shap (https://github.com/slundberg/shap)
    - similar to LIME
    - visualization can be little hard to read for multi-class model
    - supports scikit-learn

4. WhatIf tool (https://github.com/pair-code/what-if-tool)

    - backed by Google
    - focused on inference and visualization 
    - supports tensorflow
    - a more elaborative dashboard 
    - "no-code" tool with more focus on dashboard 
 
 
5. Interpret (https://github.com/interpretml/interpret)

    - backed by Microsoft
    - focused on explaining/interpreting the model
    - its own glass-box models which are designed for interpretability 
    - also supports black-box interpretability similar to LIME etc.
    - dashboard 
    - supports scikit-learn for black-box interpretability


6. AIF360 (https://github.com/IBM/AIF360)

    - backed by IBM
    - similar to Fairlearn
    - both detecting and mitigating biases based on explainable metrics
    - supports scikit-learn and tensorflow
    - 

    
 