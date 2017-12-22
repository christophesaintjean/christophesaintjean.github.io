% Une expérimentation autour de l'exploitation de données images annotées dans une architecture client-serveur.
% **[Christophe Saint-Jean]**, Julien Thérin
% Mercredi 14 Juin 2017
% Journée Python Scientifique

## Contexte applicatif

- CPER


## Contexte recherche

- Développer de nouveaux modèles

# Yolo

## Yolo (Spécification)

- Réseau convolutif 

- 145 M de paramètres

## Yolo (Keras)

```python
    model = Sequential()
    model.add(Conv2D(filters=16, kernel_size=(3, 3), input_shape=(3, 448, 448), padding='same'))
    model.add(LeakyReLU(alpha=0.1))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=32, kernel_size=(3, 3), padding='same'))
    model.add(LeakyReLU(alpha=0.1))
    ...
    model.add(Conv2D(filters=1024, kernel_size=(3, 3), padding='same'))
    model.add(LeakyReLU(alpha=0.1))
    model.add(Flatten())
    ...
    model.add(Dense(cells_h * cells_w * (classes + boxes_per_cell * 5)))
```

## Yolo (Utilisation)

- Mode Entrainement

- Mode Prédiction

## Conclusions / Perspectives
- Robot Turtle Bot 3 : 
- [TensorFlow serving](https://tensorflow.github.io/serving/)

[Christophe Saint-Jean]: https://sites.google.com/site/csaintje/
