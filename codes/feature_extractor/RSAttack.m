function  y=RSAttack(img)
[RSU_FM,RSU_M]=RSAnalysis(img,12,12);
R_dif=RSU_M(1,1)-RSU_FM(1,1);
S_dif=RSU_M(1,2)-RSU_FM(1,2);
y=R_dif/RSU_M(1,1)-S_dif/RSU_M(1,2)+0.3;
end