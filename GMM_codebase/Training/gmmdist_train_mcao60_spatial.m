function [GMM_singleNorm_spatial] = gmmdist_train_mcao60_spatial(GMM_Trained_Table)
% Function to train a spatial Gaussian Mixture Model (GMM) for MCAO-60.
% This function masks ADC and T2 images, extracts their features along with spatial coordinates,
% normalizes the features, and trains a GMM using the specified number of clusters.

% Load the brain template
% Replace the path to 'Template-masked.nii' with the appropriate path on your system.
Templ = load_nii('C:\Users\ramanna1\Documents\Backup Data\PC1\Adrian\Code\Working Code Chamba\Template-masked.nii');
Rat_Cerebrum = Templ.img > 0; % Binary mask of the cerebrum region.

%% Mask the ADC and T2 images using the brain template
% Apply the cerebrum mask to ADC and T2 images to isolate relevant regions.
GMM_Trained_Table.Masked_ADC = Maskimages_Mat(GMM_Trained_Table.ADC, Rat_Cerebrum);
GMM_Trained_Table.Masked_T2 = Maskimages_Mat(GMM_Trained_Table.T2, Rat_Cerebrum);

% Extract data arrays and labels from the masked ADC and T2 images.
[ArrayA, Combined_labelsA, ~, ~, MsizeA, NrowsA] = extractarray(GMM_Trained_Table.Masked_ADC);
[ArrayT, Combined_labelsT, ~, ~, MsizeT, NrowsT] = extractarray(GMM_Trained_Table.Masked_T2);

%% Create and normalize spatial coordinate maps
% Create spatial coordinate maps (R, X, Y, Z) for the brain volume (93x93x120).
[R, X, Y, Z] = mkcoordinatemap(93, 93, 120);

% Normalize the spatial coordinates.
Coorr = normalize(R, 1);
Coorx = normalize(X, 1);
Coory = normalize(Y, 2);
Coorz = normalize(Z, 3);

% Normalize ADC and T2 data.
ArrayTn = normalize_P(ArrayT);
ArrayAn = normalize_P(ArrayA);

% Replicate spatial coordinate maps to match the number of rows in ADC and T2 data.
Coorx = repmat(Coorx, [1, 1, 1, NrowsA]);
Coory = repmat(Coory, [1, 1, 1, NrowsA]);
Coorz = repmat(Coorz, [1, 1, 1, NrowsA]);

% Replicate unnormalized coordinate maps for comparison (optional).
X = repmat(X, [1, 1, 1, NrowsA]);
Y = repmat(Y, [1, 1, 1, NrowsA]);
Z = repmat(Z, [1, 1, 1, NrowsA]);

%% Combine features and labels
% Create a binary mask of valid data points from the ADC and T2 combined labels.
ADC_T2_labels = (Combined_labelsA | Combined_labelsT);

% Extract valid data points from ADC, T2, and spatial coordinates.
K_data_Combined(:, 1) = ArrayAn(~ADC_T2_labels); % Normalized ADC
K_data_Combined(:, 2) = ArrayTn(~ADC_T2_labels); % Normalized T2
K_data_Combined(:, 3) = Coorx(~ADC_T2_labels);  % Normalized X-coordinate
K_data_Combined(:, 4) = Coory(~ADC_T2_labels);  % Normalized Y-coordinate
K_data_Combined(:, 5) = Coorz(~ADC_T2_labels);  % Normalized Z-coordinate

% Store unnormalized features (optional).
Unnorm(:, 1) = ArrayA(~ADC_T2_labels);
Unnorm(:, 2) = ArrayT(~ADC_T2_labels);
Unnorm(:, 3) = X(~ADC_T2_labels);
Unnorm(:, 4) = Y(~ADC_T2_labels);
Unnorm(:, 5) = Z(~ADC_T2_labels);

% Normalize features again for GMM fitting.
K_data_Combined_n(:, 1) = normalize_P(K_data_Combined(:, 1));
K_data_Combined_n(:, 2) = normalize_P(K_data_Combined(:, 2));
K_data_Combined_n(:, 3) = normalize_P(K_data_Combined(:, 3));
K_data_Combined_n(:, 4) = normalize_P(K_data_Combined(:, 4));
K_data_Combined_n(:, 5) = normalize_P(K_data_Combined(:, 5));

% Store the combined and normalized features in a data structure.
Data.SelectedFeatures = K_data_Combined; % Unnormalized features.
Data.NormSelectedFeatures = K_data_Combined_n; % Normalized features.

%% Train the Gaussian Mixture Model
% Specify the number of clusters (NumClus), replicates, and maximum iterations for GMM fitting.
NumClus = 5; % Number of clusters for GMM.
[GMM_singleNorm_spatial] = fitgmdist(Data.NormSelectedFeatures, NumClus, ...
    'start', 'plus', ... % Use k-means++ initialization.
    'Replicates', 10, ... % Number of replicates.
    'Options', statset('MaxIter', 150, 'Display', 'iter')); % Set maximum iterations and display progress.

end
