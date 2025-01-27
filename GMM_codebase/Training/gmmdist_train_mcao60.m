function [GMM_singleNorm] = gmmdist_train_mcao60(GMM_Trained_Table)
% gmmdist_train - Train a Gaussian Mixture Model (GMM) on selected features

% Load the template image used for masking
Templ = load_nii('C:\Users\ramanna1\Documents\Backup Data\PC1\Adrian\Code\Working Code Chamba\Template-masked.nii');

% Define a binary mask for the Rat_Cerebrum by thresholding the template image
Rat_Cerebrum = Templ.img > 0;

% Mask the ADC and T2 images in GMM_Trained_Table with the Rat_Cerebrum mask
GMM_Trained_Table.Masked_ADC = Maskimages_Mat(GMM_Trained_Table.ADC, Rat_Cerebrum);
GMM_Trained_Table.Masked_T2 = Maskimages_Mat(GMM_Trained_Table.T2, Rat_Cerebrum);

% Extract features from the masked ADC and T2 images
[ArrayA, Combined_labelsA, ~, ~, MsizeA, NrowsA] = extractarray(GMM_Trained_Table.Masked_ADC);
[ArrayT, Combined_labelsT, ~, ~, MsizeT, NrowsT] = extractarray(GMM_Trained_Table.Masked_T2);

% Combine labels for ADC and T2 images
ADC_T2_labels = (Combined_labelsA | Combined_labelsT);

% Create a combined feature matrix for ADC and T2 data
K_data_Combined(:,1) = ArrayA(~ADC_T2_labels);
K_data_Combined(:,2) = ArrayT(~ADC_T2_labels);

% Normalize the combined feature matrix
K_data_Combined_n(:,1) = normalize_P(K_data_Combined(:,1));
K_data_Combined_n(:,2) = normalize_P(K_data_Combined(:,2));

% Store the selected features and normalized features in a data structure
Data.SelectedFeatures = K_data_Combined;
Data.NormSelectedFeatures = K_data_Combined_n;

% Set parameters for GMM training: 5 clusters, 'start' method, 10 replicates, and options
NumClus = 5;
[GMM_singleNorm] = fitgmdist(Data.NormSelectedFeatures, NumClus, ...
       'start', 'plus', 'Replicates', 10, 'Options', statset('MaxIter', 150, 'Display', 'iter'));
end
