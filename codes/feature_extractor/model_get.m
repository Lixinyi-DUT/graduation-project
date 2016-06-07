th=-0.25;
label_t=sign(th-train_set(:,5));
label_t=label_t-(label_t==0);
model1=svmtrain(label_t,train_set(:,1:4),'-t 0 -c 0.01');
model2=svmtrain(label_t,train_set(:,1:4),'-t 0 -c 1');
%model3=svmtrain(label_t,train_set(:,1:4),'-t 1 -c 0.01 -d 4');
model4=svmtrain(label_t,train_set(:,1:4),'-t 1 -c 0.1 -d 2');
model5=svmtrain(label_t,train_set(:,1:4),'-t 1 -c 0.1 -d 4');
model6=svmtrain(label_t,train_set(:,1:4),'-t 1 -c 10 -d 4');
model7=svmtrain(label_t,train_set(:,1:4),'-t 2 -c 1 -g 1');

