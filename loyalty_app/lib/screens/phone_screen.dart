import 'package:flutter/material.dart';

class PhoneScreen extends StatelessWidget {
  const PhoneScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Loyalty App'),
        backgroundColor: Colors.deepPurple,
      ),
      body: SingleChildScrollView( // Ajout d'un scroll pour les petits écrans
        child: Center(
          child: Padding(
            padding: const EdgeInsets.all(20.0), // Ajouter un peu de marge autour des éléments
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                // Titre du téléphone ou de l'application
                Text(
                  'Bienvenue sur l\'application Loyalty!',
                  style: Theme.of(context).textTheme.titleLarge,
                  textAlign: TextAlign.center, // Centrer le texte
                ),
                const SizedBox(height: 40), // Augmenter l'espace entre les éléments

                // Bouton "Voir les Marques"
                ElevatedButton(
                  onPressed: () => Navigator.pushNamed(context, '/brands'),
                  child: const Text('Voir les Marques'),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.deepPurple, // Couleur du bouton
                    padding: const EdgeInsets.symmetric(horizontal: 50, vertical: 15),
                  ),
                ),
                const SizedBox(height: 20),

                // Bouton "Voir mes Gains"
                ElevatedButton(
                  onPressed: () => Navigator.pushNamed(context, '/gains'),
                  child: const Text('Voir mes Gains'),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.deepPurple, // Couleur du bouton
                    padding: const EdgeInsets.symmetric(horizontal: 50, vertical: 15),
                  ),
                ),
                const SizedBox(height: 20),

                // Bouton "Voir mes Tickets"
                ElevatedButton(
                  onPressed: () => Navigator.pushNamed(context, '/receipts'),
                  child: const Text('Voir mes Tickets'),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.deepPurple, // Couleur du bouton
                    padding: const EdgeInsets.symmetric(horizontal: 50, vertical: 15),
                  ),
                ),
                const SizedBox(height: 40),

                // Bouton de connexion
                ElevatedButton(
                  onPressed: () => Navigator.pushNamed(context, '/login'),
                  child: const Text('Se connecter'),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.grey, // Couleur du bouton
                    padding: const EdgeInsets.symmetric(horizontal: 50, vertical: 15),
                  ),
                ),
                const SizedBox(height: 20),

                // Bouton d'inscription
                ElevatedButton(
                  onPressed: () => Navigator.pushNamed(context, '/register'),
                  child: const Text('S\'inscrire'),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.grey, // Couleur du bouton
                    padding: const EdgeInsets.symmetric(horizontal: 50, vertical: 15),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
