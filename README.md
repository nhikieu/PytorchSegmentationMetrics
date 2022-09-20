# Pytorch Segmentation Metrics

Pytorch implementation of 3 popular evaluation metrics (OA, AA, and kappa coefficient) for image segmentation

## Overall Accuracy (OA)
![image](https://user-images.githubusercontent.com/62233450/191171609-6a2d2725-78ef-495a-a998-300670e2e791.png)

## Average Accuracy (AA)
![image](https://user-images.githubusercontent.com/62233450/191171642-d9691cec-7518-4398-9f95-1a9161623e6f.png)

## Kappa Coefficient (k)
![image](https://user-images.githubusercontent.com/62233450/191171655-107adbe7-4612-4e87-b20b-b3e366ec2ff2.png)

![image](https://user-images.githubusercontent.com/62233450/191171666-c4cb7edc-ae5a-497b-b6d1-0ea654c6c5e7.png)

<p>where</p>
<p>N_c: the number of samples classifed correctly</p>
<p>N_a: the number of total samples</p>
<p>N^i_c, N^i_a: N_c and N_a for each class</p>
<p>N^i_r, N^i_p: the number of real samples for each class and the number of predicted samples for each class, respectively</p>

Equations are originally from
https://arxiv.org/abs/2008.05457
