---
layout: archive
title: "Papers"
permalink: /Papers/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

For a full list of my papers, please see my [Google Scholar](https://scholar.google.com/citations?user=rHit2vIAAAAJ&hl=en) profile.


Chen L, Chen J, Liu C, Kirchenbauer J, **Soselia D**, Zhu C, Goldstein T, Huang H (2024). OPTune: Efficient Online Preference Tuning. *arXiv preprint arXiv:2406.07657.*

Chen L, Zhu C, **Soselia D**, Chen J, Zhou T, Goldstein T, Huang H (2024). Odin: Disentangled Reward Mitigates Hacking in RLHF. *Proceedings of the 41st International Conference on Machine Learning (ICML 2024).*

Ding P, **Soselia D**, Armstrong T, Su J, Huang F (2023). Reviving Shift Equivariance in Vision Transformers. *The Second Workshop on Spurious Correlations, Invariance and Stability (SCIS), ICML 2023.*

**Soselia D**, Saifullah K, Zhou T (2023). Learning UI-to-Code Reverse Generator Using Visual Critic Without Rendering. *arXiv preprint arXiv:2305.14637.*

Zhang L, **Soselia D**, Wang R, Gutierrez-Farewik EM (2023). Estimation of Joint Torque by EMG-Driven Neuromusculoskeletal Models and LSTM Networks. *IEEE Transactions on Neural Systems and Rehabilitation Engineering.*

Zhang L, **Soselia D**, Wang R, Gutierrez-Farewik EM (2022). Lower-Limb Joint Torque Prediction Using LSTM Neural Networks and Transfer Learning. *IEEE Transactions on Neural Systems and Rehabilitation Engineering.*
- We explore the use of machine learning techniques to predict lower limb joint torques during daily activities. By using LSTMs we were able to accurately predict hip flexion/extension, hip abduction/adduction, knee flexion/extension, and ankle dorsiflexion/plantarflexion torques during various activities with relatively low error. Our results show that these techniques can be used for analyzing the effects of training or medical interventions on athletes or analyzing the remaining muscle strength in assistive device users.


**Soselia Davit** (2022). Continual Learning and Biomedical Image Data: Attempting to sequentially learn medical imaging datasets using continual learning approaches.  
- I looked at ways to improve the performance of deep learning models in the field of biomedical imaging when retraining on new tasks. We tested a range of continual learning approaches, including EWC, UCB, EWC Online, SI, MAS, and CN-DPM, using X-ray images as our focus. Our results showed that some of the approaches, such as EWC Online and SI, can help signficianrly reduce catastrophic forgetting and achieve accuracy levels similar to those seen when all the data is available at the same time.


Olsson F, **Soselia D**, Hijmans JM, Gutierrez-Farewik EM (2021). Predicting Rocker Shoe Parameters for Reducing Plantar Pressure Using Machine Learning Methods. *Gait & Posture, Elsevier.*
- In this project, we investigated the effects of different forefoot rocker parameters on gait patterns in able-bodied subjects. We tested a range of parameters, including apex position, apex angle, and rocker radius, using custom-made sneakers with interchangeable mid-and outsoles for the forefoot. Our results showed that these parameters had a significant impact on gait patterns and could potentially be used to improve walking efficiency and reduce fatigue in certain populations. Overall, this project highlights the importance of considering the role of footwear in gait analysis and the potential for customizing footwear to meet the needs of individual users.


Paolini C, **Soselia D**, Baweja H, Sarkar M (2019). Optimal Location for Fall Detection Edge Inferencing. *2019 IEEE Global Communications Conference (GLOBECOM).*  
- This project focused on using machine learning to develop a fall detection system for elderly individuals. We collected recordigs of body movements and IMU sensor readings, and used this data to train a variety of traditional and NN-based approaches. The results showed that the optimal placement for a fall detection sensor on the body is in front of the shinbone. The findings of this project have the potential to improve the safety of elderly individuals by enabling timely medical attention in the event of a fall.

**Soselia D**, Shugliashvili L, Amashukeli S, Koberidze I, Chelidze G (2018). Freezing Networks: Weight Preservation Procedure for Continual Learning. *NeurIPS Continual Learning Workshop.*
- We developed a new continual learning framework for neural networks that aims to improve their performance on a variety of tasks. The approach uses a parallel neural network structure to emulate long-term and short-term memory by finding and selectively freezing weights that have been identified as important to the network's performance on previously encountered tasks. The results of testing on the MNIST and modified Character Font Images Data Set showed that this approach was successful in avoiding the problem of catastrophic forgetting and outperforming the baseline.


**Soselia D**, Tsintsadze M, Shugliashvili L, Koberidze I, Amashukeli S (2018). On Georgian Handwritten Character Recognition. *IFAC-PapersOnLine. 51.0(30.0): 161-165. Elsevier.*
- We created an extensive dataset with over 200,000 character samples for Georgian handwritten characters, and developed a high-accuracy recognition pipeline. We framework available to users in the form of a web service and apps Android and iOS.
