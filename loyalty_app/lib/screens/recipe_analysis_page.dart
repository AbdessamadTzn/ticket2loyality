import 'package:flutter/material.dart';

class RecipeAnalysisPage extends StatelessWidget {
  const RecipeAnalysisPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Analysing your recipe'),
        backgroundColor: Colors.deepPurple,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Message Lorem Ipsum
            const Text(
              'Qorem ipsum dolor sit amet, onsectetur.',
              style: TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 20),

            // Informations sur le magasin et produit
            const Text(
              'Nom du magasin: Mon Magasin',
              style: TextStyle(
                fontSize: 16,
              ),
            ),
            const SizedBox(height: 10),
            const Text(
              '11/12/23',
              style: TextStyle(
                fontSize: 16,
                color: Colors.grey,
              ),
            ),
            const SizedBox(height: 10),
            const Text(
              'Nom du produit: Produit A',
              style: TextStyle(
                fontSize: 16,
              ),
            ),
            const SizedBox(height: 10),
            const Text(
              '12,33€',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 20),

            // Affichage du message de scan
            const Text(
              'Scaning...',
              style: TextStyle(
                fontSize: 18,
                color: Colors.orange,
              ),
            ),
            const SizedBox(height: 30),

            // Bouton pour ajouter un reçu
            ElevatedButton(
              onPressed: () {
                // Action pour ajouter un reçu
                print('Adding receipt...');
                // Ajouter ici la logique pour ajouter le reçu
              },
              child: const Text('Add Receipt'),
            ),
          ],
        ),
      ),
    );
  }
}
