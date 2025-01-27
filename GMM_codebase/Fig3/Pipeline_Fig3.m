% ADC T2
% Train Gaussian Mixture Models (GMMs) using data from 5, 10, 15, 20, and 25 animals.
% The models are trained using `gmmdist_train_mcao60` for non-spatial data.
[GMM_singleNorm_5animals] = gmmdist_train_mcao60(Table_24h_GMM_5animals);
[GMM_singleNorm_10animals] = gmmdist_train_mcao60(Table_24h_GMM_10animals);
[GMM_singleNorm_15animals] = gmmdist_train_mcao60(Table_24h_GMM_15animals);
[GMM_singleNorm_20animals] = gmmdist_train_mcao60(Table_24h_GMM_20animals);
[GMM_singleNorm_25animals] = gmmdist_train_mcao60(Table_24h_GMM_25animals);

% Train spatial Gaussian Mixture Models (GMMs) using the same data for 5, 10, 15, 20, and 25 animals.
% The spatial model incorporates spatial information into the training.
[GMM_singleNorm_5animals_spatial] = gmmdist_train_mcao60_spatial(Table_24h_GMM_5animals);
[GMM_singleNorm_10animals_spatial] = gmmdist_train_mcao60_spatial(Table_24h_GMM_10animals);
[GMM_singleNorm_15animals_spatial] = gmmdist_train_mcao60_spatial(Table_24h_GMM_15animals);
[GMM_singleNorm_20animals_spatial] = gmmdist_train_mcao60_spatial(Table_24h_GMM_20animals);
[GMM_singleNorm_25animals_spatial] = gmmdist_train_mcao60_spatial(Table_24h_GMM_25animals);

%% Testing the models with test datasets
% Test the non-spatial models with their respective datasets.
[GMM_Test_Table_5animals, ~, ~, ~, ~, ~] = gmmdist_test_mcao60(Table_24h_GMM_5_small_removed, GMM_singleNorm_5animals);
[GMM_Test_Table_10animals, ~, ~, ~, ~, ~] = gmmdist_test_mcao60(Table_24h_GMM_10_small_removed, GMM_singleNorm_10animals);
[GMM_Test_Table_15animals, ~, ~, ~, ~, ~] = gmmdist_test_mcao60(Table_24h_GMM_15_small_removed, GMM_singleNorm_15animals);
[GMM_Test_Table_20animals, ~, ~, ~, ~, ~] = gmmdist_test_mcao60(Table_24h_GMM_20_small_removed, GMM_singleNorm_20animals);
[GMM_Test_Table_25animals, ~, ~, ~, ~, ~] = gmmdist_test_mcao60(Table_24h_GMM_25_small_removed, GMM_singleNorm_25animals);

% Test the spatial models with their respective datasets.
[GMM_Test_Table_5animals_spatial, ~, ~, ~, ~, ~] = gmmdist_test_mcao60_spatial(Table_24h_GMM_5_small_removed, GMM_singleNorm_5animals_spatial);
[GMM_Test_Table_10animals_spatial, ~, ~, ~, ~, ~] = gmmdist_test_mcao60_spatial(Table_24h_GMM_10_small_removed, GMM_singleNorm_10animals_spatial);
[GMM_Test_Table_15animals_spatial, ~, ~, ~, ~, ~] = gmmdist_test_mcao60_spatial(Table_24h_GMM_15_small_removed, GMM_singleNorm_15animals_spatial);
[GMM_Test_Table_20animals_spatial, ~, ~, ~, ~, ~] = gmmdist_test_mcao60_spatial(Table_24h_GMM_20_small_removed, GMM_singleNorm_20animals_spatial);
[GMM_Test_Table_25animals_spatial, ~, ~, ~, ~, ~] = gmmdist_test_mcao60_spatial(Table_24h_GMM_25_small_removed, GMM_singleNorm_25animals_spatial);

%% Calculate Dice similarity, sensitivity, and specificity for each model
% Perform evaluation for the non-spatial models using Dice similarity, sensitivity, and specificity.
[~, struct_5animals] = DiceSensSpec_T(GMM_Test_Table_5animals.Voi_24h, GMM_Test_Table_5animals.RF_Probmaps1_new);
[~, struct_10animals] = DiceSensSpec_T(GMM_Test_Table_10animals.Voi_24h, GMM_Test_Table_10animals.RF_Probmaps1_new);
[~, struct_15animals] = DiceSensSpec_T(GMM_Test_Table_15animals.Voi_24h, GMM_Test_Table_15animals.RF_Probmaps1_new);
[~, struct_20animals] = DiceSensSpec_T(GMM_Test_Table_20animals.Voi_24h, GMM_Test_Table_20animals.RF_Probmaps1_new);
[~, struct_25animals] = DiceSensSpec_T(GMM_Test_Table_25animals.Voi_24h, GMM_Test_Table_25animals.RF_Probmaps1_new);

% Perform evaluation for the spatial models using Dice similarity, sensitivity, and specificity.
[~, struct_5animals_spatial] = DiceSensSpec_T(GMM_Test_Table_5animals_spatial.Voi_24h, GMM_Test_Table_5animals_spatial.RF_Probmaps1_new);
[~, struct_10animals_spatial] = DiceSensSpec_T(GMM_Test_Table_10animals_spatial.Voi_24h, GMM_Test_Table_10animals_spatial.RF_Probmaps1_new);
[~, struct_15animals_spatial] = DiceSensSpec_T(GMM_Test_Table_15animals_spatial.Voi_24h, GMM_Test_Table_15animals_spatial.RF_Probmaps1_new);
[~, struct_20animals_spatial] = DiceSensSpec_T(GMM_Test_Table_20animals_spatial.Voi_24h, GMM_Test_Table_20animals_spatial.RF_Probmaps1_new);
[~, struct_25animals_spatial] = DiceSensSpec_T(GMM_Test_Table_25animals_spatial.Voi_24h, GMM_Test_Table_25animals_spatial.RF_Probmaps1_new);

%% Combine spatial and non-spatial results and evaluate
% Average the probability maps from spatial and non-spatial models for each group.
[Combined_Space_GMM_5animals] = Average_M(GMM_Test_Table_5animals.RF_Probmaps1_new, GMM_Test_Table_5animals_spatial.RF_Probmaps1_new);
[Combined_Space_GMM_10animals] = Average_M(GMM_Test_Table_10animals.RF_Probmaps1_new, GMM_Test_Table_10animals_spatial.RF_Probmaps1_new);
[Combined_Space_GMM_15animals] = Average_M(GMM_Test_Table_15animals.RF_Probmaps1_new, GMM_Test_Table_15animals_spatial.RF_Probmaps1_new);
[Combined_Space_GMM_20animals] = Average_M(GMM_Test_Table_20animals.RF_Probmaps1_new, GMM_Test_Table_20animals_spatial.RF_Probmaps1_new);
[Combined_Space_GMM_25animals] = Average_M(GMM_Test_Table_25animals.RF_Probmaps1_new, GMM_Test_Table_25animals_spatial.RF_Probmaps1_new);

% Evaluate the combined results using Dice similarity, sensitivity, and specificity.
[~, struct_5animals_combined] = DiceSensSpec_T(GMM_Test_Table_5animals.Voi_24h, Combined_Space_GMM_5animals);
[~, struct_10animals_combined] = DiceSensSpec_T(GMM_Test_Table_10animals.Voi_24h, Combined_Space_GMM_10animals);
[~, struct_15animals_combined] = DiceSensSpec_T(GMM_Test_Table_15animals.Voi_24h, Combined_Space_GMM_15animals);
[~, struct_20animals_combined] = DiceSensSpec_T(GMM_Test_Table_20animals.Voi_24h, Combined_Space_GMM_20animals);
[~, struct_25animals_combined] = DiceSensSpec_T(GMM_Test_Table_25animals.Voi_24h, Combined_Space_GMM_25animals);

%% Training and testing with the 5 biggest animals dataset
% Train GMM models on the largest dataset and test them.
[GMM_singleNorm_5biggest_animals] = gmmdist_train_mcao60(Table_24h_GMM);
[GMM_singleNorm_5biggest_animals_spatial] = gmmdist_train_mcao60_spatial(Table_24h_GMM);
[GMM_Test_Table_5biggest_animals, ~, ~, ~, ~, ~] = gmmdist_test_mcao60(Table_24h_GMM, GMM_singleNorm_5biggest_animals);
[GMM_Test_Table_5biggest_animals_spatial, ~, ~, ~, ~, ~] = gmmdist_test_mcao60_spatial(Table_24h_GMM, GMM_singleNorm_5biggest_animals_spatial);

% Combine and evaluate results for the 5 biggest animals.
[Combined_Space_GMM_5biggest_animals] = Average_M(GMM_Test_Table_5biggest_animals.RF_Probmaps1_new, GMM_Test_Table_5biggest_animals_spatial.RF_Probmaps1_new);
[~, struct_5biggest_animals] = DiceSensSpec_T(GMM_Test_Table_5biggest_animals.Voi_24h, Combined_Space_GMM_5biggest_animals);

%% Training and testing with all animals dataset
% Train and test models using the entire dataset.
[GMM_singleNorm_all_animals] = gmmdist_train_mcao60(Table_24h_GMM);
[GMM_singleNorm_all_animals_spatial] = gmmdist_train_mcao60_spatial(Table_24h_GMM);
[GMM_Test_Table_all_animals, ~, ~, ~, ~, ~] = gmmdist_test_mcao60(Table_24h_GMM, GMM_singleNorm_all_animals);
[GMM_Test_Table_all_animals_spatial, ~, ~, ~, ~, ~] = gmmdist_test_mcao60_spatial(Table_24h_GMM, GMM_singleNorm_all_animals_spatial);

% Combine and evaluate results for the entire dataset.
[Combined_Space_GMM_all_animals] = Average_M(GMM_Test_Table_all_animals.RF_Probmaps1_new, GMM_Test_Table_all_animals_spatial.RF_Probmaps1_new);
[~, struct_all_animals] = DiceSensSpec_T(GMM_Test_Table_all_animals.Voi_24h, Combined_Space_GMM_all_animals);
