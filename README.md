# **Déploiement d'une application web avec pipeline CI/CD vers Azure**
Déploiement d'une application python/flask pour calculer l'indice de masse corporelle (IMC/BMI) et le métabolisme de base (MB/BMR)

## **Pré-requis**
Avant de démarrer, assurez-vous de disposer des éléments suivants :

- Docker, python 3.9 ou + et make installés sur votre système.
- Git pour cloner le dépôt du projet.
- Un éditeur de texte pour modifier les fichiers de configuration si nécessaire. (vi, nano, etc)

Vous trouverez les informations concernant Docker [ici](https://www.docker.com/)., et les instructions pour l'installer [ici](https://docs.docker.com/).

## **Installation**
Utilisez git pour cloner le dépôt

`bash`
```bash
git clone <url_du_depot>
```

## **Etapes de construction**
Génération du fichier `app.py` avec les points de terminaisons pour `/imc` et `/mb`  
![app.py](assets/app-py.png)  

Génération du fichier `health-utils.py` contenant les fonctions utilisées `calculate_imc` et `calculate_mb`  
![health-utils](assets/health-utils.png)  

Génération du `Dockerfile`  
![Dockerfile](assets/Dockerfile.png)  

Génération du fichier `requirements.txt` pour spécifier la version de Flask et de ses dépendances  
![requirements](assets/requirements.png)  

Génération du fichier `makefile`  
![Makefile](assets/Makefile.png)  

Génération du fichier `test.py`  
![tests-py](assets/test-py.png)  

Test de fonctionnement de la fonction `calculate_imc` en local  
![curl-test-imc](assets/curl-test-imc.png)  

Test de fonctionnement de la fonction `calculate_mb` en local  
![curl-test-mb](assets/curl-test-mb.png)  

Test de la commande `make init`  
![make-init](assets/make-init.png)  

Test de la commande `make run`  
![make-run](assets/make-run.png)  

Test de la commande `make test`  
![make-test](assets/make-test.png)  

Test de la commande `make build`  
![make-build](assets/make-build.png)  

Vérification des fichiers avec `git status`  
![git-status](assets/git-status.png)  

Mise en place du commit avec les commandes `git add .` et `git commit -m "Commit initial"`
![git-commit](assets/git-commit.png)  

Définition du git comme remote origin et push des fichiers  
![git-push-origin](assets/git-push-origin.png)  

Configuration de la machine sur Azure  
![azure-web-app-config](assets/azure-web-app-config.png)  

Configuration du déploiement via github  
![deploiment-github](assets/deploiement-github.png)  

Azure génère ensuite automatiquement le fichier yml pour la remontée  
![azure-ci-cd-yml](assets/azure-ci-cd-yml.png)  

Afin de faire fonctionner notre propre `ci-cd.yml` on récupère le profil de publication sur Azure  
![profil-publication](assets/profil-publication.png)  

On ajoute le profil de publication dans les secrets et variables de notre repository github  
 

On modifie la ligne correspondante de notre `ci-cd.yml` pour qu'elle corresponde au secret généré  
![modified-ci-cd-yml](assets/modified-ci-cd-yml.png)  

Les pipelines remontent bien  
![pipeline-remontent](assets/pipeline-remontent.png)  

## **Test de l'application sur Azure**
Test de la fonction `calculate_imc`  
![test-imc-azure](assets/test-imc-azure.png)  

Test de la fonction `calculate_mb` pour un homme  
![test-mb-homme-azure](assets/test-mb-homme-azure.png)  

Test de la fonction `calculate_mb` pour une femme  
![test-mb-femme-azure](assets/test-mb-femme-azure.png)  
