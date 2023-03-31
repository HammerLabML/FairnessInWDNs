# Fairness-Enhancing Ensemble Classification in Water Distribution Networks
This repository contains the implementation of the methods proposed in the paper ["Fairness-enhancing Ensemble Classification in Water Distribution Networks"](Paper.pdf) by Janine Strotherm and Barbara Hammer.

## Abstract
As relevant negative examples such as the future criminal detection software show, fairness of AI-based and social domain affecting decision support tools constitutes an important area of research. In this contribution, we investigate the applications of AI to socioeconomically relevant infrastructures such as those of water distribution networks (WDNs), where fairness issues have yet to gain a foothold. To establish the notion of fairness in this domain, we propose an appropriate definition of protected groups and group fairness in WDNs as an extension of existing definitions. We demonstrate that typical methods for the detection of leakages in WDNs are unfair in this sense. Further, we therefore propose a remedy to increase the fairness which can be applied even to non-differentiable ensemble classification methods as used in this context.

## Details
The implementation of the proposed methods can be found in the `Implementation` folder. 

The subfolder `1_FeatureGeneration` is a previous version of the [atmn](https://github.com/HammerLabML/atmn) package. Using 

python ./ScenarioGenerator.py ./samples/config_leaks.xml ./scenarios

in the command line generates the `scenarios` folder which is used in the `2_DataGeneration` subfolder. In this subfolder, the `DataGeneration.ipynb` notebook generates the excel files also included in this folder. These excel files are, in turn, used in the `3_DataUsage` subfolder. In the `FairnessExploration.ipynb` notebook, the proposed approaches are implemented.

## Requirements
All requirements for the whole project are listed in the `Implementation/requirements.txt` file. Note that the requirements listed in the `Implementation/1_FeatureGeneration/requirements.txt` file correspond to the requirements of the previous version of the [atmn](https://github.com/HammerLabML/atmn) package only.

## How To Cite
tba