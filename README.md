# saltybet-homemade-amateur

L'objectif de ce projet est de faire un mini serveur Salty Bet.

## Variables d'environnements

`BETS_OPEN` : bool
Si `True`, les utilisateurs peuvent placer leurs bets. Sinon non. Par défaut : `False`

`BET_MULTIPLIER`: float
Valeur du multiplcateur de bets. Par défaut : 1


## Routes pour le MJ

Toutes ces routes nécessiteront d'avoir une valeur `auth_token` dans le body de la request, pour confirmer qu'il s'agisse bien du MJ. Erreur 403 si le token est incorrect.

### /init

#### POST
Purge l'intégralité de la base et réinitialise complètement la base (joueurs et bets). A utiliser avec modération.
200 si OK, 500 si erreur.


### /open_bets

#### PUT

Ne fait rien si `BETS_OPEN` est `True`. Passe `BETS_OPEN` à True et efface la table des ongoing bets sinon.
200 si OK, 500 si erreur.



### /close_bets

#### PUT

Ne fait rien si `BETS_OPEN` est `False`. Passe `BETS_OPEN` à False et attribue les bets aux vainqueurs/perdants sinon.
200 si OK, 500 si erreur.



### /bet_multiplier/{facteur}

#### PUT

`facteur` est un `float`. Modifie la valeur de `BET_MULTIPLIER`. La valeur doit être comprise entre 1 et 5.
200 si OK, 500 si erreur.



### /players/{player}

#### DELETE

Supprime le joueur de la base, ses bets actifs et son solde.
200 si OK, 404 si le joueur n'existe pas, 500 si erreur.


## Routes pour les joueurs

### /bet_multiplier

#### GET

Retourne la valeur de `BET_MULTIPLIER`
200 si OK, 500 si erreur.


### /players

#### GET

Retourne un dictionnaire avec la liste des joueurs présents et leur solde.
200 si OK, 500 si erreur.


### /players/{player}

#### GET

Retourne un dictionnaire avec en clé le nom du joueur, en valeur son solde.
Erreur 404 si le joueur n'existe pas.
200 si OK, 500 si erreur.



#### POST

Crée le joueur en base, avec un solde de 1000.
201 si OK, 200 si le joueur existe déjà, 500 si erreur.


### /players/{player}/rsa

#### PUT

Si le solde du joueur est strictement inférieur à 1000, set son solde à 1000.
Erreur 404 si le joueur n'existe pas.
200 si OK, 500 si erreur.


### /bets

Retourne un dictionnaire sous cette forme :
```javascript
{
    "1": [
        {"nom_joueur": 200}
        // Liste des bets sur le PLAYER 1
    ],
    "2": [
        {"nom_joueur_b": 200}
        // Liste des bets sur le PLAYER 2
    ]
}
```

Uniquement si `BETS_OPEN` est True, erreur 403 sinon.
200 si OK, 500 si erreur.


### /bets/{player}/{ia_champion}/{bet}

#### POST

Le joueur `player` (str) place un `bet` (float) sur le `ia_champion` (int mais valeurs uniquement possibles : 1 ou 2).
201 si OK (ajout à la valeur du bet déjà existant si un bet a déjà été placé).
402 si le bet est plus gros que le solde du joueur.
404 si le joueur n'existe pas.
500 si erreur.


### /bets/{player}/{ia_champion}/allin

#### POST

Le joueur `player` (str) mise tout son solde sur le `ia_champion` (int mais valeurs uniquement possibles : 1 ou 2).
