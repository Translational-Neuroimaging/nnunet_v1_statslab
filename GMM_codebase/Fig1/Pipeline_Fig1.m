% Training
% Train a Gaussian Mixture Model (GMM) using the input training table `Table_24h_GMM1_Fig1_Train`
% and store the resulting model in `GMM_singleNorm_fig1`.
[GMM_singleNorm_fig1] = gmmdist_train_mcao60(Table_24h_GMM1_Fig1_Train);

% Train a spatially-aware Gaussian Mixture Model (GMM) using the same input training table
% and store the resulting model in `GMM_singleNorm_fig1_spatial`.
[GMM_singleNorm_fig1_spatial] = gmmdist_train_mcao60_spatial(Table_24h_GMM1_Fig1_Train);

% Testing
% Test the trained GMM model (`GMM_singleNorm_fig1`) with the testing data `Table_24h_GMM_Fig1_Test`.
% The function outputs the test results into `GMM_Test_Table_Fig1`.
[GMM_Test_Table_Fig1, ~, ~, ~, ~, ~] = gmmdist_test_mcao60(Table_24h_GMM_Fig1_Test, GMM_singleNorm_fig1);

% Test the spatial GMM model (`GMM_singleNorm_fig1_spatial`) with the same testing data.
% The test results are stored in `GMM_Test_Table_Fig1_spatial`.
[GMM_Test_Table_Fig1_spatial, ~, ~, ~, ~, ~] = gmmdist_test_mcao60_spatial(Table_24h_GMM_Fig1_Test, GMM_singleNorm_fig1_spatial);

% Averaging
% Combine the probability maps from both the non-spatial and spatial GMM tests to form a combined
% result, `Combined_Space_GMM_Fig1`.
[Combined_Space_GMM_Fig1] = Average_M(GMM_Test_Table_Fig1.RF_Probmaps1_new, GMM_Test_Table_Fig1_spatial.RF_Probmaps1_new);

% Calculating Structs
% Compute the Dice similarity coefficient, sensitivity, and specificity between the ground truth
% volumes of interest (`Voi_24h`) and the combined probability map (`Combined_Space_GMM_Fig1`).
% The results are stored in `struct_Fig1_avg`.
[~, struct_Fig1_avg] = DiceSensSpec_T(GMM_Test_Table_Fig1.Voi_24h, Combined_Space_GMM_Fig1);

% Compute Dice similarity, sensitivity, and specificity for the non-spatial GMM probability maps
% and store the results in `struct_Fig1_adct2`.
[~, struct_Fig1_adct2] = DiceSensSpec_T(GMM_Test_Table_Fig1.Voi_24h, GMM_Test_Table_Fig1.RF_Probmaps1_new);

% Compute Dice similarity, sensitivity, and specificity for the spatial GMM probability maps
% and store the results in `struct_Fig1_spat`.
[~, struct_Fig1_spat] = DiceSensSpec_T(GMM_Test_Table_Fig1.Voi_24h, GMM_Test_Table_Fig1_spatial.RF_Probmaps1_new);

%