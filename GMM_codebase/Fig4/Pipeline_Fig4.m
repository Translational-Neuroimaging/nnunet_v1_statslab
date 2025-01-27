% Training
% Train a Gaussian Mixture Model (GMM) using the training dataset for Figure 4 (`Table_24h_GMM1_Fig4_Train`).
% The trained model is stored in `GMM_singleNorm_Fig4`.
[GMM_singleNorm_Fig4] = gmmdist_train_mcao60(Table_24h_GMM1_Fig4_Train);

% Train a spatially-aware GMM using the same training dataset for Figure 4.
% The trained spatial model is stored in `GMM_singleNorm_Fig4_spatial`.
[GMM_singleNorm_Fig4_spatial] = gmmdist_train_mcao60_spatial(Table_24h_GMM1_Fig4_Train);

% Testing
% Test the trained GMM model (`GMM_singleNorm_Fig4`) with the test dataset (`Table_24h_GMM1_Fig4_Test`).
% The resulting probability maps and other outputs are stored in `GMM_Test_Table_Fig4`.
[GMM_Test_Table_Fig4, ~, ~, ~, ~, ~] = gmmdist_test_mcao60(Table_24h_GMM1_Fig4_Test, GMM_singleNorm_fig1);

% Test the trained spatial GMM model (`GMM_singleNorm_Fig4_spatial`) with the same test dataset.
% The resulting spatial probability maps are stored in `GMM_Test_Table_Fig4_spatial`.
[GMM_Test_Table_Fig4_spatial, ~, ~, ~, ~, ~] = gmmdist_test_mcao60_spatial(Table_24h_GMM1_Fig4_Test, GMM_singleNorm_fig1_spatial);

% Averaging
% Combine the probability maps from both non-spatial (`GMM_Test_Table_Fig4`) and spatial 
% (`GMM_Test_Table_Fig4_spatial`) GMMs using an averaging function.
% The combined results are stored in `Combined_Space_GMM_Fig4`.
[Combined_Space_GMM_Fig4] = Average_M(GMM_Test_Table_Fig4.RF_Probmaps1_new, GMM_Test_Table_Fig4_spatial.RF_Probmaps1_new);

% Calculating structs for 24-hour and 1-week ground truth (GT)
% Compare the combined probability maps for the control group (`Combined_Space_GMM_Fig4_Control`) 
% against the ground truth for the control group at 24 hours (`Control_Voi_24h.Voi_24h`).
% The evaluation metrics (e.g., Dice, sensitivity, specificity) are stored in `struct_Fig4_control_24h`.
[~, struct_Fig4_control_24h] = DiceSensSpec_T(Control_Voi_24h.Voi_24h, Combined_Space_GMM_Fig4_Control);

% Compare the combined probability maps for the therapy group (`Combined_Space_GMM_Fig4_Therapy`)
% against the ground truth for the therapy group at 24 hours (`Therapy_Voi_24h.Voi_24h`).
% The evaluation metrics are stored in `struct_Fig4_therapy_24h`.
[~, struct_Fig4_therapy_24h] = DiceSensSpec_T(Therapy_Voi_24h.Voi_24h, Combined_Space_GMM_Fig4_Therapy);

% Compare the combined probability maps for the control group (`Combined_Space_GMM_Fig4_Control`)
% against the ground truth for the control group at 1 week (`Control_1w_correct_order.Voi_1w1`).
% The evaluation metrics are stored in `struct_Fig4_control_1w`.
[~, struct_Fig4_control_1w] = DiceSensSpec_T(Control_1w_correct_order.Voi_1w1, Combined_Space_GMM_Fig4_Control);

% Compare the combined probability maps for the therapy group (`Combined_Space_GMM_Fig4_Therapy`)
% against the ground truth for the therapy group at 1 week (`Therapy_1w_correct_order.Voi_1w1`).
% The evaluation metrics are stored in `struct_Fig4_therapy_1w`.
[~, struct_Fig4_therapy_1w] = DiceSensSpec_T(Therapy_1w_correct_order.Voi_1w1, Combined_Space_GMM_Fig4_Therapy);
