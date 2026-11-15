PRONOCOTE PRO - SOURCE ANDROID
Version de travail : 1.1.0

CONTENU
- main.py : application Android Kivy et logique de calcul
- logo.png : emblème royal noir / vert / or
- icon.png : icône Android
- buildozer.spec : paramètres de compilation Android
- .github/workflows/android.yml : compilation APK automatique sur GitHub Actions

LES TROIS CLÉS API
1. API-Football : matchs et données football disponibles selon le forfait du fournisseur.
2. The Odds API : cotes des bookmakers disponibles selon le sport, le pays et le quota.
3. Groq : synthèse IA du match.

Les trois clés sont distinctes. Ouvrir l'application > Clé API, coller chaque clé dans le champ correspondant, appuyer sur Enregistrer, puis sur Tester. Les clés ne sont pas intégrées au code source et ne doivent jamais être publiées dans GitHub.

ANALYSE
- Mode manuel : saisir les équipes, les cotes éventuelles et les buts attendus.
- Mode automatique : recherche des cotes via The Odds API.
- Calculs Poisson : 1/N/2, score indicatif, Over/Under et BTTS.
- Estimation de mi-temps à partir d'une fraction des buts attendus.
- API-Football et Groq enrichissent l'analyse lorsque les clés sont configurées.

LIMITES IMPORTANTES
- Les probabilités et scores sont des estimations, pas des garanties.
- Les cotes automatiques dépendent des compétitions et marchés réellement couverts par The Odds API.
- Les données de joueurs, cartons, compositions et buteurs ne sont pas inventées lorsqu'elles ne sont pas disponibles dans les réponses des API.
- Les tests effectués sur cette livraison vérifient la syntaxe Python et la structure de l'archive. La compilation Android complète doit encore être exécutée par GitHub Actions pour produire un APK installable.

COMPILATION APK
1. Décompresser le dossier PronoCote_Android.
2. Envoyer tout son contenu dans la branche main du dépôt GitHub, en conservant le dossier .github/workflows/android.yml.
3. Dans GitHub, ouvrir Actions puis le workflow "Build PronoCote Android APK" et lancer "Run workflow" si le lancement automatique n'a pas démarré.
4. Lorsque le travail est terminé avec succès, ouvrir le résultat et télécharger l'artefact "PronoCote-Android-APK". L'APK se trouve dans cette archive d'artefact.
