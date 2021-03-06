# Application Pur Beurre (Projet 8)

## **I. Présentation:**
                                       
<div align="center">
    <img src="/store/static/store/img/Screenshot.png">
</div>

Pur beurre est un application web qui permet d'effectuer une recherche des aliments et de trouver un produit de substitutions 
plus sain, que l'utilisateur peut ensuite enregister dans ses aliments de substitutions favoris après avoir créé un compte 
et s'être authentifié.
Cette application est en Python/Django et utilise les bases de données d'Openfoodfacts.
L'application peut être déployé sur un serveur Heroku.

**Fonctionnalités générales:**
- Sur la page d'accueil, l'utilisateur accède à un moteur de recherche qui va lui permettre d'effectuer une recherche sur un aliment de son choix.
  
  Il a également la posibilité de créer immédiatement un compte, lui permettant d'accéder à l'ensemble des fonctionnalité 
  de l'application (Sauvegader des substituts dans ses favoris, visualiser ses enregistements et modifier les données de son compte). 
- Après avoir lancé la recherche, une page affiche les aliments trouvés en fonction de la requête. L'utilisateur a la possiblité de voir 
  le détail d'un aliment en cliquant sur '+' ou de rechercher un aliment de substitution en cliquant sur la loupe.
  
- Après avoir effectué une recherche de substituts, la page des resultats s'affiche. Si l'utilisateur est authentifié, il peux alors 
  enregister un aliment dans ses favoris qui peux consulter en cliquant sur la carotte en haut à droite.
  
  Il peut également voir le détail d'un produit de substitution en cliquant sur '+'.
  
**Le système d'authentification:**

- L'utilisateur peut créer un compte par un clique sur l'icone situé en haut à droite.
- La page l'invite à s'authenfier par son adresse mail et son mot de passe si un compte à déjà été créé. Après validation du formulaire,
  l'utilisateur est rediriger vers la page d'accueil pour y saisir sa recherche. Les menus 'Favoris' et 'se déconnecté' son désormais affiché en haut à droite.
   
  Dans le cas ou l'utilisateur n'a pas encore créer de compte, il peut accéder à la page de création de compte en cliquant sur le lien
   "Je me connecte à un compte existant" au bas du formulaire.
- Sur la page d'authentification, l'utilisateur est invité à entrer ses données personnel par le biais du formulaire.
  Seules les données "adresse e-mail" et "mot de passe' sont necessaires, les autres données sont faculatifs.
  
  Après validation du formulaire, l'utilisateur est automatiquement authentifié et rediriger vers la page d'accueil pour y effectuer sa recherche.
  
  
**NB:** L'utilisateur peut effectuer une recherche à partir de n'importe quelle page par le biais du champs de recherche situé en haut de chaque page.
        Il suffit d'entrer la requête et appuyer sur la touche "Entrer" de son clavier.
 
  
## **II. Installation**

**Prérequis:**
1) Télécharger et installé le serveur de base de donnée PostgreSQL:  
   Voir la page:  <https://www.postgresql.org/download/>
2) Télécharger et installer Python3:  
    Voir le page: <https://www.python.org/downloads/>
3) installer pip dans votre terminal. (mode console):   
   Voir la page: <https://pip.pypa.io/en/stable/installing/>

**Installation du repository et de l'environement:**
1) Ouvrir votre therminal préféré et créer un répertoire pour le projet.  
   ex: `>>> mkdir mon_repertoire`
2) Installer un environement vituel (pipenv dans notre exemple)  
   ex: `>>> pip install pipenv`     
2) Cloner ou télécharger le repository Git du projet dans le répertoire que vous venez de créer. 
3) Aller dans le repertoire racine du projet.  
    ex: `ex: cd /pur_beurre`
4) Créer et démarrer votre environement virtuel pipenv:  
    ex: `>>> pipenv shell`
    NB: En tapant la commande 'ls' le fichier requirement.txt doit être visible.
5) Installer les requirements  
    `>>> pip install -r requirement.txt`  
6) Votre environement est créé, il vous reste à installer les bases de données (voir la suite)

#### **Installation de la base de donnée:**
1) Configurer les settings:  
    a) Ouvrer fichier 'settings.py' avec votre éditeur préféré qui se trouve depuis le racine du projet:  
        **/pur_beurre/settings.py**  
        (donc dans le répertoire: **/mon_projet/pur_beurre/pur_beurre/settings.py**)  
    b) Modifier la configuration pour l'accès à votre base de donnée:  
        Dans la section DATABASES:  
    >        DATABASES = {  
    >          'default': {  
    >                'ENGINE': 'django.db.backends.postgresql',   <-- Ne pas modifier
    >                'NAME': 'pur_beurre',   <-- Ne pas modifier sauf si vous souhaiter un autre nom pour votre base de donnée.
    >                'USER': 'votre_nom_d'utilisateur',   <-- Remplacez par le nom d'utilisateur que vous avez utilisé lors de l'installation du serveur PostgreSQL
    >                'PASSWORD': '',   <-- Entrer le mot de passe de configuration de votre serveur
    >                'HOST': '',   <-- Entrer l'addresse de votre serveur s'il n'est pas en local
    >                'PORT': '5432',   <-- Ne pas modifier, sauf si vous avez changer le port par défaut de votre serveur PostgreSQL
    >            }
    >         }

2) Créer la base de donnée, les tables et peupler (remplir) les tables:  
    Retourner dans votre environement virtuel activé (à la racine de l'application '/mon_repertoire/pur_beurre' et entrer les commandes suivantes;   
    a) Créer la base de donnée:  
       `>>> createdb -O votre_nom_utilisateur pur_beurre`   <-- Non d'utilisateur et nom de la base de donnée défini dans settings.py   
    b) Créer les tables:  
       `>>> python manage.py migrate` ou le racourci `>>> ./manage.py migrate`
    c) Peupler les tables avec les données d'openfoodfacts:
       `>>> python manage.py update_db` ou le racourci `>>> ./manage.py update_db`
       
#### **Démarrer le serveur de développement:**  
  -   Toujours dans la console:  
        `>>> python manage.py runserver`
    
   **NB:** Ne pas démarrer le serveur de développement sur le serveur de production.
   
Vous pouvez vous rendre à l'adresse local indiquée dans le terminal avec votre navigateur web préféré.  
Ex: http://127.0.0.1:800 ou http://localhost:8000
   
## **III. Le déploiement sur serveur Heroku:**

**Prérequis:**  
Créer un compte sur heroku à l'adresse suivante:  
<https://www.heroku.com/>

#### **Installation**
1. Créer une nouvelle application heroku.  
   `>>> heroku create nom_application`
2. Créer les variables d'environement sur le serveur:  
   a) La variable ENV:  
   `>>> heroku config;set ENV=PRODUCTION`  
   b) La clé secrête de l'application:   
        - Générer d'abord une nouvelle clé.  
         `>>> import randon, string`   
         `>>> "".join([random.choice(string.printable) for _ in range(24)])`  
         Copier le résultat obtenu. 
        - Placer la clé en variable d'enrironement sur heroku.  
         `>>> heroku config:set SECRET_KEY='coller ici la clé généré'` <-- coller la clé généré entre guillements simple ( ' )  
3. Pusher le repository sur serveur avec Git:  
    `git push heroku master`
    
4. Créer les tables de la base de données et les peupler:
    b) Créer les tables:  
       `>>> python manage.py migrate`  
    b) Peupler les tables avec les données d'openfoodfacts:  
       `>>> python manage.py update_db`
       
    NB: Vous ne pouvez pas utiliser les commandes raccoucis comme aux l'étapes 2b et 2c.
    
 
Si tout c'est bien passé, vous pouvez vous rendre à l'adresse du serveur heroku avec votre navigateur web préféré.   
 Exemple: http://le-nom-de-votre-app.herokuapp.com  
   
   
    
    
       
       
     
    


