Main file: kNN.py
Usage of the kNN.py:

Usage 1:

    python kNN.y -r <Filename> <TargetFeature> <LowerBoundOfValueK> [UpperBoundOfValueK]

    Example1:
        "python kNN.py -r ionosphere.arff class 1 4"
            Shows f1_score of the algorithm for k change in range 1 to 4, output is:
            '''
            ===== F1 Score =====
            k = 1 | F1 Score =  0.846974751687
            k = 2 | F1 Score =  0.884115920763
            k = 3 | F1 Score =  0.833988088918
            k = 4 | F1 Score =  0.850676423041
            '''
    Example2:
        "python kNN.py -r autos.arff price 1 4"
            Shows two kinds of errors (SDE and MAPE) of the algorithm for k change in range 1 to 4, output is:
            '''
            ===== SDE =====
            k = 1 | SDE = 2863.7325621468217
            k = 2 | SDE = 2795.7804544024466
            k = 3 | SDE = 2831.932084249771
            k = 4 | SDE = 2881.7917630384923
            ===== MAPE =====
            k = 1 | MAPE = 0.119463581571
            k = 2 | MAPE = 0.122534820216
            k = 3 | MAPE = 0.126405017001
            k = 4 | MAPE = 0.128656903553
            '''

Usage 2:

    python kNN.y -f <Filename> <TargetFeature> <LowerBoundOfValueK> <UpperBoundOfValueK>

    Example1:
        "python kNN.py -f ionosphere.arff class 1 4"
            Output a diagram (curve graph) in which X-axis shows value of K and Y-axis shows F1Score
    Example2:
        "python kNN.py -f autos.arff price 1 4"
            Output two diagrams (curve graph) in which X-axis shows value of K and Y-axis shows SDE and MAPE respectively

Usage 3:

    python kNN.y -v <OriginalDataFile> <TargetFeature> <TestFile> <UpperBoundOfValueK>

    Example1:
        "python kNN.py -v ionosphere.arff class test_file_classification.csv 8"
            Shows classification of class for each instance that store in test file according to the training data
        in ionosphere.arff
            Output is:
            '''
            Prediction of class for instance 0 is g
            Prediction of class for instance 1 is g
            Prediction of class for instance 2 is g
            Prediction of class for instance 3 is b
            Prediction of class for instance 4 is g
            Prediction of class for instance 5 is b
            Prediction of class for instance 6 is g
            Prediction of class for instance 7 is b
            '''

    Example2:
        "python kNN.py -v autos.arff price test_file_prediction.csv 8"
            Shows prediction of price for each instance(autos) that store in test file according to the training data
        in autos.arff.
            Output is:
            '''
            Prediction of price for instance 0 is 9673.25
            Prediction of price for instance 1 is 9999.875
            Prediction of price for instance 2 is 7365.0
            '''

Source files:

1. filter.py:
    Be used to filter the original data:
    Usage:
        from filter import filt_into_df
        filt_into_df(filename, target_feature)
            Input:
                2 arguments: the filename of original data file and the target feature we need to predict or classify.
            Output:
                A pandas DataFrame storing the data already filtered.

2. normalize.py
    Be used to do 0-1 normalization of the data in filtered data or the data of instance that we need to  predict or
    classify:
    Usage:
        from normalize import normalize_df
        from normalize import normalize_point
        normalize_df(df, target_feature)
            Input:
                2 arguments: A filtered pandas DataFrame and the target feature we need to predict or classify.
            Output:
                A normalized pandas DataFrame.
        normalize_point(df, target_feature, dictionary)
            Input:
                3 arguments: A filtered pandas DataFrame, the target feature
                            and a dictionary storing the data of an instance that we need to  predict or classify.
            Output:
                A normalized dictionary stroring the data of the input instance.

3. prediction.py
    Be used to make prediction of the given feature for a given instance:
    Usage:
        from prediction import predict
        predict(normalized_df, test_point, target_feature, k)
            Input:
                4 arguments: A normalized pandas DataFrame;
                             A normalized dictionary storing data of an instance;
                             The target feature we need to predict;
                             The parameter K;
            Output:
                the predicted value for target feature of the given instance

4. cv_of_prediction.py
    Be used to assess the accuracy of our Prediction algorithm using kNN with different k:
    Usage:
        from cv_of_prediction import cross_validation_p
        cross_validation_p(filename, target_feature, k_range)
            Input:
                3 arguments: The filename of the original data used to test our algorithm
                             The target feature
                             The range of parameter K

5. classification.py
     basically this is the main python file, including the .knn() .handle_file() and the .performance(). It's an module file.

     .knn() functon need three parameters: data for the training datasets;
                                                                   sample for the target instance;
                                                                   k-parameter which has a default
     .handle_file() function need two parameters: data for the datasets;
                                                                                    the title of the class attribute

                                                                                    you need to predict the
                                                                                    classification
     .performance() function need three parameters: the CSV file name;
                                                                                  the target feature you need to do the prediction
                                                                                  parameter using to adjuct the k parameter                                                                                              value of 5.
6. CV_classification.py
     basically this is the python file you should run on the terminal.
                                     By simply call the function in this python file, you can easily get
                                     the result you want: the f1_score for a particular k parameter by
                                     by using .score(); the prediction for a particular
                                     instance by using .predict(). Very neat and easy to use.
    score() function:  three parameter is needed: file_name or path;
                                                                             he target feature you need to do
                                                                                    the prediction
                                                                             parameter using to adjuct the k parameter
                                                                             using this method to come up with a score list, contains
                                                                             all the score you can get from different k parameter.
    predict() function: hree parameter is needed: file_name or path;
                                                                             he target feature you need to do
                                                                                    the prediction
                                                                             the instance you want to do the prediction
                                                                             using this method to come up with a predicted class.
