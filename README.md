                                        **Pur Beurre** 

###### **I Présentation:** 
                                       
<div align=""center">
    <img src="/store/static/store/img/Screenshot.png"></img>
</div>

Pur beurre est un application web qui permet d'effectuer une recherche des aliments et de trouver un produit de substitutions 
plus sain, que l'utilisateur peut ensuite enregister dans ses aliments de substitutions favoris après avoir créé un compte 
et s'être authentifié.
Cette application est en Python/Django et utilise les bases de données d'Openfoodfacts.

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
 
  
###### **II Installation**
1) Créer un répertoire racine pour le projet ex: projet_pur_beurre
2) Cloner ou télécharger le repository Git du projet dans votre répertoire racine. 
3) Aller dans votre repertoire en mode console (ex: cd /projet_pur_beurre)
4) Créer et activer un environement virtuel virtualenv:
    - **Installer virtualenv**  
    `pip install vistualenv`
    - **Créer l'environement vituel**   
    `virtualenv venv`
    - **Activer l'environement virtuel**  
    `source venv/bin/activate`
5) Installer les requirements  
    `pip install -r requirement.txt`
    
6) 
  
   