import tensorflow as tf
from keras import layers, models, callbacks
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sn
from sys import exit



def create_df(path,seed):
    #Criando um dataset a partir do caminho fornecido
    try:
        df = pd.read_csv(path,sep=",")
        scaler = StandardScaler()
        df.iloc[:,0:2]  = pd.DataFrame(scaler.fit_transform(df.iloc[:,0:2]))

        train = df.sample(frac=0.8,random_state=seed)
        df = df.drop(train.index)
        valid = df.sample(frac=0.5,random_state=seed)
        df = df.drop(valid.index)
        test = df.sample(frac=1,random_state=seed)

        X_train = train.iloc[:,0:2]
        Y_train = train.iloc[:,2]
        X_valid = valid.iloc[:,0:2]
        Y_valid = valid.iloc[:,2]
        X_test = test.iloc[:,0:2]
        Y_test = test.iloc[:,2]
        return X_train,Y_train,X_valid,Y_valid,X_test,Y_test
    except Exception:
        exit(1)


def create_model(n):
    #Criando um modelo sequencial
    model = models.Sequential()
    
    model.add(layers.Dense(2,activation="relu",input_dim = 2)) #Camada de input
    for size in n:
        model.add(layers.Dense(size,activation="relu"))
    model.add(layers.Dense(2,activation="softmax"))
    return model


def evaluate(model,X_train,Y_train,X_valid,Y_valid,X_test,Y_test):
    #Avaliando a acuracia e a perda do treino, validacao e teste
    model.evaluate(X_train, Y_train)
    model.evaluate(X_valid, Y_valid)
    model.evaluate(X_test, Y_test)

def plot_graphs(history,y_pred,Y_test):
    #Criando os graficos
    fig ,(ax1,ax2) = plt.subplots(2)

    #Grafico de loss e val_loss
    ax1.plot(history.history["loss"],label = "Loss")
    ax1.plot(history.history["val_loss"],label = "Valid")
    ax1.legend(loc = "upper right")

    #Grafico de acuracia 
    ax2.plot(history.history["accuracy"],label = "train")
    ax2.plot(history.history["val_accuracy"],label = "Valid")
    ax2.legend(loc = "upper right")

    #Heatmap da matriz de confusao
    y_pred_labels = [i.argmax() for i in y_pred]

    cm = tf.math.confusion_matrix(labels=Y_test, predictions=y_pred_labels)

    plt.figure(figsize = (10,7))
    sn.heatmap(cm, annot=True, fmt='d')
    plt.ylabel('Truth')
    plt.xlabel('Predicted')

    plt.show()


def main():
    seed = 13
    tf.random.set_seed(seed)
    epocas = 100
    otimizador = "Adam"
    path = "./data.csv"

    X_train,Y_train,X_valid,Y_valid,X_test,Y_test = create_df(path,seed)

    model = create_model([2,4,8])
    model.compile(loss='sparse_categorical_crossentropy', optimizer=otimizador, metrics=['accuracy'])

    checkpoint_filepath = "./best.weights.h5"

    model_checkpoint_callback = callbacks.ModelCheckpoint(
        filepath=checkpoint_filepath,
        save_weights_only=True,
        monitor='val_accuracy',
        mode='max',
        save_best_only=True)

    history = model.fit(X_train, Y_train, 
                    epochs=epocas, 
                    batch_size=20, 
                    validation_data=(X_valid, Y_valid), 
                    shuffle=True, 
                    callbacks=[model_checkpoint_callback],
                    verbose=1)
    


    y_pred = model.predict(X_test)

    #Avaliando a rede
    model.load_weights(checkpoint_filepath)
    
    evaluate(model,X_train,Y_train,X_valid,Y_valid,X_test,Y_test)
    plot_graphs(history,y_pred,Y_test)

if __name__ == "__main__":
    main()