from matplotlib import pyplot as plt

in0 = open("LOSS.txt","r")

tr1=[];tr2=[];tr3=[];tr4=[];tr5=[]
vl1=[];vl2=[];vl3=[];vl4=[];vl5=[]

def input_as_int():
    return (in0.readline().strip()[0:4])

for i in range(666):
    in0.readline()

    epoch = input_as_int()

    tr_generator_adversial_loss =input_as_int()
    tr_generator_l1_loss = input_as_int()
    tr_generator_full_loss = input_as_int()
    tr_discriminator_loss = input_as_int()
    tr_discriminator_accuracy = input_as_int()

    in0.readline()
    in0.readline()
    in0.readline()

    vl_generator_adversial_loss = input_as_int()
    vl_generator_l1_loss = input_as_int()
    vl_generator_full_loss = input_as_int()
    vl_discriminator_loss = input_as_int()
    vl_discriminator_accuracy = input_as_int()

    in0.readline()

    tr1.append(tr_generator_adversial_loss)
    tr2.append(tr_generator_l1_loss)
    tr3.append(tr_generator_full_loss)
    tr4.append(tr_discriminator_loss)
    tr5.append(tr_discriminator_accuracy)

    vl1.append(vl_generator_adversial_loss)
    vl2.append(vl_generator_l1_loss)
    vl3.append(vl_generator_full_loss)
    vl4.append(vl_discriminator_loss)
    vl5.append(vl_discriminator_accuracy)

arr = []
for i in range(666):
    arr.append(i)
plt.xlabel('Epochs')
plt.ylabel('Training - Discriminator Accuracy')
#plt.scatter(arr,vl5,color="black",linewidth=0.05)
plt.plot(tr5,color = "black",linewidth=0.5)
plt.show()