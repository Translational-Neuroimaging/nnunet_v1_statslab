% Calculate Volumes for Therapy Group
% Compute the volumes for different brain regions (Rat Cortex, Rat Striatum, and Rat Cerebrum)
% using the combined probability maps for the therapy group (`Combined_Space_GMM_Fig1_Therapy`).
% The results are stored in `volumes_Therapy`.
[volumes_Therapy] = volume_calc_all(Combined_Space_GMM_Fig1_Therapy, Rat_Cortex, Rat_Striatum, Rat_Cerebrum);

% Calculate Volumes for Control Group
% Similarly, compute the volumes for the same brain regions for the control group
% using the combined probability maps (`Combined_Space_GMM_Fig1_Control`).
% The results are stored in `volumes_Control`.
[volumes_Control] = volume_calc_all(Combined_Space_GMM_Fig1_Control, Rat_Cortex, Rat_Striatum, Rat_Cerebrum);
