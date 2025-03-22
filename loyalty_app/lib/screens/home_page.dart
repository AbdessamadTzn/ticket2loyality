import 'package:flutter/material.dart';
import 'package:loyalty_app/screens/brands_page.dart';
import 'package:loyalty_app/screens/gains_page.dart';
import 'package:loyalty_app/screens/receipts_page.dart';
import 'package:loyalty_app/screens/login_page.dart'; // Importation de la page Login
import 'package:loyalty_app/screens/register_page.dart'; // Importation de la page Register

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Accueil'),
        backgroundColor: Colors.deepPurple,
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              const Text(
                'Bienvenue dans l\'application de fidélité!',
                style: TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                  color: Colors.deepPurple,
                ),
              ),
              const SizedBox(height: 40), // Espacement entre le texte et les boutons
              ElevatedButton(
                onPressed: () => Navigator.pushNamed(context, '/brands'),
                child: const Text('Voir les Marques'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.deepPurple, // Couleur du bouton
                  padding: const EdgeInsets.symmetric(horizontal: 40, vertical: 15),
                  textStyle: const TextStyle(fontSize: 18),
                ),
              ),
              const SizedBox(height: 20), // Espacement entre les boutons
              ElevatedButton(
                onPressed: () => Navigator.pushNamed(context, '/gains'),
                child: const Text('Voir mes Gains'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.green, // Couleur du bouton
                  padding: const EdgeInsets.symmetric(horizontal: 40, vertical: 15),
                  textStyle: const TextStyle(fontSize: 18),
                ),
              ),
              const SizedBox(height: 20), // Espacement entre les boutons
              ElevatedButton(
                onPressed: () => Navigator.pushNamed(context, '/receipts'),
                child: const Text('Voir mes Tickets'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.blue, // Couleur du bouton
                  padding: const EdgeInsets.symmetric(horizontal: 40, vertical: 15),
                  textStyle: const TextStyle(fontSize: 18),
                ),
              ),
              const SizedBox(height: 40), // Espacement entre les boutons
              ElevatedButton(
                onPressed: () => Navigator.pushNamed(context, '/login'),
                child: const Text('Connexion'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.orange, // Couleur du bouton de connexion
                  padding: const EdgeInsets.symmetric(horizontal: 40, vertical: 15),
                  textStyle: const TextStyle(fontSize: 18),
                ),
              ),
              const SizedBox(height: 20), // Espacement entre les boutons
              ElevatedButton(
                onPressed: () => Navigator.pushNamed(context, '/register'),
                child: const Text('S\'inscrire'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.pink, // Couleur du bouton d'inscription
                  padding: const EdgeInsets.symmetric(horizontal: 40, vertical: 15),
                  textStyle: const TextStyle(fontSize: 18),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
