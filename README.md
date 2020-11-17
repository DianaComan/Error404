Our project is composed of 4 main parts:
       - Data Preparation for the ML Model: which is also composed of 2 parts:
                     - Data preparation of the encoding, which contains the cleaning, generalizaton and mapping of the data on a constant format. We did this by following those 
                       steps:
                            - if any row didn't have any relevant information, we excluded it;
                            - if age was missing, we took the average age: 45 years;
                            - if sex was missing, if age < 55, masculine, if age > 55, feminine( as it is the average per every age interval);
                            - if any date was missing, we put a date from the others that were available( if no date was filed out, we chose a date random from the 3 months
                              period);
                            - if any information was in a different format then the constant one, we adjust it to the constant one;
                            - for the 'confirmare contact cu o persoană infectată', 'mijloace de transport folosite', 'istoric de călătorie', we transformed every answer in a 
                              DA/NU answer
                            - if any results weren't either positive or negative, then we adjust them to either positive/negative( we tested either options, neither showed any 
                              improvement in our algorithm)
                      - Data encoding:
                            - we used primarily label encoding and one hot encoding for this project:
                                   - label encoding for the next columns:
                                          - 'varsta" by age intervals using encodingAge;
                                          -  dates by the weeks using encodingTime;
                                          - 'confirmare contact cu o persoană infectată', 'mijloace de transport folosite', 'istoric de călătorie' by label encoding with Da/NU 
                                             labels
                                          - 'diagnostic' by the possibily of being suspected of covid or not
                                          - 'rezultat' by either being possitive/negative
                                   - one hot encoding:for simptomes, because multiple simptomes for a single individuals, we chose one hot encoding here
         - ML Model:
                     - we used a logistic regression for this as it is better in the cases of deciding of a pass/fail situation ( in our case, positive/negative)
                     - we used our Datapreparation and also our PerformanceMetrics functions
        - PerformanceMetrics:
                     - we used the sklearn.metrics to get our wanted metrics, to measure the performance of our model predictions
  
  
 Also, seperated from our project code flow is :
       - viz flow, which helps us to vizualize the influence our data might have on our model and how much it can influence it.
