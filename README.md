# SMS-Spam-Classifier
A binary classifier which classifies SMS into Spam Or Ham. Very Helpful, Saves Us In cheated by others
### MY APPROACH IN SOLVING THIS PROBLEM
![SMS Spam Messages Classifier - visual selection (1)](https://github.com/user-attachments/assets/c37e8990-8790-41db-b529-da26540fa5a7)
#### EXPLANATION TO MY APPROACH IN MOST SIMPLEST WAY
1. I downloaded the data, through the link provided in the assignment pdf.
2. After downloading the data, i wanted to know, what will be the most outsatnding model for this SMS classification problem using the downloaded data. Hence I used an automl framework called PyCaret. Because from this i can know about the quality of dataset and model performances. This library automates entire machine elarning life cycle.
3. If the given dataset is not good, then i may get models result's that are very low or simply 1 accuracy. If dataset is good, then all the machine learning life cycles will be implemented correctly like feature engineering etc. So if data is good that i am using then the expected results would be between 0.8 to 0.9 in terms of accuracy.
4. So, this is my first insight. And the Result for this is:
![image](https://github.com/user-attachments/assets/74cb5289-2daa-44e0-876a-49785329c7d5)
You can observe, SVM-LInear Kernal performed Very good with accuracy nearly 0.98.
### AFTER QUICK INSIGHTS STARTED BUILDING THE PROJECT FROM SCRATCH
1. Performed Data Preprocessing : In this stage, i performed knowing the shape of the data, renaming the columns, removing unnecessery columns, removing missing values and duplicate values. Since there is a textual data, if machine learning model is applied then due to more memory usage, it may thros error or it may crash. So i reduced the data size by preserving the information. Almost 33% of data size in memory is reduced without losing information in data. Also checked whether the data is balanced or not using value_counts()
2. After prepraring data i implemented word cloud graphs for both spam and ham classes.
3. After that i performed feature engineering. I performed both Tfidf Vectorizer and Bag of Words On feature column called 'description' and I simpley mapped 'Spam' and 'Ham' with 0 and 1.
#### NOTE : In fetaure engineering I performed Both Tfidf and Bag of Words separately on Feature Column called 'Description'.
#### Why i performed both TFIDF and BAG OF WORDS ? 
Because i wanted to apply more than 20+ binary classifiers on both the data to see the difference in models.

#### AFTER FEATURE ENGINEERING -
1. Now i have two transformed features : transformed features with tfidf, transformed features with bag of words.
2. First I implemented more than 20+ binery classifiers which includes ensembled techniques, naive techniques, tree techniques, neighbors techniques etc.
3. Calculted Results And Mesured the quality of models using metrics like accuracy, precision, recall scores.
4. After that, I implemented more than 20+ binery classifiers on count vectorizer's. Calculated results and measured them using accuracy, precision and recall.

#### SCREEN SHOT'S FOR MODEL PERFORMANCE ON TFIDF TRANSFORMED DATA
##### TFIDF TRANSFORMED DATA - ENSEMBEL TECHNIQUES
![image](https://github.com/user-attachments/assets/7ffa3e15-059e-47ae-aa9b-9c20f5b53430)
##### TFIDF TRANSFORMED DATA - TREE TECHNIQUES
![image](https://github.com/user-attachments/assets/18fb49d9-8684-41b1-b326-dacb4b895e75)
##### TFIDF TRANSFORMED DATA - NAIVE FAMILY
![image](https://github.com/user-attachments/assets/c71fb7dd-8b89-466a-bac6-c61bf37e9796)
##### TFIDF TRANSFORMED DATA - NEIGHBORS FAMILY
![image](https://github.com/user-attachments/assets/6d2b63a8-3a28-43e1-b44f-6045c8225293)
##### TFIDF TRANSFORMED DATA - SVM FAMILY
![image](https://github.com/user-attachments/assets/e69e08f3-d0c8-4a4b-afd8-23de14987a05)

#### SCREEN SHOT'S FOR MODEL PERFORMANCE ON COUNT TRANSFORMED DATA
##### BAG OF WORD'S TRANSFORMED DATA - ENSEMBLE FAMILY
![image](https://github.com/user-attachments/assets/2bcc08dc-0971-40fe-b9ab-290383e88773)
##### BAG OF WORD'S TRANSFORMED DATA - TREE FAMILY
![image](https://github.com/user-attachments/assets/ad8885fd-04e5-4ca0-b131-4dcf18e029f0)
##### BAG OF WORD'S TRANFORMED DATA - NAIVE BAYES FAMILY
![image](https://github.com/user-attachments/assets/61943f47-8df6-4582-b8f5-c5e1c75ce8a0)

##### BAG OF WORD'S TRANSFORMED DATA - NEIGHBOR'S FAMILY
![image](https://github.com/user-attachments/assets/0a158004-eb48-4b87-a439-51678eb9775e)
##### BAG OF WORD'S TRANSFORMED DATA - SVM FAMILY
![image](https://github.com/user-attachments/assets/22a43af2-2cd6-4c35-9262-9ac20a6abb47)


