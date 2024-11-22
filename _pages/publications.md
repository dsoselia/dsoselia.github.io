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



Longbin Zhang, **Soselia  Davit**, Wang  Ruoli, Gutierrez-Farewik  Elena M (2022). Lower-Limb Joint Torque Prediction Using LSTM Neural Networks and Transfer Learning. IEEE Transactions on Neural Systems and Rehabilitation Engineering. IEEE.
- In this project, we explored the use of machine learning techniques to predict lower limb joint torques during daily activities. By using long short-term memory (LSTM) neural networks and transfer learning, we were able to accurately predict hip flexion/extension, hip abduction/adduction, knee flexion/extension, and ankle dorsiflexion/plantarflexion torques during various activities with relatively low error. Our results show that these techniques have the potential to be useful in a variety of settings, such as analyzing the effects of training or medical interventions on athletes or analyzing the remaining muscle strength in assistive device users.


**Soselia  Davit** (2022). Continual Learning and Biomedical Image Data: Attempting to sequentially learn medical imaging datasets using continual learning approaches.
- In this project, I looked at ways to improve the performance of deep learning models in the field of biomedical imaging when retraining on new tasks. We tested a range of continual learning approaches, including EWC, UCB, EWC Online, SI, MAS, and CN-DPM, using X-ray images as our focus. Our results showed that some of the approaches, such as EWC Online and SI, can help signficianrly reduce catastrophic forgetting and achieve accuracy levels similar to those seen when all the data is available at the same time.


Olsson  F, **Soselia  D**, Hijmans  JM, Gutierrez-Farewik  EM (2021). Predicting rocker shoe parameters for reducing plantar pressure using machine learning methods. Gait & Posture. Elsevier.
- In this project, we investigated the effects of different forefoot rocker parameters on gait patterns in able-bodied subjects. We tested a range of parameters, including apex position, apex angle, and rocker radius, using custom-made sneakers with interchangeable mid-and outsoles for the forefoot. Our results showed that these parameters had a significant impact on gait patterns and could potentially be used to improve walking efficiency and reduce fatigue in certain populations. Overall, this project highlights the importance of considering the role of footwear in gait analysis and the potential for customizing footwear to meet the needs of individual users.


Paolini  Christopher, **Soselia  Davit**, Baweja  Harsimran, Sarkar  Mahasweta (2019). Optimal location for fall detection edge inferencing. 2019 IEEE Global Communications Conference (GLOBECOM). IEEE.
- This project focused on using machine learning to develop a fall detection system for elderly individuals. The team collected data on a range of factors, including body movements and IMU sensor readings, and used this data to train four different machine learning models. The models were then tested on a separate dataset to evaluate their accuracy in detecting falls. The results showed that the optimal placement for a fall detection sensor on the body is in front of the shinbone. The findings of this project have the potential to improve the safety of elderly individuals by enabling timely medical attention in the event of a fall.

**Soselia  Davit**, Shugliashvili  Levan, Amashukeli  Shota, Koberidze  Irakli, Chelidze  Giorgi (2018). Freezing Networks: Weight Preservation Procedure for Continual Learning. NeurIPS CL Workshop.
- We developed a new continual learning framework for neural networks that aims to improve their performance on a variety of tasks. The approach uses a parallel neural network structure to emulate long-term and short-term memory by finding and selectively freezing weights that have been identified as important to the network's performance on previously encountered tasks. The results of testing on the MNIST and modified Character Font Images Data Set showed that this approach was successful in avoiding the problem of catastrophic forgetting and outperforming the baseline.


**Soselia  Davit**, Tsintsadze  Magda, Shugliashvili  Levan, Koberidze  Irakli, Amashukeli  Shota, Jijavadze  Sandro (2018). On Georgian Handwritten Character Recognition. IFAC-PapersOnLine. 51.0(30.0): 161-165. Elsevier.
- We developed a framework for recognizing handwritten Georgian text using self-normalizing convolutional neural networks (CNN). We created an extensive dataset with over 200,000 character samples to train the CNN model, and then made the framework available to users in the form of a web service and apps for various operating systems, including Windows, Linux, and iOS.
