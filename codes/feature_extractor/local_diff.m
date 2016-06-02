function diff_square=local_diff(img,block)
fre_global=color_frequency(img);
fre_local=color_frequency(block);
differences=fre_global-fre_local;
diff_square=sum(differences.*differences);
end

