import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Calcul des Gains',
      theme: ThemeData(
        primarySwatch: Colors.teal, // Changement de couleur
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: GainsPage(),
    );
  }
}

class GainsPage extends StatefulWidget {
  @override
  _GainsPageState createState() => _GainsPageState();
}

class _GainsPageState extends State<GainsPage> {
  // Exemple de liste des tickets d'achats précédents
  List<Map<String, dynamic>> tickets = [
    {'magasin': 'Magasin A', 'montant': 120.0},
    {'magasin': 'Magasin B', 'montant': 50.0},
    {'magasin': 'Magasin C', 'montant': 200.0},
  ];

  double remisePourcentage = 10.0;
  double montantTotalAchats = 0.0;

  double getMontantTotalAchats() {
    montantTotalAchats = tickets.fold(
      0.0,
      (sum, ticket) => sum + ticket['montant'],
    );
    return montantTotalAchats;
  }

  double getRemise(double montant) {
    return (montant * remisePourcentage) / 100;
  }

  double getMontantApresRemise(double montant) {
    return montant - getRemise(montant);
  }

  int getPointsRecompense(double montant) {
    return getMontantApresRemise(montant).toInt();
  }

  @override
  Widget build(BuildContext context) {
    double totalAchats = getMontantTotalAchats();

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.teal, // Changement de couleur dans l'AppBar
        title: Text('Calcul des Gains', style: TextStyle(color: Colors.white)),
        elevation: 0,
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              // Titre principal avec style moderne
              Text(
                'Votre Calcul de Gains',
                style: TextStyle(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                  color: Colors.teal, // Changement de couleur ici aussi
                ),
              ),
              SizedBox(height: 30),

              // Affichage du montant total des achats
              Text(
                'Total des achats : €${totalAchats.toStringAsFixed(2)}',
                style: TextStyle(fontSize: 20, color: Colors.black87),
              ),
              SizedBox(height: 20),

              // Carte des résultats avec un design moderne
              Container(
                padding: EdgeInsets.all(20),
                margin: EdgeInsets.symmetric(vertical: 10),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(18),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.grey.withOpacity(0.2),
                      spreadRadius: 4,
                      blurRadius: 10,
                    ),
                  ],
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Titre de la section avec un design moderne
                    Text(
                      'Détails de votre paiement',
                      style: TextStyle(
                        fontSize: 22,
                        fontWeight: FontWeight.w600,
                        color: Colors.teal, // Changement de couleur
                      ),
                    ),
                    SizedBox(height: 15),

                    // Affichage des informations calculées
                    _buildInfoCard(
                      'Montant total des achats',
                      '€${totalAchats.toStringAsFixed(2)}',
                    ),
                    _buildInfoCard(
                      'Remise appliquée',
                      '€${getRemise(totalAchats).toStringAsFixed(2)}',
                    ),
                    _buildInfoCard(
                      'Montant après remise',
                      '€${getMontantApresRemise(totalAchats).toStringAsFixed(2)}',
                    ),
                    _buildInfoCard(
                      'Points de Récompense',
                      '${getPointsRecompense(totalAchats)} points',
                    ),
                  ],
                ),
              ),

              // Affichage des tickets scannés avec un style moderne
              Text(
                'Vos tickets scannés :',
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 10),
              ...tickets.map((ticket) {
                return Padding(
                  padding: const EdgeInsets.symmetric(vertical: 5.0),
                  child: Card(
                    elevation: 4,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(15),
                    ),
                    color:
                        Colors
                            .teal[50], // Changement de couleur pour les cartes
                    child: ListTile(
                      title: Text(ticket['magasin']),
                      subtitle: Text(
                        'Montant: €${ticket['montant'].toStringAsFixed(2)}',
                      ),
                    ),
                  ),
                );
              }).toList(),
            ],
          ),
        ),
      ),
    );
  }

  // Widget réutilisable pour afficher chaque information avec un design moderne
  Widget _buildInfoCard(String title, String value) {
    return Container(
      padding: EdgeInsets.symmetric(vertical: 10),
      margin: EdgeInsets.only(bottom: 15),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(18),
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(0.2),
            spreadRadius: 2,
            blurRadius: 8,
          ),
        ],
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            title,
            style: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.w600,
              color: Colors.teal, // Changement de couleur
            ),
          ),
          Text(
            value,
            style: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.w500,
              color: Colors.black87,
            ),
          ),
        ],
      ),
    );
  }
}
